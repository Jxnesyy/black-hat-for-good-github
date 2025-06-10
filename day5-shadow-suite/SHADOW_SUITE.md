# Day 5: Shadow Suite — Black Hat Techniques for Good

## OPSEC/Anonymity
- MAC randomized before scans.
- All scans via proxychains+Tor (where possible).
- Tool logs and bash history cleared after use.

---

## 1. Secret Reconnaissance (`shadow_recon.py`)
- **Domain searched:** [example.com]
- **Hunter.io results:** [e.g., No emails found, or list]
- **HaveIBeenPwned:** [e.g., No breach, or “breached!”]
- **Metadata exfil:** [e.g., GPS/Author info found in test.jpg]

---

## 2. Stealth Automation & Attack (`shadow_attack.sh`)
- **Target:** 192.168.0.80
- **MAC randomized:** ✔️
- **Nmap results:** [paste key output—open ports/services found, or “all filtered”]
- **Masscan:** [summary of discovered ports]
- **DNS tunneling:** [ran/not ran, result]
- **Slowloris:** [ran, error, or skipped]
- **Insights:** Chained tools for multi-layered stealth attack; OPSEC best practices.

---

## 3. Black Hat Defensive Ops (`shadow_defend.sh`)
- **SUID/rootkit scan:** [list or summary]
- **Log diffing:** [show new logins or none]
- **Cron job review:** [suspicious jobs?]
- **Incident response:** [shells killed, or clean]
- **Key output files:** `suid_report.txt`, `chkrootkit_report.txt`, etc.

---

## 4. Dashboard & Reflection

### **Screenshots**
- (Paste or link output screenshots here—terminal, code, report files.)

### **Lessons Learned**
- How real adversaries chain tools and evade detection.
- OPSEC isn’t optional—automation is key.
- Blue team wins by regularly hunting, not just reacting.
- “If I knew this on Day 1: Automate, cloak, and always check for weirdness.”

### **Top Secret Tips for New Hackers**
- Always randomize what you can (MACs, user agents, scan timing).
- Never trust file metadata—exfil and monitor it.
- Rotate logs and diff for changes.
- Defensive scripting is as valuable as offense.
- Never run a tool you don’t understand—read the help, check the output.

---

**All scripts and findings are from a controlled lab for ethical research only.**
