# Day 2: Hunter Grid — Automated Attack Surface Mapping

## OPSEC/Anonymity Notes
- All scans were performed via Tor proxychains for maximum anonymity.
- Tor exit IP: 192.42.116.197 (confirmed with api.ipify.org)
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

All other ports: Filtered (no response)
Note: The target is protected by Akamai CDN proxy. No backend systems directly exposed.

---

### 2. WhatWeb Results


http://example.com [200 OK]
HTTPServer[AkamaiGHost], AkamaiGHost CDN proxy detected.
No backend technologies or frameworks revealed at edge.

---

### 3. Nikto Results


Target web server is behind AkamaiGHost proxy.

No CGI directories or common vulnerabilities detected.

Security headers may be set by CDN. No application-level findings at this edge.


---

### 4. Attack Surface Table

| Port | Service  | Version                    | Web Techs       | Notes                  |
|------|----------|----------------------------|-----------------|------------------------|
| 80   | http     | AkamaiGHost CDN/Proxy      | (CDN edge only) | Behind Akamai proxy    |
| 443  | https    | AkamaiGHost CDN/Proxy      | (CDN edge only) | Behind Akamai proxy    |

---

### 5. Summary & Next Steps

**Findings:**  
- The target is fully protected by Akamai’s CDN/proxy service.
- No direct exposure of backend infrastructure, web frameworks, or vulnerable services.
- All non-essential ports are filtered or closed.

**Attacker Perspective:**  
- Very limited attack surface due to robust CDN protection.
- Next steps would focus on passive recon, subdomain enumeration, DNS history research, or searching for historical origin IP leaks.
- Social engineering or supply chain attacks might be explored if technical avenues are blocked.

**Defender Recommendations:**
- Continue to use and regularly update CDN security features.
- Monitor Akamai/CDN logs for unusual or suspicious access patterns.
- Routinely audit DNS records and ensure backend/origin IPs remain hidden.
- Implement strict WAF (Web Application Firewall) rules and bot protections at the CDN level.
- Enforce the principle of least privilege on backend systems and ensure they are not accessible from the public internet.
- Regularly scan for misconfigurations and unintended information exposure.

---

### 6. Visual Diagram
[⚠️ Suspicious Content] [Internet User]
|
[ Akamai CDN Edge ]
|
[ ??? ] (Origin IP/Backend: Hidden)

---

### 7. Reflection

- **Day 2 demonstrates:**  
  - The effectiveness of CDN protection in reducing a public attack surface.
  - The necessity of automated tools and strict OPSEC for modern reconnaissance.
  - The importance of ongoing vigilance—security is not a one-time fix, but a process of constant monitoring and improvement.

---

**All activities and findings were performed in a controlled, ethical, and legal environment for educational purposes only.**

