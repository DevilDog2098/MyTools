# build.py
import PyInstaller.__main__
import os

# Configuration
script_name = 'security_test.py'
output_name = 'Q3_Financial_Report'  # Change this to your desired filename
icon_file = 'word.ico'  # Your icon file

# Build arguments
args = [
    script_name,
    '--onefile',                    # Single executable file
    '--noconsole',                  # No console window
    '--name=' + output_name,        # Output filename
    '--icon=' + icon_file,          # Icon file
    '--clean',                      # Clean cache
    '--noconfirm',                  # Don't ask for confirmation
]

# Run PyInstaller
PyInstaller.__main__.run(args)

print(f"\n✓ Build complete! Executable is in the 'dist' folder.")
print(f"✓ File: dist/{output_name}.exe")