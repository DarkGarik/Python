#!/usr/bin/env python3
import socket, time

domains = ("drive.google.com", "mail.google.com", "google.com")
resolv = dict.fromkeys(domains)

for domain in domains:
    ip = socket.gethostbyname(domain)
    resolv[domain] = ip

while 1==1:
    for domain in domains:
        ip = socket.gethostbyname(domain)
        if ip == resolv[domain]:
            print(domain+" - "+ip)
        else:
            print("[ERROR] "+domain+" IP mismatch:"+resolv[domain]+" "+ip)
            print(domain+" - "+ip)
            resolv[domain] = ip
        time.sleep(1)
    