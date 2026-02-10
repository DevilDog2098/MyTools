# USB Security Awareness Test Tool

A Python-based security awareness training tool that educates employees about the dangers of plugging in unknown USB devices.

## 📋 Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Building the Executable](#building-the-executable)
- [USB Drive Setup](#usb-drive-setup)
- [Deployment](#deployment)
- [Monitoring Results](#monitoring-results)
- [Troubleshooting](#troubleshooting)
- [Best Practices](#best-practices)

---

## 🎯 Overview

This tool creates an executable that:
- Logs username, computer name, timestamp, and OS when executed
- Displays a security awareness message
- Saves logs to a hidden file on the USB drive
- Looks like a legitimate document (Word/PDF)

**Important:** Ensure you have written authorization from management before deploying this test.

---

## ✅ Prerequisites

### Required Software

1. **Python 3.8 or newer**
   - Download from: https://www.python.org/downloads/
   - During installation, check "Add Python to PATH"

2. **PyInstaller** (will be installed in next steps)

3. **Icon file** (.ico format)
   - Download a Word icon from: https://icon-icons.com/icon/word-office/143552
   - Or PDF icon from: https://icon-icons.com/icon/pdf-file/143591
   - Save as `word.ico` or `pdf.ico`

### System Requirements

- Windows 10 or 11
- Administrator privileges (for installation only)
- At least 500 MB free disk space

---

## 📦 Installation

### Step 1: Install Python

1. Go to https://www.python.org/downloads/
2. Download the latest Python 3 installer
3. Run the installer
4. **IMPORTANT:** Check ✅ "Add Python to PATH"
5. Click "Install Now"
6. Wait for installation to complete
7. Click "Close"

### Step 2: Verify Python Installation

1. Press `Win + R`
2. Type `cmd` and press Enter
3. In the command prompt, type:
```cmd