import ipaddress

def get_ip_class(ip):
    first_octet = int(str(ip).split('.')[0])
    if 1 <= first_octet <= 126:
        return "Class A"
    elif 128 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D (Multicast)"
    elif 240 <= first_octet <= 255:
        return "Class E (Experimental)"
    else:
        return "Unknown"

def to_binary(ip):
    return '.'.join([format(int(octet), '08b') for octet in ip.split('.')])

def analyze_ip(ip_str):
    try:
        ip = ipaddress.ip_address(ip_str)

        print(f"\n📍 IP Address     : {ip}")
        print(f"🔢 Version        : IPv{ip.version}")
        print(f"🧠 Binary         : {to_binary(ip_str)}")
        print(f"📎 Class          : {get_ip_class(ip)}")
        print(f"🔒 Private        : {'Yes' if ip.is_private else 'No'}")
        print(f"🌀 Loopback       : {'Yes' if ip.is_loopback else 'No'}")
        print(f"🚫 Multicast      : {'Yes' if ip.is_multicast else 'No'}")
        print(f"📛 Reserved       : {'Yes' if ip.is_reserved else 'No'}\n")

    except ValueError:
        print("\n❌ Invalid IP address.\n")

# 🧪 Run loop
while True:
    ip_input = input("Enter an IP address (or type 'exit'): ")
    if ip_input.lower() == "exit":
        break
    analyze_ip(ip_input)
