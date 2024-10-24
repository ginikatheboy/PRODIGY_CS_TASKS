from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

# Function to handle each of the packet
def process_packet(packet):
    # Checking if it has an IP layer
    if packet.haslayer(IP):
        ip_layer = packet[IP]

        # Extracting the source and destination IP addresses
        source_ip = ip_layer.src
        destination_ip = ip_layer.dst

        # Checking for protocol type
        if packet.haslayer(TCP):
            protocol = "TCP"
        elif packet.haslayer(UDP):
            protocol = "UDP"
        elif packet.haslayer(ICMP):
            protocol = "ICMP"
        else:
            protocol = "other"

        # Code to print the packet info
        print(f"Source: {source_ip} -> Destination: {destination_ip} | Protocol: {protocol}")

        # To captrue and print the payload data
        payload_data =bytes(packet[IP].payload)
        print(f"Payload: {payload_data}")

# To start sniffing packets
sniff(prn=process_packet, count=5)
