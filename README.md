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

**[→ View USB Exe Blocker Documentation](./USBexeBlocker/README.md)**

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

**[→ View USB Security Test Documentation](./USBSecurityTest/README.md)**

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
cd usb-exe-blocker
# Follow the README.md in that folder
```

### For Security Training - Education

If you want to **test and educate** employees:
```bash
cd usb-security-test
# Follow the README.md in that folder
```

## 📁 Repository Structure
```
usb-security-toolkit/
│
├── README.md                          # This file
│
├── usb-exe-blocker/                   # USB executable blocking tool
│   ├── README.md                      # Setup and usage instructions
│   ├── blocker.py                     # Main blocking script
│   ├── install.bat                    # Installation script
│   └── uninstall.bat                  # Removal script
│
└── usb-security-test/                 # USB security awareness test
    ├── README.md                      # Complete setup guide
    ├── security_test.py               # Main test program
    ├── read_logs.py                   # Log analysis tool
    ├── build.py                       # Build automation
    └── check_usb.bat                  # Quick log checker
```

## 🔄 Complementary Usage Strategy

These tools work best when used together as part of a comprehensive USB security program:

### Phase 1: Baseline Assessment (Week 1-2)
1. Deploy **USB Security Awareness Test** to measure current awareness levels
2. Identify high-risk users and departments
3. Collect baseline metrics

### Phase 2: Training (Week 3-4)
1. Provide targeted training to those who failed the test
2. Share results and best practices organization-wide
3. Educate on USB security threats

### Phase 3: Enforcement (Week 5+)
1. Deploy **USB Exe Blocker** on endpoints
2. Monitor for blocked attempts
3. Provide ongoing training as needed

### Phase 4: Continuous Improvement (Quarterly)
1. Run periodic **USB Security Awareness Tests**
2. Measure improvement over time
3. Adjust **USB Exe Blocker** policies as needed
4. Update training materials

## 🎓 Best Practices

### Before Deployment

- [ ] Get written authorization from management
- [ ] Coordinate with HR, Legal, and Security teams
- [ ] Review and update security policies
- [ ] Plan communication strategy
- [ ] Prepare training materials
- [ ] Test tools in isolated environment

### During Deployment

- [ ] Start with pilot group
- [ ] Monitor for issues
- [ ] Collect feedback
- [ ] Document exceptions and edge cases
- [ ] Maintain communication channels

### After Deployment

- [ ] Analyze results and metrics
- [ ] Provide follow-up training
- [ ] Recognize good security behavior
- [ ] Document lessons learned
- [ ] Plan next phase

## 📊 Metrics to Track

### For USB Exe Blocker
- Number of blocked execution attempts
- Most common blocked file types
- Repeat offenders
- Legitimate exceptions requiring policy updates

### For USB Security Awareness Test
- Initial failure rate
- Improvement over time
- Department-by-department breakdown
- Training completion rates
- Number of reported suspicious USBs

## ⚖️ Legal & Ethical Considerations

### Required Authorizations

Before using either tool:

1. **Written authorization** from senior management
2. **Legal review** of your security testing program
3. **HR coordination** for employee testing
4. **Privacy compliance** with local/regional laws (GDPR, etc.)
5. **Union notification** if applicable
6. **Policy documentation** in employee handbook

### Ethical Guidelines

- **Transparency**: Eventually inform employees this is a test
- **Education**: Focus on learning, not punishment
- **Privacy**: Protect collected data appropriately
- **Fairness**: Apply policies consistently
- **Support**: Provide resources for improvement
- **Recognition**: Reward good security behavior

## 🔒 Security Considerations

### Data Protection

- Store logs securely with access controls
- Encrypt sensitive information
- Follow data retention policies
- Limit access to authorized personnel only
- Implement audit logging

### Testing Environment

- Test in isolated environment first
- Verify on multiple Windows versions
- Check compatibility with security software
- Document system requirements
- Plan rollback procedures

## 🆘 Troubleshooting

### Common Issues

**Issue:** Tools conflict with antivirus software  
**Solution:** Whitelist executables or code-sign them

**Issue:** Group Policy conflicts  
**Solution:** Review and align with existing policies

**Issue:** Users need legitimate exceptions  
**Solution:** Document exception process in advance

**Issue:** Logs contain sensitive data  
**Solution:** Review data handling procedures with legal/privacy teams

## 📚 Additional Resources

### USB Security Best Practices
- NIST SP 800-124: Guidelines for Managing USB Devices
- SANS USB Security Checklist
- CISA USB Security Guidance

### Security Awareness Training
- NIST Cybersecurity Framework
- SANS Security Awareness Roadmap
- KnowBe4 USB Security Training

### Incident Response
- NIST SP 800-61: Computer Security Incident Handling Guide
- SANS Incident Response Process

## 🤝 Contributing

This is an internal IT security toolkit. If you have improvements or suggestions:

1. Test thoroughly in isolated environment
2. Document changes clearly
3. Follow security review process
4. Update relevant README files
5. Coordinate with IT Security team

## 📝 License

**Internal Use Only**

These tools are designed for authorized internal security testing and enforcement within your organization. Ensure you have proper authorization before deployment.

## 📞 Support

### Internal Support Contacts

- **IT Security Team**: security@yourcompany.com
- **Help Desk**: helpdesk@yourcompany.com
- **Emergency Security**: security-emergency@yourcompany.com

### Documentation

- USB Exe Blocker: See `./usb-exe-blocker/README.md`
- USB Security Test: See `./usb-security-test/README.md`

## 🗺️ Roadmap

### Planned Enhancements

- [ ] PowerShell version of USB Exe Blocker
- [ ] Centralized logging dashboard
- [ ] Automated reporting tools
- [ ] Integration with SIEM systems
- [ ] Multi-language support
- [ ] macOS and Linux versions
- [ ] Email notification system
- [ ] Advanced analytics and trends

## 📋 Version History

### Version 1.0.0 (Current)
- Initial release
- USB Exe Blocker basic functionality
- USB Security Awareness Test with logging
- Complete documentation

---

## 🎯 Quick Decision Guide

**Choose USB Exe Blocker if you want to:**
- ✅ Block all USB executables automatically
- ✅ Enforce security policy technically
- ✅ Prevent malware execution
- ✅ Implement permanent controls

**Choose USB Security Test if you want to:**
- ✅ Test employee awareness
- ✅ Provide security training
- ✅ Measure security culture
- ✅ Identify training needs

**Use Both if you want to:**
- ✅ Comprehensive USB security program
- ✅ Education + enforcement approach
- ✅ Measurable security improvement
- ✅ Defense in depth strategy

---

## 🚦 Getting Started

1. **Read this overview** ✅ (You are here!)
2. **Choose your tool:**
   - Enforcement → [USB Exe Blocker](./usb-exe-blocker/README.md)
   - Education → [USB Security Test](./usb-security-test/README.md)
3. **Get authorization** from management
4. **Review tool-specific README** for detailed instructions
5. **Test in isolated environment** before deployment
6. **Deploy and monitor** according to best practices
7. **Measure and improve** continuously

---

**Questions?** Contact your IT Security team.

**Remember:** USB security is everyone's responsibility. Technology + Training = Strong Security Posture 🔒
