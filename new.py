#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import socket
import platform
import getpass
from datetime import datetime

def show_banner():
    # ================== COLORS ==================
    RED     = "\033[91m"
    DARKRED = "\033[31m"
    CYAN    = "\033[96m"
    GRAY    = "\033[90m"
    WHITE   = "\033[97m"
    BOLD    = "\033[1m"
    RESET   = "\033[0m"

    # ================== METADATA ==================
    AUTHOR = "Ahmar Wajahat"
    ROLE = "Ethical Hacker | Cyber Security Student"
    CREATED_ON = "2026-02-28"
    PLATFORM_NAME = "Kali Linux"

    # ================== SYSTEM INFO ==================
    user = getpass.getuser()
    hostname = socket.gethostname()
    kernel = platform.system() + " " + platform.release()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        ip = socket.gethostbyname(hostname)
    except:
        ip = "N/A"

    access = "ROOT ACCESS" if os.geteuid() == 0 else "USER MODE"

    # ================== CLEAR ==================
    os.system("clear")

    # ================== INTRO ==================
    intro = [
        "Initializing secure environment...",
        "Loading modules...",
        "Verifying permissions...",
        "Preparing interface..."
    ]

    print(f"{DARKRED}{BOLD}")
    for line in intro:
        print(f"[•] {line}")
        time.sleep(0.25)

    print(f"\n[✓] Environment Ready{RESET}")
    time.sleep(0.6)
    os.system("clear")

    # ================== BANNER ==================
    banner = f"""
{RED}{BOLD}
 █████╗ ██╗  ██╗███╗   ███╗ █████╗ ██████╗
██╔══██╗██║  ██║████╗ ████║██╔══██╗██╔══██╗
███████║███████║██╔████╔██║███████║██████╔╝
██╔══██║██╔══██║██║╚██╔╝██║██╔══██║██╔══██╗
██║  ██║██║  ██║██║ ╚═╝ ██║██║  ██║██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
{RESET}
"""

    print(banner)

    print(f"{GRAY}════════════════════════════════════════════════════════════{RESET}")
    print(f"{DARKRED}{BOLD}        AHMAR :: CYBER SECURITY PORTFOLIO MODE{RESET}")
    print(f"{GRAY}════════════════════════════════════════════════════════════{RESET}\n")

    print(f"{WHITE}{BOLD} Author        : {RESET}{AUTHOR}")
    print(f"{WHITE}{BOLD} Role          : {RESET}{ROLE}")
    print(f"{WHITE}{BOLD} Created On    : {RESET}{CREATED_ON}")
    print(f"{WHITE}{BOLD} Platform      : {RESET}{PLATFORM_NAME}\n")

    print(f"{CYAN}{BOLD} Session Info{RESET}")
    print(f"{CYAN} ├─ User        : {user}@{hostname}{RESET}")
    print(f"{CYAN} ├─ Access      : {access}{RESET}")
    print(f"{CYAN} ├─ IP Address  : {ip}{RESET}")
    print(f"{CYAN} ├─ Kernel      : {kernel}{RESET}")
    print(f"{CYAN} └─ Time        : {current_time}{RESET}")

    print(f"\n{GRAY}════════════════════════════════════════════════════════════{RESET}")
    print(f"{DARKRED}{BOLD}“Power without discipline is chaos.”{RESET}")
    print(f"{GRAY}════════════════════════════════════════════════════════════{RESET}\n")