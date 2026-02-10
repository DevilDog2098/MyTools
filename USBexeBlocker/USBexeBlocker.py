import os
import time
import psutil
import threading
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging

# Configure logging
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('usb_blocker.log'),
        logging.StreamHandler()
    ]
)

# Executable extensions to block
EXECUTABLE_EXTENSIONS = {
    '.exe', '.bat', '.cmd', '.com', '.msi', '.scr', '.vbs', 
    '.js', '.jar', '.app', '.deb', '.rpm', '.run', '.sh',
    '.ps1', '.psm1', '.psd1', '.dll', '.sys'
}

class USBMonitor:
    def __init__(self):
        self.monitored_drives = set()
        self.observers = {}
        
    def get_removable_drives(self):
        """Detect all removable USB drives"""
        removable_drives = []
        
        for partition in psutil.disk_partitions():
            # Check if it's a removable drive
            if 'removable' in partition.opts.lower() or 'usb' in partition.device.lower():
                removable_drives.append(partition.mountpoint)
        
        return removable_drives
    
    def scan_and_block_executables(self, drive_path):
        """Scan a drive for executable files and block them"""
        blocked_count = 0
        
        try:
            for root, dirs, files in os.walk(drive_path):
                for file in files:
                    file_path = Path(root) / file
                    
                    # Check if file has executable extension
                    if file_path.suffix.lower() in EXECUTABLE_EXTENSIONS:
                        try:
                            # Make file read-only and remove execute permissions
                            file_path.chmod(0o444)
                            logging.warning(f"BLOCKED: {file_path}")
                            blocked_count += 1
                            
                            # Optional: Move to quarantine folder
                            # self.quarantine_file(file_path)
                            
                        except Exception as e:
                            logging.error(f"Error blocking {file_path}: {e}")
        
        except Exception as e:
            logging.error(f"Error scanning drive {drive_path}: {e}")
        
        if blocked_count > 0:
            logging.info(f"Blocked {blocked_count} executable(s) on {drive_path}")
        
        return blocked_count
    
    def quarantine_file(self, file_path):
        """Move suspicious file to quarantine folder"""
        quarantine_dir = Path.home() / "USB_Quarantine"
        quarantine_dir.mkdir(exist_ok=True)
        
        try:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            new_name = f"{timestamp}_{file_path.name}"
            quarantine_path = quarantine_dir / new_name
            
            file_path.rename(quarantine_path)
            logging.info(f"QUARANTINED: {file_path} -> {quarantine_path}")
        except Exception as e:
            logging.error(f"Error quarantining {file_path}: {e}")
    
    def start_monitoring(self, drive_path):
        """Start monitoring a USB drive for new files"""
        if drive_path not in self.monitored_drives:
            event_handler = USBFileHandler(self)
            observer = Observer()
            observer.schedule(event_handler, drive_path, recursive=True)
            observer.start()
            
            self.observers[drive_path] = observer
            self.monitored_drives.add(drive_path)
            logging.info(f"Started monitoring: {drive_path}")
    
    def stop_monitoring(self, drive_path):
        """Stop monitoring a USB drive"""
        if drive_path in self.monitored_drives:
            observer = self.observers.get(drive_path)
            if observer:
                observer.stop()
                observer.join()
                del self.observers[drive_path]
            
            self.monitored_drives.remove(drive_path)
            logging.info(f"Stopped monitoring: {drive_path}")
    
    def monitor_usb_drives(self):
        """Continuously monitor for USB drives being plugged in/out"""
        logging.info("USB Executable Blocker started")
        logging.info(f"Monitoring for executable extensions: {EXECUTABLE_EXTENSIONS}")
        
        while True:
            try:
                current_drives = set(self.get_removable_drives())
                
                # Check for newly connected drives
                new_drives = current_drives - self.monitored_drives
                for drive in new_drives:
                    logging.info(f"NEW USB DRIVE DETECTED: {drive}")
                    
                    # Scan existing files
                    self.scan_and_block_executables(drive)
                    
                    # Start monitoring for new files
                    self.start_monitoring(drive)
                
                # Check for disconnected drives
                removed_drives = self.monitored_drives - current_drives
                for drive in removed_drives:
                    logging.info(f"USB DRIVE REMOVED: {drive}")
                    self.stop_monitoring(drive)
                
                time.sleep(2)  # Check every 2 seconds
                
            except KeyboardInterrupt:
                logging.info("Shutting down USB monitor...")
                break
            except Exception as e:
                logging.error(f"Error in monitor loop: {e}")
                time.sleep(5)
        
        # Cleanup
        for drive in list(self.monitored_drives):
            self.stop_monitoring(drive)


class USBFileHandler(FileSystemEventHandler):
    """Handler for file system events on USB drives"""
    
    def __init__(self, usb_monitor):
        self.usb_monitor = usb_monitor
    
    def on_created(self, event):
        """Called when a file is created"""
        if event.is_directory:
            return
        
        file_path = Path(event.src_path)
        
        # Check if it's an executable
        if file_path.suffix.lower() in EXECUTABLE_EXTENSIONS:
            try:
                logging.warning(f"EXECUTABLE DETECTED: {file_path}")
                
                # Block the file immediately
                time.sleep(0.1)  # Small delay to ensure file is written
                file_path.chmod(0o444)
                
                logging.warning(f"BLOCKED NEW FILE: {file_path}")
                
                # Optional: Quarantine instead of just blocking
                # self.usb_monitor.quarantine_file(file_path)
                
            except Exception as e:
                logging.error(f"Error blocking new file {file_path}: {e}")
    
    def on_modified(self, event):
        """Called when a file is modified"""
        if event.is_directory:
            return
        
        file_path = Path(event.src_path)
        
        # Re-check if executable
        if file_path.suffix.lower() in EXECUTABLE_EXTENSIONS:
            try:
                # Ensure it stays blocked
                file_path.chmod(0o444)
            except Exception as e:
                logging.error(f"Error maintaining block on {file_path}: {e}")


def main():
    # Check if running with appropriate permissions
    if os.name == 'nt':  # Windows
        import ctypes
        if not ctypes.windll.shell32.IsUserAnAdmin():
            logging.error("This script requires administrator privileges on Windows!")
            logging.error("Please run as Administrator.")
            return
    else:  # Linux/Mac
        if os.geteuid() != 0:
            logging.error("This script requires root privileges on Linux/Mac!")
            logging.error("Please run with sudo.")
            return
    
    monitor = USBMonitor()
    
    try:
        monitor.monitor_usb_drives()
    except KeyboardInterrupt:
        logging.info("\nShutdown requested by user")
    except Exception as e:
        logging.error(f"Fatal error: {e}")


if __name__ == "__main__":
    main()