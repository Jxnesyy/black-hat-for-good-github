#!/usr/bin/env python3
import requests
import sys
import os
import json
import re

def hunter_email_enum(domain):
    print(f"\n[+] Querying Hunter.io for emails at: {domain}")
    HUNTER_API = os.getenv('HUNTER_API_KEY')  # Export your API key to HUNTER_API_KEY
    if not HUNTER_API:
        print("  [-] No Hunter.io API key set (export HUNTER_API_KEY=yourkey). Skipping...")
        return
    url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={HUNTER_API}"
    resp = requests.get(url)
    try:
        data = resp.json()
        emails = data.get("data", {}).get("emails", [])
        for e in emails:
            print(f"    - {e['value']} (type: {e['type']})")
        if not emails:
            print("    - No emails found.")
    except Exception as ex:
        print("  [-] API error:", ex)

def hibp_pwned_check(email):
    print(f"\n[+] Checking HaveIBeenPwned for: {email}")
    headers = {'User-Agent': 'ShadowSuite'}
    url = f"https://haveibeenpwned.com/unifiedsearch/{email}"
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200 and "No breached accounts" not in resp.text:
        print("    - This email appears in at least one breach!")
    else:
        print("    - No breaches found or limited API.")

def exif_scan(filename):
    print(f"\n[+] Extracting metadata from: {filename}")
    try:
        from subprocess import check_output
        out = check_output(['exiftool', filename]).decode()
        for line in out.strip().split('\n'):
            if re.search(r'(GPS|Location|Author|Creator|Software|Date|Time|Email)', line, re.I):
                print("    " + line.strip())
    except Exception as ex:
        print("  [-] exiftool not found or file error:", ex)

if __name__ == "__main__":
    print("===== Shadow Recon: Advanced OSINT & Metadata =====")
    target_domain = input("Enter domain (e.g., example.com): ")
    hunter_email_enum(target_domain)
    demo_email = f"admin@{target_domain}"
    hibp_pwned_check(demo_email)
    img = input("Path to image or PDF for metadata extraction (blank to skip): ")
    if img.strip():
        exif_scan(img)
    print("Recon complete.")
