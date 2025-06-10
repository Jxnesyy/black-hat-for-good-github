#!/bin/bash
echo "===== Shadow Defend: Stealth Detection & Incident Response ====="

echo "[*] Searching for hidden SUIDs and rootkits..."
find / -perm -4000 -type f 2>/dev/null | grep -Ev "bin/(su|sudo|ping|mount|umount|passwd)" > suid_report.txt
chkrootkit > chkrootkit_report.txt 2>/dev/null

echo "[*] Log diffing for anomalies..."
diff /var/log/auth.log /var/log/auth.log.1 | grep "Accepted" > auth_diff.txt

echo "[*] Detecting suspicious new cron jobs..."
ls -al /etc/cron* /var/spool/cron/crontabs 2>/dev/null | grep -v root > cron_diff.txt

echo "[*] Live response: kill shells running from /tmp or suspicious dirs..."
ps aux | grep '/tmp' | grep -v grep | awk '{print $2}' | xargs -r sudo kill -9

echo "[*] Summarizing anomalies:"
cat suid_report.txt
cat chkrootkit_report.txt | grep -E "(INFECTED|Warning|Suspicious)"
cat auth_diff.txt
cat cron_diff.txt

echo "[*] Shadow Defend Complete."
