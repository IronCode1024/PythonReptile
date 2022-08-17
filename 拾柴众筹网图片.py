import os
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve


    #http://www.zhongchou.cn/browse/id-23-ds     //公益    -p页码
    #http://www.zhongchou.cn/browse/id-28-ds     //农业    -p页码
    #http://www.zhongchou.cn/browse/id-28-tid-43-ds   //农业
    #http://www.zhongchou.cn/browse/id-16-ds     //出版    -p页码
    #http://www.zhongchou.cn/browse/id-10001-ds  //娱乐    -p页码
    #http://www.zhongchou.cn/browse/id-22-ds     //艺术    -p页码
    #http://www.zhongchou.cn/browse/id-18-p2     //其他

"""
爬取众筹网图片素材     网站地址：http://www.zhongchou.cn/
"""
#请求头：Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/64.0

# GET 请求：用于从服务器获取数据做处理的
# Post 请求：用于向服务器发送数据请求的
#if __name__=='__main__':#程序入口

saveDir = "F:\\VS2013项目源码文件\\拾柴众筹网项目\\拾柴众筹网素材"
######################################################爬取首页图片##############################################################
def shouye():
    #url='http://www.zhongchou.cn/sso-getLibJsPms'
    url = 'http://www.zhongchou.cn/'
    zc=requests.get(url)
    zc.encoding="utf-8"
    html=zc.text
    #        解析器【1、html.parser   2、lxml】
    bf=BeautifulSoup(html,'html.parser')
    #find 单个的获取数据       find_all  相当于是一个列表（容器）
    target_url=bf.find_all(class_="siteCardItemImgA ind")
    #target_url 网页的图片路径
    b=0
    for each in target_url:
        #                         alt图片的名字  =  src图片的路径
        #list_url.append(each.img.get('src')+"="+each.img.get('alt'))   #append()方法是一个追加，将所有的数据追加到列表的后面
        #os.mkdir("C:\\Users\\Admin\\Desktop\\拾柴众筹网素材\\")
        os.chdir("C:\\Users\\Admin\\Desktop\\拾柴众筹网素材\\")
        imgs=requests.get(each.img.get('src'))
        #name=each.img.get('src')
        b+=1
        open(str(b)+'.jpg', 'wb').write(imgs.content)
######################################################爬取首页图片##############################################################
    #     open(str(each_img) + '.jpg', 'wb').write(im.content)
#shouye()

######################################################爬取公益项目图片（小图）##############################################################
def gongyi():
    #http://www.zhongchou.cn/browse/id-23-si_c
    #http://www.zhongchou.cn/browse/id-23-si_c-p2
    #http: // www.zhongchou.cn/browse/id-23-si_c-p79
    # url = 'http://www.zhongchou.cn/browse/id-23-si_c'
    # # siteCardItemImgA souSuo
    # gy = requests.get(url)
    # gy.encoding = 'utf-8'
    # html_gy = gy.text
    # bf = BeautifulSoup(html_gy, 'html.parser')
    # target_gyurl = bf.find_all(class_="siteCardItemImgA souSuo")
    #
    # b = 0
    # os.mkdir(saveDir + "\\公益众筹项目素材\\第" + str(1) + '页')
    # for each in target_gyurl:
    #     os.chdir(saveDir + "\\公益众筹项目素材\\第" + str(1) + '页')
    #     gyimgs = requests.get(each.img.get('src'))
    #     b += 1
    #     open(str(b) + '.jpg', 'wb').write(gyimgs.content)


    numy=1
    numyy = ""
    for item in range(0,79):
        url = 'http://www.zhongchou.cn/browse/id-23-si_c'+str(numyy)
        #siteCardItemImgA souSuo
        gy = requests.get(url)
        gy.encoding = 'utf-8'
        html_gy=gy.text
        bf = BeautifulSoup(html_gy, 'html.parser')
        target_gyurl = bf.find_all(class_="siteCardItemImgA souSuo")

        b = 0
        os.mkdir(saveDir + "\\公益众筹项目素材\\第" + str(numy) + '页')
        for each in target_gyurl:
            os.chdir(saveDir + "\\公益众筹项目素材\\第"+str(numy)+'页')
            gyimgs = requests.get(each.img.get('src'))
            b += 1
            open(str(b) + '.jpg', 'wb').write(gyimgs.content)
        numy += 1
        numyy = "-p" + numy.__str__()
#gongyi()
######################################################爬取公益众筹项目图片（小图）##############################################################


