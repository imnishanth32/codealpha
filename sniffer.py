from scapy.all import sniff, IP, TCP, UDP, ICMP

def analyze_packet(packet):
    print("\n--- Packet Captured ---")

    # Check if packet has IP layer
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        print(f"Source IP      : {ip_layer.src}")
        print(f"Destination IP : {ip_layer.dst}")
        print(f"Protocol       : {ip_layer.proto}")

        # TCP
        if packet.haslayer(TCP):
            tcp_layer = packet[TCP]
            print("Protocol Name  : TCP")
            print(f"Source Port    : {tcp_layer.sport}")
            print(f"Destination Port: {tcp_layer.dport}")

        # UDP
        elif packet.haslayer(UDP):
            udp_layer = packet[UDP]
            print("Protocol Name  : UDP")
            print(f"Source Port    : {udp_layer.sport}")
            print(f"Destination Port: {udp_layer.dport}")

        # ICMP
        elif packet.haslayer(ICMP):
            print("Protocol Name  : ICMP")

        # Payload
        if packet.payload:
            raw_data = bytes(packet.payload)
            print(f"Payload (raw)  : {raw_data[:50]}")  # first 50 bytes

def main():
    print("Starting packet capture... Press Ctrl+C to stop.")
    sniff(prn=analyze_packet, store=False)

if __name__ == "__main__":
    main()
