from bs4 import BeautifulSoup
import requests
import re 
import os
from time import sleep


HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

# Bold Text Colors
bd_dark_Gray = '\033[1;30;40m'
bd_bright_Red = '\033[1;31;40m'
bd_bright_Green = '\033[1;32;40m'
bd_yellow = '\033[1;33;40m'
bd_bright_Blue = '\033[1;34;40m'
bd_bright_Magenta = '\033[1;35;40m'
bd_bright_Cyan = '\033[1;36;40m'
bd_white = '\033[1;37;40m'

# Text Color Grey Background
txt_black = '\033[0;30;47m'
txt_red = '\033[0;31;47m'
txt_green = '\033[0;32;47m'
txt_brown = '\033[0;33;47m'
txt_blue = '\033[0;34;47m'
txt_magenta = '\033[0;35;47m'
txt_cyan = '\033[0;36;47m'
txt_light_Grey = '\033[0;37;40m'

# Colored Background
bg_black = '\033[0;37;48m'
bg_red = '\033[0;37;41m'
bg_green = '\033[0;37;42m'
bg_yellow = '\033[0;37;43m'
bg_blue = '\033[0;37;44m'
bg_magenta = '\033[0;37;45m'
bg_cyan = '\033[0;37;46m'
bg_white = '\033[0;37;47m'


msg = '''

            *******************************************
            *** Mp4 link successfully obtained from ***
            ***            shahid4u                 ***
            *******************************************

'''
# print(msg)

# # url = "https://shahid4u.plus/episode/%D9%85%D8%B3%D9%84%D8%B3%D9%84-%D8%A7%D9%84%D9%84%D9%8A-%D9%85%D8%A7%D9%84%D9%88%D8%B4-%D9%83%D8%A8%D9%8A%D8%B1-%D8%A7%D9%84%D8%AD%D9%84%D9%82%D8%A9-1-%D8%A7%D9%84%D8%A7%D9%88%D9%84%D9%8A"
# url = input("Enter Your Movie or Series URL: ")
# user agent
header = {
    "USER_AGENT":"'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'",
    'referer': 'https://shahid4u.dev/'
}


# # Open Session
s = requests.Session()

# # update headers
s.headers.update(header)

# # Request of king get
# r = s.get(url)

def get_master_url(r):
    soup = BeautifulSoup(r.content, "html.parser")
    btns = soup.findAll('div', {'class':'btns'})
    for btn in btns:
        link = btn.find('a')
        master_link = link['href']
    return master_link


def get_emb_url(r):
    soup = BeautifulSoup(r.content, "html.parser")

    emb = soup.findAll('iframe')
    for i in emb:
        i_url = i['src'].split('.html://')
        i_url = i['src'].replace('\r', '')
        emb_url = i_url
        return emb_url

# url_emb = get_emb_url(r)
# # print(url_emb)

# r = s.get(url_emb)

def get_mp4_link_360p(r):
    text = r.content.decode()
    # print(text)

    for x in text.split("\n"):
        if 'eval(function(p,a,c,k,e,d)' in x:
            # print(x)
            data = x
            # data = data.split("|")
            # for num, txt in enumerate(data):
            #     print(f"{num} - {txt}")
    # # print(data)
    data = data.split("|")
    htp = 'https://'
    adb = data[32]
    first= f'{adb}.amzn-cdn.net/'
    # v3.amzn-cdn.net
    if len(data[90]) == 60 or len(data[90]) > 60:
        token=data[90]
        last='/v.mp4'
        mp4 = f'{htp}{first}{token}{last}'
        print('')
        print(mp4)
    else:
        token = "token is not found pls try again"
        last='/v.mp4'
        mp4 = f'{token}'
        # mp4 = f'{htp}{first}{token}{last}'
        print('')
        print(mp4)


