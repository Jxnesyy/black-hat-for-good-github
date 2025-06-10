#!/usr/bin/env python3
import socket

def check_ftp_backdoor(ip, port=21):
    s = socket.socket()
    s.settimeout(3)
    try:
        s.connect((ip, port))
        banner = s.recv(1024).decode()
        if "vsFTPd 2.3.4" in banner:
            print(f"[!] {ip}:{port} appears vulnerable to vsFTPd 2.3.4 backdoor (CVE-2011-2523)")
        else:
            print(f"[+] {ip}:{port} FTP banner: {banner.strip()}")
    except Exception as e:
        print(f"[-] Could not connect to {ip}:{port}: {e}")
    s.close()

if __name__ == "__main__":
    target = input("Enter target IP: ")
    check_ftp_backdoor(target)
