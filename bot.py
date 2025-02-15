import requests
import asyncio
import aiohttp
from colorama import init, Fore, Style
from datetime import datetime

init(autoreset=True)

from colorama import Fore, Style, init

# Initialize colorama (for Windows support)
init(autoreset=True)

print(Fore.GREEN + Style.BRIGHT + """
██████╗ ██╗███╗   ██╗███████╗███████╗████████╗███████╗
██╔══██╗██║████╗  ██║██╔════╝██╔════╝╚══██╔══╝██╔════╝
██████╔╝██║██╔██╗ ██║█████╗  █████╗     ██║   █████╗  
██╔═══╝ ██║██║╚██╗██║██╔══╝  ██╔══╝     ██║   ██╔══╝  
██║     ██║██║ ╚████║███████╗███████╗   ██║   ███████╗
╚═╝     ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝   ╚═╝   ╚══════╝
""" + Style.RESET_ALL)

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Host": "mainnet.capfizz.com",
    "Referer": "https://mainnet.capfizz.com/dashboard/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"'
}

def load_cookies(filename="cookie.txt"):
    try:
        with open(filename, 'r') as file:
            cookie_string = file.read().strip()
            if cookie_string:
                headers["Cookie"] = cookie_string
                print(Fore.GREEN + Style.BRIGHT + f"Loaded cookies.")
            else:
                print(Fore.RED + Style.BRIGHT + "Error: Cookies not found in cookie.txt.")
    except FileNotFoundError:
        print(Fore.RED + Style.BRIGHT + "Error: cookie.txt not found.")

def load_proxies(filename="proxy.txt"):
    proxies = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                proxy = line.strip()
                if proxy:
                    proxies.append(proxy)
    except FileNotFoundError:
        print(Fore.RED + Style.BRIGHT + "Error: proxy.txt not found.")
    return proxies

async def make_get_request(session, url, proxy):
    try:
        async with session.get(url, headers=headers, proxy=proxy) as response:
            text = await response.text()
            print(Fore.CYAN + Style.BRIGHT + f"GET {url} (Proxy: {proxy}): {response.status}")
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + f"GET {url} failed (Proxy: {proxy}): {str(e)}")

async def make_post_request(session, url, proxy, data):
    try:
        async with session.post(url, json=data, headers=headers, proxy=proxy) as response:
            text = await response.text()
            print(Fore.BLUE + Style.BRIGHT + f"POST {url} (Proxy: {proxy}): {response.status}")
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + f"POST {url} failed (Proxy: {proxy}): {str(e)}")

async def perform_requests():
    load_cookies()
    proxies = load_proxies()
    base_url = "https://mainnet.capfizz.com/api"
    async with aiohttp.ClientSession() as session:
        while True:
            for proxy in proxies:
                print(Fore.WHITE + Style.BRIGHT + f"\nUsing Proxy: {proxy}")
                await make_get_request(session, f"{base_url}/user/extension/init", proxy)
                await make_get_request(session, f"{base_url}/user/extension/check-auth", proxy)
                await make_get_request(session, f"{base_url}/user/extension", proxy)
                await make_get_request(session, f"{base_url}/user/extension/uptime-static", proxy)
                await make_get_request(session, f"{base_url}/ping", proxy)
                await make_get_request(session, f"{base_url}/user/point", proxy)
                await make_get_request(session, f"{base_url}/user/info/", proxy)
                await make_post_request(session, f"{base_url}/node/mining", proxy, {"key": "value"})
                await asyncio.sleep(1)
            print(Fore.YELLOW + Style.BRIGHT + f"\nSyncing proxies at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(perform_requests())
