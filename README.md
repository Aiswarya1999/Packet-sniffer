# 🛡️ Network Attack Detection using Python & Wireshark

This project is designed to detect network-based attacks targeting the host computer using Python and `tshark` (the command-line version of Wireshark). It simulates attacks using a Linux Virtual Machine (VM) hosted in Oracle VirtualBox, providing a safe environment to test detection capabilities.

---

## 📌 Project Overview

**Goal:**  
Monitor the host Windows network interface for potential cyberattacks (e.g., SYN floods, port scans) using real-time packet analysis. The system reports:
- Type of attack
- Attacker's IP address
- Timestamp of the incident

**Key Tools:**
- `Python` for scripting and automation
- `tshark` (part of Wireshark) for packet capture and filtering
- `VirtualBox` with a Linux VM (used to simulate attacks)
- `nmap`, `hping3` on Linux VM for attack generation

---

## 🖥️ System Setup

### 1. Host Machine (Windows)
- **Install**:  
  - [Python](https://www.python.org/downloads/)
  - [Wireshark](https://www.wireshark.org/download.html) (ensure `tshark` is added to PATH)
  - [Visual Studio Code](https://code.visualstudio.com/) (for editing)

- **Check tshark installation:**
  ```bash
  tshark -v
