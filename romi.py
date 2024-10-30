import requests
import os
import re
import time
import random
from requests.exceptions import RequestException

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def lines():
    print('\u001b[37m' + '[>] ================================')

def lines2():
    print('\u001b[37m' + '[[>]] ===============ROMII=T00L=RUNNING================')

cls()

CLEAR_SCREEN = '\033[2J'
GREEN = "\033[1;32;1m"
RED = "\033[1;31;1m"
CYAN = "\033[1;36;1m"
YELLOW = "\033[1;33;1m"
BLUE = "\033[1;34;1m"
MAGENTA = "\033[1;35;1m"
RESET = "\033[0m"

def new_logo():
    logo_text = """

██████╗ ███████╗██████╗ ███████╗██╗         
██╔══██╗██╔════╝██╔══██╗██╔════╝██║         
██████╔╝█████╗  ██████╔╝█████╗  ██║         
██╔══██╗██╔══╝  ██╔══██╗██╔══╝  ██║         
██║  ██║███████╗██████╔╝███████╗███████╗    
╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚══════╝    

                                            
$$$$$$$\            $$\           $$\   $$\ 
$$  __$$\           $$ |          $$ |  $$ |
$$ |  $$ |$$\   $$\ $$ | $$$$$$\  \$$\ $$  |
$$$$$$$  |$$ |  $$ |$$ |$$  __$$\  \$$$$  / 
$$  __$$< $$ |  $$ |$$ |$$$$$$$$ | $$  $$<  
$$ |  $$ |$$ |  $$ |$$ |$$   ____|$$  /\$$\ 
$$ |  $$ |\$$$$$$  |$$ |\$$$$$$$\ $$ /  $$ |
\__|  \__| \______/ \__| \_______|\__|  \__|
                                            
                                            
                                            
                      
[> Note :: All rulex izzat Kro Humri warna  chod de ge tumhri <]
    """
    colors = [GREEN, RED, CYAN, YELLOW, BLUE, MAGENTA]
    box_width = max(len(line) for line in logo_text.split('\n'))
    print(random.choice(colors) + "┌" + "─" * (box_width + 2) + "┐")
    for line in logo_text.split('\n'):
        print(random.choice(colors) + "│ " + line.ljust(box_width) + " │")
    print(random.choice(colors) + "└" + "─" * (box_width + 2) + "┘" + RESET)

new_logo()

def read_cookie():
    try:
        lines()
        cookies_file = input("\033[1;36m[•] ENTER YOUR COOKIE FILE : ")
        lines()
        with open(cookies_file, 'r') as f:
            cookie = f.read().splitlines()
        return cookie
    except FileNotFoundError:
        print("GANDO FILE DEL ABUSE WALI")
        return None

def make_request(url, headers, cookie):
    try:
        response = requests.get(url, headers=headers, cookies={'Cookie': cookie}).text
        return response
    except RequestException as e:
        print("\033[1;31m[!] Error making request:", e)
        return None

def extract_target_id(url):
    match = re.search(r'target_id=(\d+)', url)
    return match.group(1) if match else None

def main():
    print("\033[1;36m(Mr Romi)Start Time:", time.strftime("%Y-%m-%d %H:%M:%S"))

    while True:
        try:
            cookies_data = read_cookie()
            if cookies_data is None:
                break

            headers = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]'
            }

            valid_cookies = []
            for cookie in cookies_data:
                response = make_request('https://business.facebook.com/business_locations', headers=headers, cookie=cookie)
                if response:
                    try:
                        token_eaag = re.search('(EAAG\w+)', str(response)).group(1)
                        valid_cookies.append((cookie, token_eaag))
                    except AttributeError:
                        print("\033[1;31m[!] EAAG token not found in the response for cookie:", cookie)
                        continue
                else:
                    print("\033[1;31m[!] No response for cookie:", cookie)

            if not valid_cookies:
                print("\033[1;31m[!] No valid cookie found. Exiting...")
                break

            post_url = input("\033[1;36m[[=>]] ENTER THE FACEBOOK POST URL : ")
            target_id = extract_target_id(post_url)
            if not target_id:
                print("\033[1;31m[!] Invalid URL. Exiting...")
                break

            commenter_name = input("\033[1;36m[[=>]] ENTER YOUR HATER NAME HERE : ")
            lines()
            delay = int(input("\033[1;36m[[=>]] ENTER YOUR TIME HERE : "))
            lines()

            comment_file_path = input("\033[1;36m[[=>]] ENTER YOUR COMMENTS FILE HERE (IN .txt ) : ")

            with open(comment_file_path, 'r') as file:
                comments = file.readlines()
            lines()
            x, y, cookie_index = 0, 0, 0

            while True:
                try:
                    teks = comments[x].strip()
                    comment_with_name = f"{commenter_name}: {teks}"

                    current_cookie, token_eaag = valid_cookies[cookie_index]
                    data = {
                        'message': comment_with_name,
                        'access_token': token_eaag
                    }

                    print("\033[1;36m[>] Opening and submitting comment")
                    response2 = requests.post(f'https://graph.facebook.com/{target_id}/comments/', data=data, cookies={'Cookie': current_cookie}).json()

                    if 'id' in response2:
                        print("\033[1;32mTarget id ::", target_id)
                        print("\033[1;32mDate time ::", time.strftime("%Y-%m-%d %H:%M:%S"))
                        print("\033[ 1;32mCOOKIE No. ::" , cookie_index+1)
                        print("\033[1;32mComment sent ::", comment_with_name)
                        lines2()
                        x = (x + 1) % len(comments)
                        cookie_index = (cookie_index + 1) % len(valid_cookies)
                    else:
                        y += 1
                        print("\033[1;31m[{}] Status : Failure".format(y))
                        print("\033[1;31m COOKIE NUMBER : " , cookie_index +1)
                        print("\033[1;31m[/]Link : https://m.basic.facebook.com//{}".format(target_id))
                        print("\033[1;31m[/]Comments : {}\n".format(comment_with_name))
                        x = (x + 1) % len(comments)
                        cookie_index = (cookie_index + 1) % len(valid_cookies)
                        y += 1
                        time.sleep(delay)

                except RequestException as e:
                    print("\033[1;31m[!] Error making request:", e)
                    time.sleep(5.5)
                    continue

        except Exception as e:
            print("\033[1;31m[!] An unexpected error occurred:", e)
            break

if __name__ == "__main__":
    main()
