from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box
from colorama import init
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
try:
    import os
    import sys
    import time
    import json
    import random
    import string
    import requests
    import base64
    import subprocess
    import uuid
    import hashlib
    from collections import defaultdict    
    from datetime import datetime, timedelta
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich import box
    from colorama import init
    from pystyle import Colors, Colorate
except ModuleNotFoundError as e:
    lib = e.name
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', lib])
        print("\n 💻 Cài đặt thư viện {lib} thành công ✔️")
    except subprocess.CalledProcessError:
        print(f"Không thể cài đặt {lib}, thoát...")
        sys.exit(1)
from rich.panel import Panel
from rich.text import Text
from rich import box
from colorama import init
from pystyle import Colors, Colorate 
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

try:
    import os
    import sys
    import time
    import json
    import random
    import string
    import requests
    import base64
    import subprocess
    import uuid
    import hashlib
    from collections import defaultdict    
    from datetime import datetime, timedelta
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich import box
    from colorama import init
    from pystyle import Colors, Colorate
except ModuleNotFoundError as e:
    lib = e.name
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', lib])
        print("\n 💻 Cài đặt thư viện {lib} thành công ✔️")
    except subprocess.CalledProcessError:
        print(f"Không thể cài đặt {lib}, thoát...")
        sys.exit(1)

trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam = '\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
AQUA = "\033[96m"
LIME = "\033[92m"
hongnhat = "#FFC0CB"
kt_code = "🌸"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
vua = "\033[1;39m[\033[1;32m ¤ \033[1;39m] \033[32;5;245m\033[1m\033[38;5;39m=> "

import threading
import base64
import os
import time
import re
import json
import random
import requests
import socket
import sys
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box
from colorama import init
from pystyle import Colors, Colorate 
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor



import os
try:
    import os
    import sys
    import time
    import json
    import random
    import string
    import requests
    import base64
    import subprocess
    import uuid
    import hashlib
    from collections import defaultdict    
    from datetime import datetime, timedelta
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich import box
    from colorama import init
    from pystyle import Colors, Colorate
except ModuleNotFoundError as e:
    lib = e.name
    print(f"Thiếu thư viện {lib}, đang cài đặt 💻...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', lib])
        print("\n📂 \033[1;32mĐã tải thư viện \033[1;31m{lib} ")
        os.execl(sys.executable, sys.executable, *sys.argv)
    except subprocess.CalledProcessError:
        print(f"Không thể cài đặt {lib}, thoát...")
        sys.exit(1)
    
    
#import lại sau khi cài đặt
from faker import Faker
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box
from colorama import init
from pystyle import Colors, Colorate
import requests

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print (Colorate.Diagonal(Colors.cyan_to_green, """
    
                      © Bản Quyền Thuộc PhuocAn 
                      
    ██████╗ ██╗  ██╗██╗   ██╗ ██████╗  ██████╗                                            
    ██████╔╝███████║██║   ██║██║   ██║██║                         
    ██╔═══╝ ██╔══██║██║   ██║██║   ██║██║                           
    ██║     ██║  ██║╚██████╔╝╚██████╔╝╚██████╗                      
    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝  ╚═════╝ 

    ▶ Nhóm   :  https://zalo.me/g/mprgxe166        
    ▶ FaceBook : facebook.com/phuocan.9999         
    ▶ Youtube : youtube.com/@phuocan.9999          
    ▶ Zalo : 0915.948.201                          
    
================================

"""))

os.system('cls' if os.name == 'nt' else 'clear')
print("")
banner()

def reverse_string(s):
    return s[::-1]

def xePwjMDG(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

def tLx6cpsx():
    url = 'https://api.mail.tm/domains'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['hydra:member']
        else:
            pass
            return None
    except Exception as e:
        print(f'{vua}{do}[×] Error: {e}')
        return None

def f9kSLNSXl():
    fake = Faker()
    mail_domains = tLx6cpsx()
    if mail_domains:
        domain = random.choice(mail_domains)['domain']
        username = xePwjMDG(10)
        password = fake.password()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=59)
        first_name = fake.first_name()
        last_name = fake.last_name()
        url = 'https://api.mail.tm/accounts'
        headers = {'Content-Type': 'application/json'}
        data = {'address': f'{username}@{domain}', 'password': password}
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 201:
                print(Colorate.Diagonal(Colors.green_to_red,f'[ √ ] 💻 Tạo Mail Ảo Thành Công : {username}@{domain}'))
                return (f'{username}@{domain}', password, first_name, last_name, birthday)
            else:
                pass
                return None, None, None, None, None
        except Exception as e:
            print(f'{vua}{do}[×] Error: {e}')
            return None, None, None, None, None
    return None, None, None, None, None

def QuanHau(email, password, first_name, last_name, birthday):
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    gender = random.choice(['Gái', 'Trai' ,'Gaysex','Khác'])

    req = {
        'api_key': api_key,
        'attempt_login': True,
        'birthday': birthday.strftime('%Y-%m-%d'),
        'client_country_code': 'EN',
        'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod',
        'fb_api_req_friendly_name': 'registerAccount',
        'firstname': first_name,
        'format': 'json',
        'gender': gender,
        'lastname': last_name,
        'email': email,
        'locale': 'en_US',
        'method': 'user.register',
        'password': password,
        'reg_instance': xePwjMDG(32),
        'return_multiple_errors': True
    }

    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
    ensig = hashlib.md5((sig + secret).encode()).hexdigest()
    req['sig'] = ensig

    api_url = 'https://b-api.facebook.com/method/user.register'
    response = requests.post(api_url, data=req)

    if response.status_code == 200:
        reg = response.json()
        id = reg.get('new_user_id')
        token = reg.get('session_info', {}).get('access_token')
        print(Colorate.Diagonal(Colors.red_to_green,
            f"""[ √ ] Email Acc 💻 : {email} 📂
[ √ ] Mật Khẩu 💻 : {password} 📂
[ √ ] Tên 💻 : {first_name} {last_name} 📂
[ √ ] Sinh Nhật 💻 : {birthday} 📂
[ √ ] Giới Tính 💻 : {gender} 📂
[ √ ] Reg TK Thành Công ✔️
[ √ ] Chúc bạn 8386 🌃
==================================="""
        ))
    else:
        print(f'{vua}{do} Reg Thất Bại : {response.text}')

def WcfriFTc(url, params, post=True):
    headers = {
        'User-Agent': '[FBAN/FB4A;FBAV/35.0.0.48.273;FBDM/{density=1.33125,width=800,height=1205};FBLC/en_US;FBCR/;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/4.1.1;FBBK/0;]'
    }
    if post:
        response = requests.post(url, data=params, headers=headers)
    else:
        response = requests.get(url, params=params, headers=headers)
    return response.json()

def create_accounts(num_accounts):
    for i in range(num_accounts):
        email, password, first_name, last_name, birthday = f9kSLNSXl()
        if email and password and first_name and last_name and birthday:
            QuanHau(email, password, first_name, last_name, birthday)

# Sử dụng: gọi hàm create_accounts với số lượng tài khoản cần tạo
num_accounts = int(input(Colorate.Diagonal(Colors.green_to_cyan, '[ ♡ ] => Số TK FB Cần Reg ☞ : ')))
create_accounts(num_accounts)
