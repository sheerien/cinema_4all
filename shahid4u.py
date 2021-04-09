from bs4 import BeautifulSoup
import requests
import re 
from time import sleep


msg = '''

            *******************************************
            *** Mp4 link successfully obtained from ***
            ***            shahid4u                 ***
            *******************************************

'''
print(msg)


# url = 'https://shahid4u.dev/watch/%D9%81%D9%8A%D9%84%D9%85-the-big-bull-2021-%D9%85%D8%AA%D8%B1%D8%AC%D9%85-%D8%A7%D9%88%D9%86-%D9%84%D8%A7%D9%8A%D9%86'
url = input("Enter Your Movie or Series URL: ")
# user agent
header = {
    "USER_AGENT":"'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'"
}


# # Open Session
s = requests.Session()

# # update headers
s.headers.update(header)

# # Request of king get
r = s.get(url)


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
    first= 'h5.amzn-cdn.net/'
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
    first= 'h5.amzn-cdn.net/'
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

url_emb = get_emb_url(r)
# print(url_emb)

r = s.get(url_emb)

print('360p: ') ; get_mp4_link_360p(r)

print('plz wait ...')
sleep(5)

print('')
print('720p: '); get_mp4_link_720p(r)
