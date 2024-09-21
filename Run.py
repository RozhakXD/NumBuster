import requests
import time
import sys
import os
import json

def callerprotect(phone_number):
    base_url = "https://callerprotect.de"
    path = "/api/v202310/search/{}".format(phone_number)

    headers = {
        'Accept-Encoding': 'UTF-8',
        'User-Agent' : 'okhttp/4.9.1',
        'Connection': 'Keep-Alive',
        'Host': 'callerprotect.de'
    }

    params = {
        'access_token': '6NaCG4bSV3UIWGu2zvKWpol2a1WsRiS96bZcMpWAaxz07JArZq', # You can replace it with your NumBuster Token!
        'locale': 'in',
        'timestamp': '{}'.format(int(time.time())),
        'signature': '',
        'cnonce': '',
        'paidSearch': '0',
        'order_by': 'interesting',
        'source': 'MAIN_SEARCH'
    }

    response = requests.get(f"{base_url}{path}", params=params, headers=headers, verify=True)
    json_response = json.loads(response.text)['data']
    
    if json_response['averageProfile'] != None:
        firstName = json_response['averageProfile']['firstName']
        lastName = json_response['averageProfile']['lastName']
    else:
        firstName = 'Tidak Diketahui'
        lastName = ''

    carrier = json_response['phone']['carrier']
    number = json_response['phone']['number']
    phone_region = json_response['phone']['region']
    region = 'Tidak ada' if phone_region == '' else phone_region
    seeMoreLink = json_response['common']['seeMoreLink']

    print("\n\x1b[1;97m================= \x1b[1;92mPROFILE PUBLIK\x1b[1;97m =================\n")
    print(f"\x1b[1;97mNama Lengkap     :\x1b[1;92m {firstName} {lastName}")
    print(f"\x1b[1;97mTautan           :\x1b[1;92m {seeMoreLink}")
    print(f"\x1b[1;97mCarrier          :\x1b[1;92m {carrier}")
    print(f"\x1b[1;97mRegion           :\x1b[1;92m {region}")
    print(f"\x1b[1;97mPhone Number     :\x1b[1;92m {number}\x1b[1;97m")

    return (True)

if __name__ == "__main__":

    os.system('cls' if os.name == 'nt' else 'clear')
    print("""\x1b[1;97m _   _                ______           _            
\x1b[1;97m| \ | |               | ___ \         | |           
\x1b[1;97m|  \| |_   _ _ __ ___ | |_/ /_   _ ___| |_ ___ _ __ 
\x1b[1;97m| . ` | | | | '_ ` _ \| ___ \ | | / __| __/ _ \ '__|
\x1b[1;97m| |\  | |_| | | | | | | |_/ / |_| \__ \ ||  __/ |   
\x1b[1;97m\_| \_/\__,_|_| |_| |_\____/ \__,_|___/\__\___|_|   """)

    phone_number = input('\n\x1b[1;97mEnter Phone Number:\x1b[1;92m ').replace(" ", "").replace("+", "")
    if phone_number.startswith('0'):
        new_phone_number = '62' + phone_number[1:]
    else:
        new_phone_number = phone_number
    callerprotect(phone_number=new_phone_number)
    sys.exit()