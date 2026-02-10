# USB Executable Blocker

A Python script that monitors USB drives and prevents executable files from running or being transferred to the system.

## Features

- **Real-time monitoring**: Detects when USB drives are plugged in
- **Automatic scanning**: Scans existing files when a drive is connected
- **File blocking**: Makes executable files read-only to prevent execution
- **Live protection**: Monitors for new files being copied to USB drives
- **Comprehensive logging**: Logs all activities to file and console
- **Optional quarantine**: Can move suspicious files to a quarantine folder

## Requirements

- Python 3.7 or higher
- Administrator/root privileges
- Windows, Linux, or macOS

## Installation

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Windows
Run as Administrator:
```cmd
python usb_executable_blocker.py
```

### Linux/Mac
Run with sudo:
```bash
sudo python3 usb_executable_blocker.py
```

## How It Works

1. **Detection**: Monitors the system for removable USB drives
2. **Initial Scan**: When a drive is detected, scans all existing files
3. **Blocking**: Sets executable files to read-only (chmod 444)
4. **Monitoring**: Watches for new files being created or copied
5. **Prevention**: Immediately blocks any new executables

## Blocked File Types

The script blocks the following executable extensions:
- Windows: .exe, .bat, .cmd, .com, .msi, .scr, .vbs, .js, .ps1, .dll, .sys
- Cross-platform: .jar, .sh, .run
- Linux: .deb, .rpm
- macOS: .app

## Configuration Options

### Enable Quarantine Mode
Uncomment the quarantine lines in the code:
```python
# Change this line:
# self.quarantine_file(file_path)
# To:
self.quarantine_file(file_path)
```

This will move blocked files to `~/USB_Quarantine/` instead of just blocking them.

### Add Custom Extensions
Edit the `EXECUTABLE_EXTENSIONS` set:
```python
EXECUTABLE_EXTENSIONS = {
    '.exe', '.bat', # ... add your extensions here
}
```

### Adjust Monitoring Interval
Change the sleep time in the monitor loop:
```python
time.sleep(2)  # Check every 2 seconds
```

## Logs

All activities are logged to:
- Console output (real-time)
- `usb_blocker.log` (persistent file)

## Important Security Notes

⚠️ **Authorization Required**: Only use this on systems you own or have explicit permission to manage.

⚠️ **Elevated Privileges**: This script requires administrator/root access to:
- Monitor USB devices
- Modify file permissions
- Access all drive contents

⚠️ **Legitimate Use Cases**:
- Corporate security policies
- Protected workstations in sensitive environments
- Personal device protection
- Educational/lab environments

## Limitations

- Requires elevated privileges to run
- Cannot block files already being executed
- May not work with encrypted USB drives
- Some file systems may not support permission changes
- Determined users with admin rights could bypass this

## Enhanced Security Recommendations

For enterprise environments, consider:
1. Group Policy Objects (Windows) or MDM solutions
2. Hardware-based USB blocking
3. Endpoint Detection and Response (EDR) tools
4. Application whitelisting
5. USB port physical locks

## Stopping the Script

Press `Ctrl+C` to gracefully shutdown the monitor.

## Troubleshooting

**"Permission Denied" errors**
- Ensure you're running with administrator/root privileges

**USB drives not detected**
- Check if the drive is properly mounted
- Verify the drive appears in your file manager

**Files still executing**
- The script can only block new files or files it's scanned
- Files already running cannot be stopped
- Some operating systems cache executables

## License

Use responsibly and only on systems you're authorized to manage.
