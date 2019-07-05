# issue: When certain have no data, deal with the error code
# issue: Crawl the champion page
# issue: find out the champion id and the correspond champion on op.gg

import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime
import csv

class ChampionRank:
    def __init__(self):
        self.processHTML()

    def __str__(self):
        return str(self.data)

    def requestData(self):
        urlBan="https://www.op.gg/champion/ajax/statistics/trendChampionList/type=winratio&"
        urlWin="https://www.op.gg/champion/ajax/statistics/trendChampionList/type=banratio&"
        header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        r=requests.get(urlBan,headers=header)
        sdw1=r.content.decode('utf-8')
        r=requests.get(urlWin,headers=header)
        sdw2=r.content.decode('utf-8')
        return sdw1, sdw2

    def processHTML(self):
        sdw1, sdw2 = self.requestData()
        soup1 = BeautifulSoup(sdw1, 'html.parser')
        soup2 = BeautifulSoup(sdw2, 'html.parser')
        self.data = {'#': ['name','Position', 'Win Rate', 'Pick Rate', 'Ban Rate']}
        for idx, tr in enumerate(soup1.tbody.find_all('tr')):
            tds = tr.find_all('td')
            divs = tds[2].find_all('div')
            name_position = str(divs[0].string)+';'+str(divs[1].string.strip().replace('\t', ''))
            self.data[name_position] = []
            self.data[name_position].append(divs[0].string)
            self.data[name_position].append(divs[1].string.strip().replace('\t', ''))
            self.data[name_position].append(tds[3].contents[0].string)
            self.data[name_position].append(tds[4].contents[0].string)

        for idx, tr in enumerate(soup2.tbody.find_all('tr')):
            tds = tr.find_all('td')
            divs = tds[2].find_all('div')
            name_position = str(divs[0].string)+';'+str(divs[1].string.strip().replace('\t', ''))
            self.data[name_position].append(tds[3].contents[0].string)

    def saveToCSV(self):
        with open('./data/ChamRank--{}.csv'.format(datetime.now().strftime('%Y-%m-%d %H')), 'w', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow((self.data.keys()))
            for i in self.data.keys():
                csv_writer.writerow(self.data[i])


class ChampionStat:
    def __init__(self, type, league, period, mapId, queue):
        self.__type=type
        self.__league=league
        self.__period=period
        self.__mapId=mapId
        self.__queue=queue

        self.processHTML()

    def __str__(self):
        return str(self.data)

    def qCode_to_string(self, type, league, period, mapId, queue):
        typeD = {'win': 'Win rate', 'lose': 'Low win ratio',
            'picked': 'Pick ratio per game', 'banned': 'Ban ratio per game'}
        leagueD = {'all': 'All', 'iron': 'Iron',
            'bronze': 'Bronze', 'silver': 'Silver',
            'gold': 'Gold', 'platinum': 'Platinum',
            'diamond': 'Diamond', 'master': 'Master',
            'grandmaster': 'Grand Master', 'challenger': 'Challenger'}
        periodD = {'month': 'Last Month', 'week': 'Last 7 Days', 'today': 'Today'}
        mapIdD = {'1': "Summoner's Rift", '10':'The Twisted Treeline', '12':'Howling Abyss'}
        queueD = {'ranked': 'Ranked', 'normal': 'Normal Queue', 'aram': 'ARAM'}

        self.type=typeD[type]
        self.league=leagueD[league]
        self.period=periodD[period]
        self.mapId=mapIdD[mapId]
        self.queue=queueD[queue]

    def requestData(self):
        url="https://www.op.gg/statistics/ajax2/champion/type={}&League={}&period={}&mapId={}&queue={}".format(
            self.__type, self.__league, self.__period, self.__mapId, self.__queue)
        header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        r=requests.get(url,headers=header)
        sdw=r.content.decode('utf-8')
        return sdw

    def processHTML(self):
        soup = BeautifulSoup(self.requestData(), 'html.parser')
        self.data = {}
        for idx, tr in enumerate(soup.find_all('tr')):
            if idx == 0:
                ths = tr.find_all('th')
                self.data[ths[0].string] = []
                self.data[ths[1].string] = []
                self.data[ths[2].string] = []
                self.data[ths[3].string] = []
                self.data[ths[4].string] = []
                self.data[ths[5].string] = []
                self.data[ths[6].string] = []
            if idx != 0:
                tds = tr.find_all('td')
                self.data[list(self.data.keys())[0]].append(tds[0].contents[0].string)
                self.data[list(self.data.keys())[1]].append(tds[2].contents[1].string)
                self.data[list(self.data.keys())[2]].append(tds[3].contents[3].string)
                gamePlayed = tds[4].contents[0].string.strip()
                self.data[list(self.data.keys())[3]].append(''.join(gamePlayed.split(',')))
                self.data[list(self.data.keys())[4]].append(tds[5].contents[1].string)
                self.data[list(self.data.keys())[5]].append(tds[6].contents[3].string)
                gold = tds[7].contents[3].string
                self.data[list(self.data.keys())[6]].append(''.join(gold.split(',')))

    def saveToCSV(self):
        with open('./data/ChamStat--{}.csv'.format(datetime.now().strftime('%Y-%m-%d %H')), 'w', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow((self.data.keys()))
            for i in range(len(self.data['#'])):
                csv_writer.writerow([self.data[list(self.data.keys())[0]][i],
                    self.data[list(self.data.keys())[1]][i],
                    self.data[list(self.data.keys())[2]][i],
                    self.data[list(self.data.keys())[3]][i],
                    self.data[list(self.data.keys())[4]][i],
                    self.data[list(self.data.keys())[5]][i],  
                    self.data[list(self.data.keys())[6]][i]])  
    

championRank = ChampionRank()
print(championRank)
championRank.saveToCSV()

championStat = ChampionStat('win', 'all', 'month', '1', 'ranked')
print(championStat)
championStat.saveToCSV()

