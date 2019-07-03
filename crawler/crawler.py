import requests
import json

def getTierStat(type, period, mapId, queue):
    url="https://www.op.gg/statistics/ajax2/tier/type={}&period={}&mapId={}&queue={}".format(type, period, mapId, queue)
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    r=requests.get(url,headers=header)
    sdw=r.content.decode('utf-8')
    print(sdw)
    
    
    
getTierStat('kda', 'month', '1', 'ranked')