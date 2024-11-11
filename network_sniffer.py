import scapy.all as scapy

def sniff_packets(interface, count):
    scapy.conf.verb = 0  # Disable verbose mode for cleaner output
    packets = scapy.sniff(iface=interface, count=count)
    return packets

def print_packet_info(packet):
    print("Packet Info:")
    if packet.haslayer(scapy.IP):
        print(f"  Source IP: {packet[scapy.IP].src}")
        print(f"  Destination IP: {packet[scapy.IP].dst}")
    if packet.haslayer(scapy.Ether):
        print(f"  Destination MAC: {packet[scapy.Ether].dst}")
    if packet.haslayer(scapy.TCP):
        print(f"  Source Port: {packet[scapy.TCP].sport}")
        print(f"  Destination Port: {packet[scapy.TCP].dport}")
    print(f"  Length: {len(packet)} bytes")

def print_http_info(packet):
    if packet.haslayer(scapy.TCP) and packet.haslayer(scapy.IP):
        src_port = packet[scapy.TCP].sport
        dst_port = packet[scapy.TCP].dport
        if src_port == 80 or dst_port == 80:  # Checks for HTTP traffic
            print("HTTP Packet:")
            if packet.haslayer(scapy.Raw):
                http_data = packet[scapy.Raw].load
                if b"GET" in http_data or b"POST" in http_data:
                    print("  HTTP Request:")
                    print(f"    {http_data.decode('utf-8', 'ignore')}")

def main():
    interface = "eth0"  # Change to your network interface
    count = 25
    packets = sniff_packets(interface, count)
    for packet in packets:
        print_packet_info(packet)
        print_http_info(packet)
        print()  # Print a blank line for readability

if __name__ == "__main__":
    main()

