import re
from bs4 import BeautifulSoup as bs
import requests
import json
import pandas as pd

# regex 기준으로 xpath 추출
def get_xpath(element):
    components = []
    child = element if element.name else element.parent

    for parent in child.parents:
        siblings = parent.find_all(child.name, recursive=False)
        components.append(
            child.name if 1 == len(siblings) else '%s[%d]' % (child.name, next(i for i, s in enumerate(siblings, 1) if s is child))
            )
        child = parent
    components.reverse()
    return '/%s' % '/'.join(components)

# 정규표현식으로 사용되는 특수문자 치환 & 시작(^)종료($) 세팅
def get_regex_param(param):
    res = ''

    if param.startswith('http'):
        res += param.replace('?', '\?')
    else:
        res = '^'
        for s in param:
            if s in '.*+?^$[]\{\}()|':
                res += '\\' + s
            else:
                res += s
        res += '$'

    return res

def main():
    # xpath return object define
    df = pd.DataFrame(columns=['site','title','price','img'])

    # xpath parameter read
    with open('etl/config.json', 'r', encoding='UTF-8') as f:
        config = json.load(f)['xpath']
        
    # url 갯수만큼 항목별 xpath 추출
    for target in config:
        url = config[target]['url']
        title = get_regex_param(config[target]['title'])
        price = get_regex_param(config[target]['price'])
        img = get_regex_param(config[target]['img'])

        html = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
        soup = bs(html, 'lxml')
        
        df.loc[df['title'].count()] = ([target
           ,get_xpath(soup.find(string=re.compile(title)))
           ,get_xpath(soup.find(string=re.compile(price)))
           ,get_xpath(soup.find(string=re.compile(img)))
        ])
    return df