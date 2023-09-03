import requests
from sys import argv
import threading


def scan(url):
    shape = '\033[34m' + "[" +  '\033[91m' + "+" + '\033[34m' + "]" + '\033[34m' + " Found"
    with open("dires.txt", "r") as x:
        words = x.read().strip().split()  
    for word in words: 
        response = requests.get(f"{url}/{word}")
        if response.status_code == 200:
            print(shape +"\033[32m" + f" {url}/{word}")
        else:
            pass

if len(argv) < 2:
    print('\033[91m' + "My website : " + "\033[32m" + "https://rdkgt7us.000webhostapp.com/")
    print('\033[91m' + "My instgram : " + "\033[32m" + "r_d515\n")
    print('\033[91m' + "Usage: python main.py <https://url>")
else:
    website_url = argv[1]
    threading.Thread(target=scan, args=(website_url,)).start()

