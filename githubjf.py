import os
import requests
# https://github.com/trending
# url='https://pvp.qq.com/web201605/js/herolist.json'
# html=requests.get(url)
# html_json=html.json()  #转换成json格式

# hero_name=list(map(lambda x:x['cname'],html.json()))
# hero_number=list(map(lambda x:x['ename'],html.json()))
# print(hero_name)
# print(hero_number)

# 模拟浏览器--突破反爬虫虫机制
# headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/64.0"
# }
import soup as soup
import json
from bs4 import BeautifulSoup

def main():
    url = 'https://github.com/trending'
    html = requests.get(url)
    html.encoding = 'utf-8'
    html_gy = html.text
    bf = BeautifulSoup(html_gy, 'html.parser',from_encoding='utf-8')
    box_row_url = bf.find_all(class_="Box-row")
    #print(box_row_url)
    # hero_name=list(map(lambda x:x['cname'],html.json()))
    # hero_number=list(map(lambda x:x['ename'],html.json()))
    for mneach in box_row_url:
        box_row_h1=mneach.find_all('h1',class_='h3 lh-condensed')
        box_row_p = mneach.find_all("p")
        box_row_div = mneach.find_all('div')
        # print(box_row_div)
        # 获取项目仓库地址
        for reap_Links in box_row_h1:
            # aherf=links.find_all("a")
            reop_ahref = str('https://www.github.com') + reap_Links.a.get('href')
            print("仓库地址：", str(reop_ahref), "\n仓库名称：",str(reap_Links.a.text).split('/'))
        # 获取说明文字
        for reop_Content in box_row_p:
            content=reop_Content.text
            print("获取说明文字:", str(content))

        # 获取下面的语言 star数等内容
        for reop_Bottom in box_row_div:
            # reop_ahref = str('https:www.github.com/') + reopLinks.a.get('href')
            bottomL = reop_Bottom.find_all('span',class_ = 'd-inline-block ml-0 mr-3')
            for btoL in bottomL:
                # 获取语言 类型
                Language = btoL.find(itemprop = 'programmingLanguage').text
                print("语言 类型:", str(Language))

            bottomZ = reop_Bottom.find_all('a', class_='muted-link d-inline-block mr-3')
            # bottomZsvg1 = reop_Bottom.find_all('svg', class_='octicon octicon-star')
            # bottomZsvg2 = reop_Bottom.find_all('svg', class_='octicon octicon-repo-forked')
            # print(bottomZ)
            # 循环的是bottomZ中的子元素的个数
            for btoZ in bottomZ:
                # 获取 点赞数
                bto = btoZ.text
                print(bto)
            # print(bottoms)


main()






# r = requests.get('https://www.qidian.com/')
# r.encoding = 'utf-8'
# soup = BeautifulSoup(r.text, from_encoding='utf-8')
def wrap_func():
    result = {}
    wrap = soup.select('#rank-list-row .rank-list')
    for item in wrap:
        if item['data-l2'] == "2":
            books_url = 'http:' + item.select('.wrap-title a')[0]['href']
            books_html = requests.get(books_url)
            books_soup = BeautifulSoup(books_html.text, from_encoding='utf-8')
            books = books_soup.select('.rank-body .book-img-text li')
            booklist = []
            num = 0
            for key in books:
                if num < 10:
                    info = {}
                    if len(key.select('.book-img-box a img')) > 0:
                        info['cover'] = key.select('.book-img-box a img')[0]['src']
                    if len(key.select('.book-mid-info h4 a')) > 0:
                        info['url'] = key.select('.book-mid-info h4 a')[0]['href']
                        info['title'] = key.select('.book-mid-info h4 a')[0].text
                    if len(key.select('.book-mid-info .author .name')) > 0:
                        info['actor'] = key.select('.book-mid-info .author .name')[0].text
                    booklist.append(info)
                num += 1
            index = 0
            wraplist = []
            wraplist1 = []
            for element in booklist:
                if index < 3:
                    wraplist1.append(element)
                else:
                    wraplist.append(element)
                index += 1
            result['wrapbox'] = wraplist
            result['wrap'] = wraplist1

    print(result)
    return json.dumps(result)

# wrap_func()
