#!/bin/bash
echo "===== Phantom Defend: SSH Brute-Force Detection ====="
LOG=${1:-/var/log/auth.log}
echo "Scanning $LOG for brute-force attempts..."
grep "Failed password" $LOG | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr | head
echo "Done."
