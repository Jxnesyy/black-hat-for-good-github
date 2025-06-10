#!/bin/bash
echo "===== Hunter Grid: Elite Attack Surface Mapping ====="
TARGET=$1

if [ -z "$TARGET" ]; then
    echo "Usage: $0 <target-domain>"
    exit 1
fi

echo "[*] Running Nmap (service and version detection)..."
proxychains nmap -sV -Pn -T4 -oN nmap_results.txt $TARGET

echo "[*] Running WhatWeb (web tech fingerprinting)..."
proxychains whatweb $TARGET > whatweb.txt

echo "[*] Running Nikto (web vuln scan)..."
proxychains nikto -host $TARGET > nikto.txt

echo "===== Scans Complete! Results in: nmap_results.txt, whatweb.txt, nikto.txt ====="
