import os
import requests
#http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/509/509-bigskin-2.jpg

#https://pvp.qq.com/web201605/herodetail/509.shtml
#https://pvp.qq.com/web201605/herodetail/510.shtml

#https://pvp.qq.com/web201605/js/herolist.json  --英雄列表

url='https://pvp.qq.com/web201605/js/herolist.json'
html=requests.get(url)
html_json=html.json()  #转换成json格式

hero_name=list(map(lambda x:x['cname'],html.json()))
hero_number=list(map(lambda x:x['ename'],html.json()))
# print(hero_name)
# print(hero_number)

def main():
    wz=0
    for i in hero_number:
        os.mkdir("C:\\Users\\小草\\Desktop\\王者荣耀皮肤\\"+hero_name[wz])   #创建文件夹
        os.chdir("C:\\Users\\小草\\Desktop\\王者荣耀皮肤\\"+hero_name[wz])     #进入文件夹
        wz+=1
        for j in range(12):
            #拼接url
            onehero_links='http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'+str(i)+'/'+str(i)+'-bigskin-'+str(j)+'.jpg'
            im=requests.get(onehero_links)  #得到的链接，请求连接
            if im.status_code==200:   #请求的返回状态码
                open(str(j)+'.jpg','wb').write(im.content)

main()

# 模拟浏览器--突破反爬虫虫机制
# headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/64.0"
# }


