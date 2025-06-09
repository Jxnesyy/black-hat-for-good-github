#!/usr/bin/env python3
"""
Recon Ghost — Black Hat for Good Day 1
Automates recon: WHOIS, DNS, GitHub dorking.
"""

import os

target = input("Enter target domain (e.g. example.com): ")

print("\n[WHOIS Lookup]")
os.system(f"whois {target}")

print("\n[DNS Lookup]")
os.system(f"nslookup {target}")

print("\n[GitHub Dorking]")
query = input("Enter a GitHub search query (e.g. password repo:{target}): ")
os.system(f'xdg-open "https://github.com/search?q={query}"')

print("\n[Basic OSINT Google]")
os.system(f'xdg-open "https://www.google.com/search?q={target}+filetype:txt+password"')

print("\nRecon complete. Document findings in GHOST_RECON.md.")
