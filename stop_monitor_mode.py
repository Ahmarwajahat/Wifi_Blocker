import subprocess

# Interface currently in monitor mode
MON_INTERFACE = "wlan0mon"

print(f"[*] Stopping monitor mode on {MON_INTERFACE}...")

try:
    subprocess.run(
        ["sudo", "airmon-ng", "stop", MON_INTERFACE],
        check=True
    )
    print(f"[+] Monitor mode disabled. {MON_INTERFACE} is back to managed mode.")
except subprocess.CalledProcessError:
    print("[-] Failed to stop monitor mode.")
    print("Make sure the interface exists and is in monitor mode.")