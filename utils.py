import threading
from colorama import Fore, Style, init
from discord_webhook import *
from datetime import datetime

Lock = threading.Lock()
init(convert=True)
init(autoreset=True)

def formatProxy(ipAddress) -> str:
    proxyDetails = ipAddress.split(":")
    ipAddressFormatted = f'{proxyDetails[2]}:{proxyDetails[3]}@{proxyDetails[0]}:{proxyDetails[1]}'
    proxiesFormatted = {
        'http': f'http://{ipAddressFormatted}',
        'https': f'http://{ipAddressFormatted}'
    }
    return proxiesFormatted

def log(content):
    with Lock:
        print(f'[{datetime.now()}] {Fore.LIGHTMAGENTA_EX}{content}{Style.RESET_ALL}')
def log_success(content):
    with Lock:
        print(f'[{datetime.now()}] {Fore.LIGHTGREEN_EX}{content}{Style.RESET_ALL}')
def log_error_p(content):
    with Lock:
        print(f'[{datetime.now()}] {Fore.LIGHTRED_EX}{content}{Style.RESET_ALL}')
def log_info(content):
    with Lock:
        print(f'[{datetime.now()}] {Fore.YELLOW}{content}{Style.RESET_ALL}')
def logo(content):
    with Lock:
        print(f'{Fore.LIGHTMAGENTA_EX}{content}{Style.RESET_ALL}')
