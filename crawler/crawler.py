import requests
import json
from bs4 import BeautifulSoup

def getChamRank():
    url1="https://www.op.gg/champion/ajax/statistics/trendChampionList/type=banratio&"
    url2="https://www.op.gg/champion/ajax/statistics/trendChampionList/type=winratio&"
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    r=requests.get(url1,headers=header)
    sdw1=r.content.decode('utf-8')
    r=requests.get(url2,headers=header)
    sdw2=r.content.decode('utf-8')
    
def getChamStat(type, league, period, mapId, queue):
    url="https://www.op.gg/statistics/ajax2/champion/type={}&League={}&period={}&mapId={}&queue={}".format(type, league, period, mapId, queue)
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    r=requests.get(url,headers=header)
    sdw=r.content.decode('utf-8')
    soup = BeautifulSoup(sdw, 'html.parser')
    for idx, tr in enumerate(soup.find_all('tr')):
        if idx == 0:
            ths = tr.find_all('th')
            print(ths[0].string)
            print(ths[1].string)
            print(ths[2].string)
            print(ths[3].string)
            print(ths[4].string)
            print(ths[5].string)
            print(ths[6].string)
        if idx != 0:
            tds = tr.find_all('td')
            print(tds[0].contents[0].string)
            print(tds[2].contents[1].string)
            print(tds[3].contents[3].string)
            print(tds[4].contents[0].string.strip())
            print(tds[5].contents[1].string)
            print(tds[6].contents[3].string)
            print(tds[7].contents[3].string)
            
    
def getTierStat(type, period, mapId, queue):
    url="https://www.op.gg/statistics/ajax2/tier/type={}&period={}&mapId={}&queue={}".format(type, period, mapId, queue)
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    r=requests.get(url,headers=header)
    sdw=r.content.decode('utf-8')




getChamRank()
getChamStat('win', 'all', 'month', '1', 'ranked')
getTierStat('kda', 'month', '1', 'ranked')