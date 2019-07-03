import requests
import json


def getChamRank():
    url1="https://www.op.gg/champion/ajax/statistics/trendChampionList/type=banratio&"
    url2="https://www.op.gg/champion/ajax/statistics/trendChampionList/type=winratio&"
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    r=requests.get(url1,headers=header)
    sdw1=r.content.decode('utf-8')
    r=requests.get(url2,headers=header)
    sdw2=r.content.decode('utf-8')
    print(sdw1)    
    print(sdw2)    
    
def getChamStat(type, league, period, mapId, queue):
    url="https://www.op.gg/statistics/ajax2/champion/type={}&League={}&period={}&mapId={}&queue={}".format(type, league, period, mapId, queue)
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    r=requests.get(url,headers=header)
    sdw=r.content.decode('utf-8')
    print(sdw)    
    
def getTierStat(type, period, mapId, queue):
    url="https://www.op.gg/statistics/ajax2/tier/type={}&period={}&mapId={}&queue={}".format(type, period, mapId, queue)
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    r=requests.get(url,headers=header)
    sdw=r.content.decode('utf-8')
    print(sdw)




getChamRank()
getChamStat('win', 'all', 'month', '1', 'ranked')
getTierStat('kda', 'month', '1', 'ranked')