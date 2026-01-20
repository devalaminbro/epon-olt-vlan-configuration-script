```python
import telnetlib
import time

# ============================================================
# EPON OLT VLAN Automation Tool
# Author: Sheikh Alamin Santo
# Description: Automates VLAN creation on V-SOL/BDCOM OLTs
# ============================================================

# --- Configuration ---
HOST = "192.168.8.100"  # OLT IP Address
USER = "admin"          # OLT Username
PASSWORD = "password"   # OLT Password
UPLINK_PORT = "GE1"     # Uplink Port Name

# VLAN Range to Create (e.g., VLAN 101 to 108 for 8 PON ports)
VLAN_START = 101
PON_PORTS = 8 

def configure_olt():
    try:
        print(f"[+] Connecting to OLT at {HOST}...")
        tn = telnetlib.Telnet(HOST, timeout=10)

        # Login Process
        tn.read_until(b"Login: ")
        tn.write(USER.encode('ascii') + b"\n")
        
        tn.read_until(b"Password: ")
        tn.write(PASSWORD.encode('ascii') + b"\n")
        
        print("[+] Login Successful. Starting Configuration...")
        
        # Enter Enable / Config Mode
        tn.write(b"enable\n")
        tn.write(b"config\n")
        
        # Loop to create VLANs and Assign to PON Ports
        for i in range(PON_PORTS):
            vlan_id = VLAN_START + i
            pon_id = i + 1
            
            print(f"    - Configuring VLAN {vlan_id} for PON {pon_id}...")
            
            # Commands for V-SOL/BDCOM (Standard CLI)
            cmd_create_vlan = f"vlan {vlan_id}\n"
            cmd_name_vlan = f"name PON_{pon_id}_Client\n"
            cmd_exit = "exit\n"
            
            tn.write(cmd_create_vlan.encode('ascii'))
            tn.write(cmd_name_vlan.encode('ascii'))
            tn.write(cmd_exit.encode('ascii'))
            
            # Tag VLAN to Uplink
            cmd_uplink = f"interface {UPLINK_PORT}\n"
            cmd_tag = f"switchport trunk allowed vlan add {vlan_id}\n"
            
            tn.write(cmd_uplink.encode('ascii'))
            tn.write(cmd_tag.encode('ascii'))
            tn.write(cmd_exit.encode('ascii'))
            
            time.sleep(0.5) # Wait for OLT to process

        # Save Configuration
        print("[+] Saving Configuration...")
        tn.write(b"write all\n")
        tn.write(b"exit\n")
        
        print(tn.read_all().decode('ascii'))
        print("[+] OLT Configuration Completed Successfully!")

    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    configure_olt()
