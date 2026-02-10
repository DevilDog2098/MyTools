# USB Security Toolkit

A comprehensive toolkit for IT administrators to manage and test USB security policies in enterprise environments.

## 📋 Overview

This repository contains two complementary security tools designed to help IT departments protect against USB-based threats:

1. **USB Exe Blocker** - Prevents unauthorized executables from running on USB drives
2. **USB Security Awareness Test** - Tests employee awareness of USB security risks

## 🛠️ Tools Included

### 1. USB Exe Blocker
**Location:** `/usb-exe-blocker/`

A security enforcement tool that prevents executable files from running on removable USB drives, protecting your network from malware and unauthorized software.

**Use Cases:**
- Enforce organizational security policies
- Prevent malware execution from USB drives
- Block unauthorized software installation
- Protect endpoints from USB-based attacks

**[→ View USB Exe Blocker Documentation](./usb-exe-blocker/README.md)**

---

### 2. USB Security Awareness Test
**Location:** `/usb-security-test/`

An educational tool that simulates a USB-based attack to test and train employees on proper USB security practices.

**Use Cases:**
- Security awareness training
- Employee security education
- Identify security training needs
- Measure security culture improvement
- Compliance with security training requirements

**[→ View USB Security Test Documentation](./usb-security-test/README.md)**

---

## 🎯 When to Use Each Tool

| Scenario | Recommended Tool |
|----------|------------------|
| Prevent all USB executables from running | **USB Exe Blocker** |
| Test employee security awareness | **USB Security Awareness Test** |
| Enforce strict security policy | **USB Exe Blocker** |
| Educate users about USB threats | **USB Security Awareness Test** |
| Block malware on USB drives | **USB Exe Blocker** |
| Measure security training effectiveness | **USB Security Awareness Test** |
| Permanent security control | **USB Exe Blocker** |
| Temporary training exercise | **USB Security Awareness Test** |

## 🚀 Quick Start

### For IT Administrators - Enforcement

If you want to **prevent** USB executables from running:
```bash
