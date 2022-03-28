#! /usr/bin/python3

import sys, requests, bs4, webbrowser,os


# Read the command line arguments from sys.argv.
#Fetch the search result page with the requests module.\
url = 'https://xkcd.com'  
os.makedirs('xkcd', exist_ok=True)    # store comics in ./xkcd
os.chdir(os.path.join(os.getcwd(), 'xkcd'))
while not url.endswith('#'):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    img = soup.select('html body div#middleContainer.box div#comic img')
    if img == []:
        print('Could not find comic image.')
    else:
        imgURL = 'https:' + img[0].get('src')
        res = requests.get(imgURL)
        res.raise_for_status()
        fhan = open('xkcd.txt', 'wb')
        for chunk in res.iter_content(100000):
            fhan.write(chunk)
        fhan.close()
    prev = soup.select('html body div#middleContainer.box ul.comicNav li a')
    url += prev[0].get('href')


