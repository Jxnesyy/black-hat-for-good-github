## OPSEC/Anonymity Notes

- Cloak activated using Tor and proxychains.
- Tor exit IP at session start: 185.220.101.42
- All recon performed through anonymized proxychains for maximum privacy.
- VPN option: Not available during this session. (Update this if/when you use a VPN instead.)


# Day 1: Recon Ghost Report

## Target Domain: example.com

---

### WHOIS Info
- **Domain Name:** EXAMPLE.COM
- **Created:** 1995-08-14
- **Registrar:** RESERVED-Internet Assigned Numbers Authority
- **Name Servers:**  
  - A.IANA-SERVERS.NET  
  - B.IANA-SERVERS.NET
- **Organisation:** Internet Assigned Numbers Authority

---

### DNS Info
- **IPv4 addresses:**
  - 96.7.128.198
  - 23.192.228.80
  - 23.192.228.84
  - 23.215.0.136
  - 23.215.0.138
  - 96.7.128.175
- **IPv6 addresses:**
  - 2600:1406:bc00:53::b81e:94ce
  - 2600:1408:ec00:36::1736:7f24
  - 2600:1408:ec00:36::1736:7f31
  - 2600:1406:3a00:21::173e:2e65
  - 2600:1406:3a00:21::173e:2e66
  - 2600:1406:bc00:53::b81e:94c8

---

### GitHub Dorking

- **Query Used:** `password example.com`
- **Results:**  
  - No sensitive information or passwords related to example.com were found in public GitHub repositories.  
  - Search results mostly included generic code examples, documentation, or reference material using "example.com" as a placeholder, which is standard practice.

---

### OSINT Findings

- **General Web Search:**  
  - No leaks, credentials, or sensitive data associated with example.com found in Google or other public sources.
  - The domain is widely used in tutorials, documentation, and as a safe example in public codebases.

---

## Summary / Insights

- Recon on example.com was safe and produced no private or real-world sensitive data.
- This demonstrates proper use of demo targets and validates good digital hygiene for reserved domains.
- Practicing recon on such domains is highly recommended for learning and workflow development.
- If this had been a real client domain, any sensitive findings would be documented for responsible disclosure.

---

**Screenshots / Logs:**  
- (Attach `recon_output.txt` or relevant screenshots here if available.)

