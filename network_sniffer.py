from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from colorama import init, Fore
from string import printable

# Initialize colorama
init(autoreset=True)

# Colors
RED = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
YELLOW = Fore.YELLOW

def get_protocol_name(packet):
    if packet.haslayer(TCP):
        return "TCP", RED
    elif packet.haslayer(UDP):
        return "UDP", BLUE
    elif packet.haslayer(ICMP):
        return "ICMP", GREEN
    else:
        return "Other", YELLOW

def is_readable(text):
    """Check if payload contains mostly printable characters"""
    return all(c in printable for c in text)

def packet_callback(packet):
    if not packet.haslayer(IP):
        return

    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    protocol, color = get_protocol_name(packet)

    sport = dport = "N/A"

    if packet.haslayer(TCP):
        sport = packet[TCP].sport
        dport = packet[TCP].dport
    elif packet.haslayer(UDP):
        sport = packet[UDP].sport
        dport = packet[UDP].dport

    print(f"{color}[*] {src_ip}:{sport} --> {dst_ip}:{dport} | Protocol: {protocol}")

    # Payload handling (safe)
    if packet.haslayer('Raw'):
        raw_data = packet['Raw'].load
        try:
            decoded = raw_data.decode('utf-8')
            if decoded and is_readable(decoded):
                print(f"    {YELLOW}Payload: {decoded[:80]}")
        except:
            pass

def start_sniffer():
    print(f"{GREEN}Starting Network Sniffer...")
    print(f"{GREEN}Press Ctrl+C to stop.\n")
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    start_sniffer()
