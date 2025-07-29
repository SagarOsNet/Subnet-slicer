# calc.py

import ipaddress
import sys

def subnet_info(ip_cidr):
    try:
        net = ipaddress.ip_network(ip_cidr, strict=False)
        hosts = list(net.hosts())
        print(f"\nIP Address:     {ip_cidr.split('/')[0]}")
        print(f"Subnet Mask:    {net.netmask}")
        print(f"Network:        {net.network_address}")
        print(f"Broadcast:      {net.broadcast_address}")
        print(f"Total Hosts:    {net.num_addresses}")
        if len(hosts) > 2:
            print(f"Usable Hosts:   {len(hosts)}")
            print(f"Usable Range:   {hosts[0]} – {hosts[-1]}")
        else:
            print("Usable Hosts:   N/A (Too small for usable range)")
    except Exception as e:
        print(f"\n[Error] Invalid input → {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python calc.py <IP/CIDR>")
    else:
        subnet_info(sys.argv[1])
