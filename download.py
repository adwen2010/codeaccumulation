from bs4 import BeautifulSoup
import requests
import os

def main():
    url = 'https://finance.sina.cn/2020-03-27/detail-iimxxsth2166312.d.html?from=groupmessage'
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text)
    imgs = soup.find_all('head')
    print(imgs['title'])
    

def test():
    url = 'https://finance.sina.cn/2020-03-27/detail-iimxxsth2166312.d.html?from=groupmessage'
    res = requests.get(url)
    soup = BeautifulSoup(res.text)
    imgs = soup.find_all('img')
    os.mkdir('c:/test')
    for i in imgs:
        path = i.get('data-src')
        if path == None :
            continue
        newurl = 'https:' + str(path)
        print(newurl)
        response = requests.get(newurl)
        filepath = 'c:/test/' + newurl[-10:-4]
        filepath = filepath + '.jpg'
        print(filepath)
        with open(filepath,'wb+') as file:
            file.write(response.content)

main()