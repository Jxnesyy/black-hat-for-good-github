# Day 2: Hunter Grid — Elite Attack Surface Mapping

## OPSEC/Anonymity Notes
- All scans performed via Tor proxychains for maximum anonymity.
- Tor exit IP: (insert Tor IP from `ghost`)
- Date/time: 2025-06-10 00:52 BST

---

## Target: example.com

---

### 1. Nmap Results

Host: example.com (23.215.0.138)
Open Ports:

80/tcp http AkamaiGHost (Akamai's HTTP Acceleration/Mirror service)

443/tcp ssl/http AkamaiGHost (Akamai's HTTP Acceleration/Mirror service)
rDNS: a23-215-0-138.deploy.static.akamaitechnologies.com
Note: Only Akamai proxy services detected. Most other ports filtered (stealth mode or firewall).
---

### 2. WhatWeb Results
(Insert WhatWeb findings here. Usually this reveals if any web technologies are detected—if blank or only Akamai, it's likely a proxy/CDN edge.)

---

### 3. Nikto Results

(Insert Nikto findings here. For Akamai/CDN targets, Nikto usually finds little to nothing—this is normal for high-profile domains protected by a CDN.)


---

### 4. Attack Surface Table

| Port | Service  | Version                    | Web Techs (if any) | Notes                |
|------|----------|----------------------------|--------------------|----------------------|
| 80   | http     | AkamaiGHost (CDN/Proxy)    | (See WhatWeb)      | Behind Akamai proxy  |
| 443  | ssl/http | AkamaiGHost (CDN/Proxy)    | (See WhatWeb)      | Behind Akamai proxy  |

---

### 5. Summary & Next Steps

- **Key findings:**  
  - Target protected by Akamai CDN/proxy; direct enumeration of backend is blocked.
  - Only web ports (80, 443) open. All other ports filtered.
- **Attacker next steps:**  
  - Attempt web-based recon for exposed files, misconfigurations, or leaks via CDN edge.
  - Try passive recon (Google dorking, DNS history) to discover underlying origin infrastructure.
  - Enumerate for historical DNS records, subdomains, or possible unprotected endpoints.
- **Defender recommendations:**  
  - Continue hiding origin infrastructure behind CDN.
  - Monitor CDN logs for suspicious patterns.
  - Harden backend and ensure security of origin IPs and DNS records.

---

### 6. Visual Diagram

[ Internet ]
|
[ Akamai CDN Edge ]
|
[ ??? ]

*Backend origin not exposed—demonstrates high security posture.*
