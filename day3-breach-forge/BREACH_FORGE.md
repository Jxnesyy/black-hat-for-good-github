# Day 3: Breach Forge — Exploiting and Hardening Weaknesses

## OPSEC/Anonymity Notes

- All scans performed via Tor proxychains for maximum anonymity.
- Tor exit IP (checked via api.ipify.org): 192.42.116.197
- Date/time: 2025-06-10 (07:35)

---

## Target: (insert test target, e.g., metasploitable VM, allowed demo target)

---

### 1. Nmap Vulnerability Scan

 Nmap 7.95 scan initiated Tue Jun 10 07:36:21 2025 as: /usr/lib/nmap/nmap --privileged -sV --script vuln -T4 -oN nmap_vuln.txt example.com



---

### 2. Brute-Force Simulation (Optional/If Used)

Hydra ran a brute-force attack on the local FTP server (192.168.56.101).
Hydra was unable to brute-force the FTP server using the top 14 million passwords from rockyou.txt.
All attempts were denied. The server may be well-configured or test credentials may not be present.


---

### 3. Exploitation Attempt (Only Demo/Allowed)

(Describe safe proof-of-concept: e.g., login with weak creds, known test exploit, etc.)


---

### 4. Defender/Hardening Recommendations

- **Findings:**  
  - Summarize discovered weaknesses
- **Fixes:**  
  - Patch, strong passwords, disable weak services, monitor logs, etc.

---

### 5. Summary & Reflections

- What was learned about offensive and defensive security.
- Any scripts, tweaks, or customizations added.

---

