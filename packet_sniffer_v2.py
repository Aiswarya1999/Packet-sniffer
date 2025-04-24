import pyshark
from datetime import datetime
from collections import defaultdict

# Use your Wi-Fi interface
INTERFACE = r'\Device\NPF_{40463D53-799E-4508-8DEB-50DDFEE7205F}'

# Keep count of SYN packets per source IP
syn_counts = defaultdict(int)
THRESHOLD = 10  # Adjust as needed

print(f"[*] Starting capture on: {INTERFACE}")

# Live capture with filter: TCP packets with SYN flag set
capture = pyshark.LiveCapture(interface=INTERFACE, display_filter='tcp.flags.syn == 1')

for packet in capture.sniff_continuously():
    try:
        src_ip = packet.ip.src
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        syn_counts[src_ip] += 1
        count = syn_counts[src_ip]

        if count > THRESHOLD:
            print(f"[{timestamp}] ⚠️ SYN flood alert! Source IP: {src_ip} | Count: {count}")
        else:
            print(f"[{timestamp}] SYN from {src_ip} (count: {count})")

    except AttributeError:
        # Some packets may not have IP layer — skip them
        continue
