import requests
import json
import pandas as pd
import time

base_url = "https://data.stats.gov.cn/easyquery.htm"


# ?m=QueryData&dbcode=hgyd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%5D&k1=1649741442313&h=1


def getTime():
    return int(round(time.time() * 1000))


def get_text(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    }

    key = {}
    key['m'] = 'QueryData'
    key['dbcode'] = 'hgyd'
    key['rowcode'] = 'zb'
    key['colcode'] = 'sj'
    key['wds'] = '[]'
    key['dfwds'] = '[]'
    key['k1'] = str(getTime())

    res = requests.post(url, params=key, headers=headers, verify=False)
    return res


def parse_text(text):
    res = {}
    data = json.loads(text)
    data = data['returndata']['datanodes']
    len_data = len(data)
    for i in range(len_data):
        res[i] = data[i]['data']['strdata']
    return res


if __name__ == "__main__":
    r = get_text(base_url)
    json_data = json.loads(r.text)
    print(json_data)
    res = parse_text(r.text)
    print(res)