def get_mp4_link_720p(r):
    text = r.content.decode()
    # print(text)

    for x in text.split("\n"):
        if 'eval(function(p,a,c,k,e,d)' in x:
            # print(x)
            data = x
            # data = data.split("|")
            # for num, txt in enumerate(data):
            #     print(f"{num} - {txt}")
    # # print(data)
    data = data.split("|")
    htp = 'https://'
    adb = data[22]
    first= f'{adb}.amzn-cdn.net/'
    if len(data[93]) == 60 or len(data[93]) > 60:
        token=data[93]
        last='/v.mp4'
        mp4 = f'{htp}{first}{token}{last}'
        print('')
        print(mp4)
    else:
        token = "token is not found pls try again"
        last='/v.mp4'
        mp4 = f'{token}'
        print('')
        print(mp4)


def show():
    print("")
    os.system("color 0a")
    os.system("mode 80,25")
    os.system('title  Movies 4U [ V 1.0.0 ]')
    os.system("cls")
    print(f"{bd_bright_Cyan}")
    sh = '''
                        ***********************
                        *****             *****
                        * Welcome Everybody:] *
                        *****             *****
                        ***********************
            
                    ╭━━━┳╮╱╭┳━━━┳╮╱╭┳━━┳━━━┳╮╱╭┳╮╱╭╮
                    ┃╭━╮┃┃╱┃┃╭━╮┃┃╱┃┣┫┣┻╮╭╮┃┃╱┃┃┃╱┃┃
                    ┃╰━━┫╰━╯┃┃╱┃┃╰━╯┃┃┃╱┃┃┃┃╰━╯┃┃╱┃┃
                    ╰━━╮┃╭━╮┃╰━╯┃╭━╮┃┃┃╱┃┃┃┣━━╮┃┃╱┃┃
                    ┃╰━╯┃┃╱┃┃╭━╮┃┃╱┃┣┫┣┳╯╰╯┃╱╱┃┃╰━╯┃
                    ╰━━━┻╯╱╰┻╯╱╰┻╯╱╰┻━━┻━━━╯╱╱╰┻━━━╯

           *****************************************************
           ****            shahid4u Tool @v1.0.0            ****
           ****        Developed by : Sherien Bassem        ****
           ****                MSD - Company                ****
           *****************************************************
    '''
    print(sh)
    input("Press Enter To Continue ....... ")

def run():
    print("")
    show()
    print("")
    os.system("cls")
    print("")
    website = '''
           *****************************************************
           ****               Go To Web-Site                ****
           ****       [ https://shahid4u.plus ]             ****
           ****       choose any Movie to fetch mp4 url     ****
           ****       choose any Series to fetch mp4 url    ****
           *****************************************************
    '''
    print(website)
    print("")
    print("======================= Enter Your Movie Url ==========================")
    print("")
    vod_path = input("Enter your movie url : ")
    is_url = re.search(
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", vod_path)
    if is_url:
        r = s.get(vod_path)
        master = get_master_url(r)
        # print(master)
        r = s.get(master)
        url_emb = get_emb_url(r)
        # print(url_emb)

        r = s.get(url_emb)

        print('')
        print('360p: ') ; get_mp4_link_360p(r)

        print('plz wait ...')
        sleep(5)

        print('')
        print('720p: '); get_mp4_link_720p(r)
    else:
        print("")
        print("Please Enter A Valid URL ...")
        sleep(5)
        os.system("cls")


run()
while True:
    try:
        user_choice = input("Do you want to continue [y/n]: ").lower().strip()
        if user_choice == 'y':
            run()
        elif user_choice == "n":
            print('The tool has been finished ...')
            sleep(3)
            exit()
        else:
            err_1 = '''
                    *******************************************
                    ***   Please Choose  [ y ] or [ n ]     ***
                    *******************************************
                    '''
            print(err_1)
            sleep(3)
    except ValueError:
        err_2 = '''
            *****************************************
            ***  Please Enter A Valid Choice !!!  ***
            *****************************************
        '''
        print(err_2)
        sleep(3)

# master = get_master_url(r)
# # print(master)
# r = s.get(master)
# url_emb = get_emb_url(r)
# # print(url_emb)

# r = s.get(url_emb)

# print('')
# print('360p: ') ; get_mp4_link_360p(r)

# print('plz wait ...')
# sleep(5)

# print('')
# print('720p: '); get_mp4_link_720p(r)

# pyinstaller --onefile "<nameScript.py>"
