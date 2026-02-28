#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import socket
import platform
import getpass
import sys
import random
from datetime import datetime

# ================== GLOBAL COLORS ==================
# Colors defined OUTSIDE the function so they are available everywhere
RED = "\033[91m"
DARK_RED = "\033[31m"
GREEN = "\033[92m"
DARK_GREEN = "\033[32m"
CYAN = "\033[96m"
DARK_CYAN = "\033[36m"
BLUE = "\033[94m"
DARK_BLUE = "\033[34m"
PURPLE = "\033[95m"
MAGENTA = "\033[35m"
YELLOW = "\033[93m"
BROWN = "\033[33m"
GRAY = "\033[90m"
LIGHT_GRAY = "\033[37m"
WHITE = "\033[97m"
BLACK = "\033[30m"

# Text Styles
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
REVERSE = "\033[7m"
DIM = "\033[2m"
RESET = "\033[0m"

# Cursor Control
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"
CLEAR_LINE = "\033[2K"
MOVE_UP = "\033[F"


def show_banner():
    # ================== METADATA ==================
    AUTHOR = "SIR AHMAR"  # Changed to SIR AHMAR only
    EMAIL = "ahmarwajhatawan@gmail.com"
    GITHUB = "github.com/Ahmarwajahat"
    LINKEDIN = "linkedin.com/in/ahmarwajahat"
    ROLE = "⦿ Ethical Hacker ⦿ Security Researcher ⦿ Red Teamer"
    CREATED_ON = "2026-02-28"
    PLATFORM = "Kali Linux 2025.4"
    VERSION = "2.5.0"

    # ================== SYSTEM INFO ==================
    user = getpass.getuser()
    hostname = socket.gethostname()
    kernel = platform.system() + " " + platform.release()
    architecture = platform.machine()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        ip = socket.gethostbyname(hostname)
    except:
        ip = "127.0.0.1"

    access = "⚡ ROOT ACCESS ⚡" if os.geteuid() == 0 else "⚠ USER MODE ⚠"

    # Get terminal size
    terminal_width = os.get_terminal_size().columns
    line = "═" * min(70, terminal_width - 10)

    print(HIDE_CURSOR, end="")
    os.system("clear")

    # ================== EPIC LOADING SEQUENCE ==================
    loading_frames = ["█", "▓", "▒", "░"]
    loading_messages = [
        "Bypassing firewall",
        "Spoofing MAC address",
        "Enabling monitor mode",
        "Loading modules",
        "Establishing secure channel"
    ]

    print(f"\n{DARK_CYAN}{BOLD}╔{line}╗{RESET}")
    print(f"{DARK_CYAN}{BOLD}║{RESET}{WHITE}{BOLD}              SYSTEM BOOT SEQUENCE INITIATED              {RESET}{DARK_CYAN}{BOLD}║{RESET}")
    print(f"{DARK_CYAN}{BOLD}╚{line}╝{RESET}\n")

    for i, msg in enumerate(loading_messages):
        for frame in loading_frames:
            print(f"{CYAN}[{frame}] {msg}...{RESET}", end="", flush=True)
            time.sleep(0.03)
            print(MOVE_UP + CLEAR_LINE, end="")
        print(f"{GREEN}[✓] {msg}... SUCCESS{RESET}")
        time.sleep(0.1)

    time.sleep(0.5)
    os.system("clear")

    # ================== HEADER WITH ASCII BORDER ==================
    header = f"""
{DARK_RED}{BOLD}╔══════════════════════════════════════════════════════════════════════════════╗
║{RESET}{WHITE}{BOLD}                 WIFI RECONNAISSANCE FRAMEWORK v1.0.0                 {DARK_RED}{BOLD}║
║{RESET}{YELLOW}{BOLD}            CYBER SECURITY • ETHICAL HACKING • EDUCATION           {DARK_RED}{BOLD}║
╚══════════════════════════════════════════════════════════════════════════════╝{RESET}
"""
    print(header)
    time.sleep(0.3)

    # ================== MAIN ASCII BANNER ==================
    banner = f"""
{RED}{BOLD}
    █████╗ ██╗  ██╗███╗   ███╗ █████╗ ██████╗  
   ██╔══██╗██║  ██║████╗ ████║██╔══██╗██╔══██╗   
   ███████║███████║██╔████╔██║███████║██████╔╝    
   ██╔══██║██╔══██║██║╚██╔╝██║██╔══██║██╔══██╗    
   ██║  ██║██║  ██║██║ ╚═╝ ██║██║  ██║██║  ██║    
   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝     
{RESET}"""

    # Print banner with slight delay for dramatic effect
    banner_lines = banner.split('\n')
    for line in banner_lines:
        if line.strip():
            print(f"{DARK_RED}{BOLD}{line}{RESET}")
            time.sleep(0.02)
        else:
            print()

    # ================== PROFILE HEADER ==================
    print(f"{MAGENTA}{BOLD}╔═══════════════════════[ PROFILE INFORMATION ]═══════════════════════╗{RESET}")

    print(f"{WHITE}{BOLD}┃  AUTHOR  {RESET}{GRAY}──────────────────────────────────────────────────{RESET}")
    print(f"{WHITE}  ▸ Name     : {CYAN}{BOLD}{AUTHOR}{RESET}")
    print(f"{WHITE}  ▸ Email    : {BLUE}{EMAIL}{RESET}")
    print(f"{WHITE}  ▸ GitHub   : {PURPLE}{GITHUB}{RESET}")
    print(f"{WHITE}  ▸ LinkedIn : {DARK_BLUE}{LINKEDIN}{RESET}")
    print(f"{WHITE}  ▸ Role     : {YELLOW}{ROLE}{RESET}")
    print(f"{WHITE}  ▸ Created  : {GREEN}{CREATED_ON}{RESET}")
    print(f"{WHITE}  ▸ Platform : {RED}{PLATFORM}{RESET}")
    print(f"{WHITE}  ▸ Version  : {MAGENTA}{VERSION}{RESET}")

    print(f"{MAGENTA}{BOLD}╚════════════════════════════════════════════════════════════════════╝{RESET}\n")

    # ================== SYSTEM HEADER ==================
    print(f"{GREEN}{BOLD}╔═══════════════════════[ SYSTEM STATUS ]════════════════════════╗{RESET}")

    # Format system info with proper alignment
    print(f"{GREEN}┃{RESET}  {WHITE}User     :{RESET} {YELLOW}{user}{RESET}{WHITE}@{RESET}{GREEN}{hostname}{RESET}")
    print(f"{GREEN}┃{RESET}  {WHITE}Access   :{RESET} {RED}{BOLD}{access}{RESET}")
    print(f"{GREEN}┃{RESET}  {WHITE}IP Addr  :{RESET} {CYAN}{ip}{RESET}")
    print(f"{GREEN}┃{RESET}  {WHITE}Kernel   :{RESET} {YELLOW}{kernel}{RESET}")
    print(f"{GREEN}┃{RESET}  {WHITE}Arch     :{RESET} {PURPLE}{architecture}{RESET}")
    print(f"{GREEN}┃{RESET}  {WHITE}Terminal :{RESET} {BLUE}{terminal_width} columns{RESET}")
    print(f"{GREEN}┃{RESET}  {WHITE}Time     :{RESET} {DARK_CYAN}{current_time}{RESET}")

    print(f"{GREEN}{BOLD}╚════════════════════════════════════════════════════════════════╝{RESET}\n")

    # ================== QUOTE SECTION ==================
    quotes = [
        ("Sun Tzu", "The Art of War", "Know your enemy and know yourself"),
        ("Kevin Mitnick", "Hacker", "The quieter you become, the more you are able to hear"),
        ("Bruce Schneier", "Security Expert", "Security is always excessive until it's not enough"),
        ("Anonymous", "Hacker Mantra", "Leave it better than you found it"),
        ("Voltaire", "Philosopher", "With great power comes great responsibility")
    ]

    quote_author, quote_source, quote_text = random.choice(quotes)

    print(f"{YELLOW}{BOLD}╔═══════════════════════[ WISDOM OF THE DAY ]══════════════════════╗{RESET}")
    print(f"{YELLOW}║{RESET}  {WHITE}{BOLD}\"{quote_text}\"{RESET}")
    print(f"{YELLOW}║{RESET}  {CYAN}— {quote_author} ({quote_source}){RESET}")
    print(f"{YELLOW}{BOLD}╚════════════════════════════════════════════════════════════════╝{RESET}\n")

    # ================== ETHICAL HEADER ==================
    print(f"{RED}{BOLD}╔═══════════════════════[ LEGAL DISCLAIMER ]════════════════════════╗{RESET}")
    print(f"{RED}║{RESET}  {WHITE}{BOLD}⚠  STRICT ETHICAL USE ONLY - AUTHORIZED TESTING REQUIRED{RESET}")
    print(f"{RED}║{RESET}  {GRAY}▸ Use only on networks you OWN or have WRITTEN PERMISSION{RESET}")
    print(f"{RED}║{RESET}  {GRAY}▸ Unauthorized access is ILLEGAL - You are responsible{RESET}")
    print(f"{RED}║{RESET}  {GRAY}▸ Educational purposes ONLY - Not for malicious use{RESET}")
    print(f"{RED}{BOLD}╚════════════════════════════════════════════════════════════════════╝{RESET}\n")

    # ================== READY PROMPT WITH STYLE ==================
    print(f"{GREEN}{BOLD}╔════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{GREEN}{BOLD}║{RESET}{GREEN}{BOLD}                    ⚡ SYSTEM READY ⚡                     {GREEN}{BOLD}║{RESET}")
    print(f"{GREEN}{BOLD}╚════════════════════════════════════════════════════════════════╝{RESET}\n")

    # Cool prompt with colors
    print(f"{DARK_CYAN}┌─[{RED}{BOLD}✓{RESET}{DARK_CYAN}]─[{YELLOW}{BOLD}READY{RESET}{DARK_CYAN}]─[{GREEN}{BOLD}{user}{RESET}{WHITE}@{RESET}{GREEN}{BOLD}{hostname}{RESET}{DARK_CYAN}]─[{BLUE}{BOLD}{ip}{RESET}{DARK_CYAN}]")
    print(f"{DARK_CYAN}└──╼ {RESET}{GREEN}{BOLD}⚡{RESET} ", end="")

    print(SHOW_CURSOR, end="")


if __name__ == "__main__":
    try:
        show_banner()
    except KeyboardInterrupt:
        print(f"\n{RED}{BOLD}⚠ System interrupted by user{RESET}")
        print(f"{GREEN}Exiting gracefully...{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{RED}{BOLD}⚠ Error: {e}{RESET}")
        sys.exit(1)