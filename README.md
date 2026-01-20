# 🔌 EPON OLT VLAN Automation Script

![Language](https://img.shields.io/badge/Language-Python%203-blue)
![Hardware](https://img.shields.io/badge/Hardware-V--SOL%20%7C%20BDCOM-orange)
![Network](https://img.shields.io/badge/Network-FTTH%20GPON%2FEPON-green)

## 📖 Overview
Configuring VLANs manually on an OLT (Optical Line Terminal) command line is tedious and error-prone. One wrong command can disconnect hundreds of FTTH clients.

This repository contains a **Python Automation Tool** designed for Network Engineers. It connects to the OLT via Telnet, automatically creates VLANs, assigns them to PON ports, and tags the Uplink port.

## 🛠 Features
- ⚡ **Bulk Configuration:** Configure 8 or 16 PON ports in seconds.
- 🏷️ **Auto-Tagging:** Automatically tags VLANs to the GE Uplink port.
- 🔒 **Safe Mode:** Validates login credentials before executing commands.
- 📝 **Log Generation:** Saves the configuration log for auditing.

## ⚙️ Supported Hardware
- **V-SOL** (V1600 Series)
- **BDCOM** (P3600 Series)
- **C-Data** (Generic EPON)

## 🚀 Usage Guide

### Step 1: Install Python & Libraries
Ensure you have Python installed. You may need `telnetlib` (standard in older Python) or install dependencies manually.

### Step 2: Configure the Script
Edit `olt_config.py` to set your OLT IP and Credentials:
```python
HOST = "192.168.8.100"
user = "admin"
password = "password"

Step 3: Run the Script
python3 olt_config.py

⚠️ Warning
This script modifies core network configurations. Do not run this on a live production OLT without testing in a lab environment first.
Author: Sheikh Alamin Santo
Cloud Infrastructure Specialist & Network Engineer
