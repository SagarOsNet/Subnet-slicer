import ipaddress

def classify_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        if ip_obj.is_private:
            scope = "Private"
        else:
            scope = "Public"

        if ip_obj.version == 4:
            version = "IPv4"
        else:
            version = "IPv6"

        print(f"IP Address   : {ip}")
        print(f"Version      : {version}")
        print(f"Scope        : {scope}")
    except ValueError:
        print("❌ Invalid IP address.")

# 👇 Test IP goes here
ip_input = "192.168.1.1"
classify_ip(ip_input)