######################################################爬取农业众筹项目图片（小图）##############################################################
def master():
    #http://www.zhongchou.cn/browse/id-28-ds     //农业    -p页码
    #http://www.zhongchou.cn/browse/id-28-tid-43-ds   //农业

    #url='http://www.zhongchou.cn/'
    num=1

    # http://www.zhongchou.cn/browse/id-28-ds
    # normalPage
    for i in range(0,5):
        urll='http://www.zhongchou.cn/browse/id-28-tid-4'+str(num)+'-ds'

        tid = requests.get(urll)
        tid.encoding = 'utf-8'
        html_tid = tid.text
        bf = BeautifulSoup(html_tid, 'html.parser')
        target_tidurl = bf.find_all(class_="normalPage")
        #print(target_tidurl)

        for item in target_tidurl:
            hh=item.get('href')
            if hh == 'http://www.zhongchou.cn/browse/id-28-tid-41-ds':
                numyy = ""
                numy = 1
                for j in range(0,3):
                    tid1 = requests.get('http://www.zhongchou.cn/browse/id-28-tid-41-ds'+str(numyy))
                    tid1.encoding = 'utf-8'
                    html_tid1 = tid1.text
                    bf = BeautifulSoup(html_tid1, 'html.parser')
                    target_tid1 = bf.find_all(class_="siteCardItemImgA souSuo")
                    b = 0
                    os.mkdir(saveDir + "\\农业众筹项目素材\\生物科技\\第" + str(numy) + '页')
                    for each in target_tid1:
                        os.chdir(saveDir + "\\农业众筹项目素材\\生物科技\\第" + str(numy) + '页')
                        msimgs = requests.get(each.img.get('src'))
                        b += 1
                        if msimgs.status_code == 200:
                            open(str(b) + '.jpg', 'wb').write(msimgs.content)
                    numy += 1
                    numyy = "-p" + numy.__str__()
            elif hh == 'http://www.zhongchou.cn/browse/id-28-tid-42-ds':
                numyy2 = ""
                numy2 = 1
                for j in range(0, 10):
                    tid2 = requests.get(hh + str(numyy2))
                    tid2.encoding = 'utf-8'
                    htm2_tid1 = tid2.text
                    bf2 = BeautifulSoup(htm2_tid1, 'html.parser')
                    target_tid2 = bf2.find_all(class_="siteCardItemImgA souSuo")
                    b2 = 0
                    os.mkdir(saveDir + "\\农业众筹项目素材\\果蔬种植\\第" + str(numy2) + '页')
                    for each in target_tid2:
                        os.chdir(saveDir + "\\农业众筹项目素材\\果蔬种植\\第" + str(numy2) + '页')
                        msimgs = requests.get(each.img.get('src'))
                        b2 += 1
                        if msimgs.status_code == 200:
                            open(str(b2) + '.jpg', 'wb').write(msimgs.content)
                    numy2 += 1
                    numyy2 = "-p" + numy2.__str__()
            elif hh == 'http://www.zhongchou.cn/browse/id-28-tid-43-ds':
                numyy3 = ""
                numy3 = 1
                for j in range(0, 7):
                    tid3 = requests.get(hh + str(numyy3))
                    tid3.encoding = 'utf-8'
                    htm3_tid1 = tid3.text
                    bf3 = BeautifulSoup(htm3_tid1, 'html.parser')
                    target_tid3 = bf3.find_all(class_="siteCardItemImgA souSuo")
                    b3 = 0
                    os.mkdir(saveDir + "\\农业众筹项目素材\\生态养殖\\第" + str(numy3) + '页')
                    for each in target_tid3:
                        os.chdir(saveDir + "\\农业众筹项目素材\\生态养殖\\第" + str(numy3) + '页')
                        msimgs = requests.get(each.img.get('src'))
                        b3 += 1
                        if msimgs.status_code == 200:
                            open(str(b3) + '.jpg', 'wb').write(msimgs.content)
                    numy3 += 1
                    numyy3 = "-p" + numy3.__str__()
            elif hh == 'http://www.zhongchou.cn/browse/id-28-tid-44-ds':
                numyy4 = ""
                numy4 = 1
                for j in range(0, 10):
                    tid4 = requests.get(hh + str(numyy4))
                    tid4.encoding = 'utf-8'
                    html_tid4 = tid4.text
                    bf4 = BeautifulSoup(html_tid4, 'html.parser')
                    target_tid4 = bf4.find_all(class_="siteCardItemImgA souSuo")
                    b4 = 0
                    os.mkdir(saveDir + "\\农业众筹项目素材\\茶酒饮品\\第" + str(numy4) + '页')
                    for each in target_tid4:
                        os.chdir(saveDir + "\\农业众筹项目素材\\茶酒饮品\\第" + str(numy4) + '页')
                        msimgs = requests.get(each.img.get('src'))
                        b4 += 1
                        if msimgs.status_code == 200:
                            open(str(b4) + '.jpg', 'wb').write(msimgs.content)
                    numy4 += 1
                    numyy4 = "-p" + numy4.__str__()
            elif hh == 'http://www.zhongchou.cn/browse/id-28-tid-45-ds':
                numyy5 = ""
                numy5 = 1
                for j in range(0, 5):
                    tid5 = requests.get(hh + str(numyy5))
                    tid5.encoding = 'utf-8'
                    html_tid5 = tid5.text
                    bf5 = BeautifulSoup(html_tid5, 'html.parser')
                    target_tid5 = bf5.find_all(class_="siteCardItemImgA souSuo")
                    b5 = 0
                    os.mkdir(saveDir + "\\农业众筹项目素材\\休闲零食\\第" + str(numy5) + '页')
                    for each in target_tid5:
                        os.chdir(saveDir + "\\农业众筹项目素材\\休闲零食\\第" + str(numy5) + '页')
                        msimgs = requests.get(each.img.get('src'))
                        b5 += 1
                        if msimgs.status_code == 200:
                            open(str(b5) + '.jpg', 'wb').write(msimgs.content)
                    numy5 += 1
                    numyy5 = "-p" + numy5.__str__()
        num+=1

