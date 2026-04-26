#!/bin/bash
# Example recon script: Quick Nmap scan + service enumeration
TARGET=$1

if [ -z "$TARGET" ]; then
echo "Usage: $0 <target-ip>"
exit 1
fi

echo "[+] Scanning $TARGET for open ports and services..."
nmap -sV -O -T4 $TARGET
