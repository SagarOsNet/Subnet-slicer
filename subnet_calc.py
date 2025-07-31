# subnet_calc.py 🚀
def cidr_to_netmask(cidr):
    bits = 0xffffffff ^ (1 << 32 - cidr) - 1
    return f"{(bits >> 24) & 255}.{(bits >> 16) & 255}.{(bits >> 8) & 255}.{bits & 255}"

def main():
    ip = "192.168.50.0"
    cidr = 29
    subnet_mask = cidr_to_netmask(cidr)

    block_size = 2 ** (32 - cidr)
    total_hosts = block_size
    usable_hosts = block_size - 2
    network_address = ip
    broadcast_address = "192.168.50.7"
    usable_range = ("192.168.50.1", "192.168.50.6")

    print(f"IP Address       : {ip}")
    print(f"CIDR Notation    : /{cidr}")
    print(f"Subnet Mask      : {subnet_mask}")
    print(f"Block Size       : {block_size}")
    print(f"Network Address  : {network_address}")
    print(f"Broadcast Address: {broadcast_address}")
    print(f"Usable Range     : {usable_range[0]} - {usable_range[1]}")
    print(f"Total Hosts      : {total_hosts}")
    print(f"Usable Hosts     : {usable_hosts}")

if __name__ == "__main__":
    main()