#master()
######################################################爬取农业众筹项目图片（小图）##############################################################

######################################################爬取出版众筹项目图片（小图）##############################################################
def chuban():
    # http://www.zhongchou.cn/browse/id-16-ds     //出版    -p页码
    numyy = ""
    numy = 1
    for j in range(0, 36):
        cb = requests.get('http://www.zhongchou.cn/browse/id-16' + str(numyy))
        cb.encoding = 'utf-8'
        html_cb = cb.text
        bf = BeautifulSoup(html_cb, 'html.parser')
        target_tid = bf.find_all(class_="siteCardItemImgA souSuo")
        b = 0
        os.mkdir(saveDir + "\\出版众筹项目素材\\第" + str(numy) + '页')
        for each in target_tid:
            os.chdir(saveDir + "\\出版众筹项目素材\\第" + str(numy) + '页')
            msimgs = requests.get(each.img.get('src'))
            b += 1
            if msimgs.status_code == 200:
                open(str(b) + '.jpg', 'wb').write(msimgs.content)
        numy += 1
        numyy = "-p" + numy.__str__()

#chuban()
######################################################爬取出版众筹项目图片（小图）##############################################################

######################################################爬取娱乐众筹项目图片（小图）##############################################################
def yule():
    #http://www.zhongchou.cn/browse/id-10001-p2
    #numyy = ""
    numy = 16
    numyy = "-p" + numy.__str__()
    for j in range(0, 20):
        cb = requests.get('http://www.zhongchou.cn/browse/id-10001' + str(numyy))
        cb.encoding = 'utf-8'
        html_cb = cb.text
        bf = BeautifulSoup(html_cb, 'html.parser')
        target_tid = bf.find_all(class_="siteCardItemImgA souSuo")
        b = 0
        os.mkdir(saveDir + "\\娱乐众筹项目素材\\第" + str(numy) + '页')
        for each in target_tid:
            os.chdir(saveDir + "\\娱乐众筹项目素材\\第" + str(numy) + '页')
            msimgs = requests.get(each.img.get('src'))
            b += 1
            if msimgs.status_code == 200:
                open(str(b) + '.jpg', 'wb').write(msimgs.content)
        numy += 1
        numyy = "-p" + numy.__str__()
#yule()
######################################################爬取娱乐众筹项目图片（小图）##############################################################

######################################################爬取艺术众筹项目图片（小图）##############################################################
def yishu():
    #http://www.zhongchou.cn/browse/id-22-p2
    #numyy = ""
    numy = 41
    numyy = "-p" + numy.__str__()
    for j in range(0, 2):
        cb = requests.get('http://www.zhongchou.cn/browse/id-22' + str(numyy))
        cb.encoding = 'utf-8'
        html_cb = cb.text
        bf = BeautifulSoup(html_cb, 'html.parser')
        target_tid = bf.find_all(class_="siteCardItemImgA souSuo")
        b = 0
        os.mkdir(saveDir + "\\艺术众筹项目素材\\第" + str(numy) + '页')
        for each in target_tid:
            os.chdir(saveDir + "\\艺术众筹项目素材\\第" + str(numy) + '页')
            msimgs = requests.get(each.img.get('src'))
            b += 1
            if msimgs.status_code == 200:
                open(str(b) + '.jpg', 'wb').write(msimgs.content)
        numy += 1
        numyy = "-p" + numy.__str__()
#yishu()
######################################################爬取艺术众筹项目图片（小图）##############################################################

######################################################爬取艺术众筹项目图片（小图）##############################################################
def qita():
    #http://www.zhongchou.cn/browse/id-18-p2
    numyy = ""
    numy = 1
    #numyy = "-p" + numy.__str__()
    for j in range(0, 54):
        qt = requests.get('http://www.zhongchou.cn/browse/id-18' + str(numyy))
        qt.encoding = 'utf-8'
        html_cb = qt.text
        bf = BeautifulSoup(html_cb, 'html.parser')
        target_tid = bf.find_all(class_="siteCardItemImgA souSuo")
        b = 0
        os.mkdir(saveDir + "\\其他众筹项目素材\\第" + str(numy) + '页')
        for each in target_tid:
            os.chdir(saveDir + "\\其他众筹项目素材\\第" + str(numy) + '页')
            msimgs = requests.get(each.img.get('src'))
            b += 1
            if msimgs.status_code == 200:
                open(str(b) + '.jpg', 'wb').write(msimgs.content)
        numy += 1
        numyy = "-p" + numy.__str__()

#qita()
######################################################爬取艺术众筹项目图片（小图）##############################################################






