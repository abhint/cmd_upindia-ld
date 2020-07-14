import requests
from bs4 import BeautifulSoup

def banner():
    return """ 
           ____  _    _ _____ 
     /\   |  _ \| |  | |_   _|
    /  \  | |_) | |__| | | |  
   / /\ \ |  _ <|  __  | | |  
  / ____ \| |_) | |  | |_| |_ 
 /_/    \_\____/|_|  |_|_____|
        © ABHIJITH N T 
https://github.com/Abhijith-cloud
""" 
print(banner()) 

def index_upindia():
    url = input("[?] Enter URL uploadfile.cc / upindia.mobi:\n[?] > ")
    URL = url
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    page = requests.get(URL, headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    file_name_class = soup.title.get_text()
    file_name = str(file_name_class)
    print(file_name+ '\n')
    download_link = ''
    for link in soup.find_all(attrs="download_box_new link_download_1"):
        download_link = link.get('itemlink')  

    return download_link

def mirrorpage(pass_download_link):
    URL = 'http:' + pass_download_link
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    page = requests.get(URL, headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    download_link_m = ''
    for link in soup.find_all(attrs="mirror_link_v2"):
        download_link_m = link.get('itemlink')  
    print('http://upindia.mobi'+ download_link_m)

def main():
    returned_download_link = index_upindia()
    mirrorpage(returned_download_link) 
main()
