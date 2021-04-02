from bs4 import BeautifulSoup
import requests
from time import sleep
# from requests.api import get

# https://w3.cima4u.live/

# user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'

# url = 'https://cima4u.live/category/%d8%a7%d9%81%d9%84%d8%a7%d9%85-%d8%a7%d8%ac%d9%86%d8%a8%d9%8a-movies-english/?__cf_chl_jschl_tk__=612214f7b8b468b1953db749e9c588e04d622282-1617394997-0-AZdzPGbH_11QFSE1HX_qyJuDmzY_njTTSQ2kSdesDjtQYGY2W2u2Oxox5ijJLIaGwSIUXgKl7YZgP_dHBDWVWiuH92XvIQL-sY56IFMLtBf2TeMNaEUSzVPklW3IJyyh-HW56J3bzoPPZMic19ilknGAHagMNXw4bjHY5Z1Id2KliF9-eMZIVGoVm9LFeYccnV1Q1oUj4YD_k2AQE6SGtOkMEFmPJRfHscP-Eeh2rVSsOFG3kfmBvRTGB0UGaK4R0UvAj4ejAR67ooqVDoI2TynagYJivmRNBMWygrcui_vBZqyR2NvgnV3QdaBOCMYqre26HccvuxBBKPiFKfxVSBeUtA6YwEmiKlkugpdEW9VBNKAaOOI3bB5JpOfp7HRZLMjzG4nDItYhT3WDwqlVg-s3esTtM0oDEdnaVRAJbJM7N-IZuZYte5WfK9NLqUEqdTH7Bg0yhfLJ1ULMZ32ttHvkM7tzASK6hfVOE-hoqBGe'
url = 'https://cima4u.live/category/%d8%a7%d9%81%d9%84%d8%a7%d9%85-%d8%b9%d8%b1%d8%a8%d9%8a-arabic-movies/'
# user agent
headers = {
    "USER_AGENT":"'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'"
}
# # Open Session
# s = requests.Session()

# # update headers
# s.headers.update(headers)

# # Request of king get
# r = s.get(url)

# # create object from BeautifulSoup
# soup = BeautifulSoup(r.content, "html.parser")
# # sleep(5)
# print(soup.text)

def get_soup_object(url, headers={}):
    # Open Session
    s = requests.Session()

    # update headers
    s.headers.update(headers)

    # Request of king get
    r = s.get(url)

    # create object from BeautifulSoup
    soup = BeautifulSoup(r.content, "html.parser")
    return soup

soup = get_soup_object(url, headers=headers)
sleep(2)

for items in soup.findAll("ul", {"class":"Cima4uBlocks"}):
    sleep(2)
    # print(items.text)
    for info in items.findAll("li", {"class":"MovieBlock"}):
        sleep(3)
        print(info.text)
        
# print(soup.text)



