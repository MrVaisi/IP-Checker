import requests
import os
import time
from colorama import Fore, Style, init
from pyfiglet import Figlet

init(autoreset=True)
print (Fore.BLUE + """\..............
            ..,;:ccc,.
          ......```;lxO.
.....````..........,:ld;
           .`;;;:::;,,.x,
      ..```.            0Xxoc:,.  ...
  ....                ,ONkc;,;cokOdc`,.
 .                   OMo           `:ddo.
                    dMc               :OO;
                    0M.    Hr-team      .:o.
                    ;Wd
                     ;XO,
                       ,d0Odlc;,..
                           ..`,;:cdOOd::,.
                                    .:d;.`:;.
                                       'd,  .`
                                         ;l   ..
                                          .o
                                            c
                                            .`
                                             .""")
time.sleep(2.5)
os.system('clear' if os.name != 'nt' else 'cls')

f = Figlet(font='big')
ascii_art = f.renderText('HR Team')
print(Fore.GREEN + ascii_art)

def get_ip_info(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        data = response.json()
        if data['status'] == 'success':
            print(Fore.CYAN + f"\nInformation of IP {ip}:\n")
            print(Fore.CYAN + f"Country: {data.get('country', 'N/A')}")
            print(Fore.CYAN + f"Region: {data.get('regionName', 'N/A')}")
            print(Fore.CYAN + f"City: {data.get('city', 'N/A')}")
            print(Fore.CYAN + f"ZIP Code: {data.get('zip', 'N/A')}")
            print(Fore.CYAN + f"ISP: {data.get('isp', 'N/A')}")
            print(Fore.CYAN + f"Timezone: {data.get('timezone', 'N/A')}")
            
            lat = data.get('lat')
            lon = data.get('lon')
            if lat is not None and lon is not None:
                map_link = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
                print(Fore.YELLOW + f"Location Map: {map_link}")
        else:
            print(Fore.RED + "IP is not correct or API returned failure.")
    except Exception as e:
        print(Fore.RED + f"Error! {e}")

def main():
    while True:
        ip = input(Fore.GREEN + "\nInput IP target (or type 'exit' to quit): ")
        if ip.lower() == 'exit':
            break
        get_ip_info(ip)

if __name__ == "__main__":
    main()
