import os
import requests
from urllib import request
import json
from tkinter import *
from tkinter import messagebox
#from PIL import ImageTk

# import soup as soup
# import json
from bs4 import BeautifulSoup

import traceback
# 输出中文乱码解决办法
# File->Settings->Editor->File Encodings

# 待加入功能：请求失败自动重试
# 需要下载视频总数
loadVideoCount = 0
# 以下载视频数


currentWorkPath = os.getcwd()


def main():
    while(1):
        print("请输入章节连接地址(输入e退出)：")
        inputStr = input()
        if (inputStr == "e"):
            return
        try:
            with request.urlopen(inputStr) as file:
                print(file.status)
                # print(file.reason)
                if(file.status == 200):
                    startLoading(inputStr)
        except Exception as e:
            traceback.print_exc()
            print(404)

# https://www.zlketang.com/wxpub/api/video_show?from=web&channel=web&devtype=web&platform_type=web&v_date=&t=1620575335199&teacher_id=17&year=2020&course_id=392&system=win

def startLoading(url):
    # https://www.zlketang.com/wxpub/api/video_show?from=web&channel=web&devtype=web&platform_type=web&v_date=&t=1620488939837&teacher_id=17&year=2020&course_id=5311&system=win
    # https://www.zlketang.com/wxpub/api/video_show?from=web&channel=web&devtype=web&platform_type=web&v_date=&t=1620488939837&teacher_id=17&year=2020&course_id=5311&system=win
    # s = requests.Session()


    c = {
        'sessionid': 'Hm_lpvt_856009d9a3adebb423815cf9d1af9218=1598851932; Hm_lvt_856009d9a3adebb423815cf9d1af9218=1598327119,1598399369,1598598493,1598851932; UM_distinctid=176f9697f3b5c0-0e0f39ec6c46ea-31346d-384000-176f9697f3c63c; Hm_lvt_13687f8c0c21b8bf841e8dfa626d539e=1620394592; SWOOLESESSSIONNAME=ptF9RHcXjzzRJyfOGHoOlvFXlqccv85o; PAGERECORDER=eyJjZiI6eyJwYWdlLXByb2JsZW0iOlsic3ViamVjdF9pZCIsImV4YW1fdHlwZSJdfSwiZmxhZyI6dHJ1ZSwidWlkIjoiNTFlMTFjYTc1ZWEwOTUyYjA4OGI0NzQ4NjNiZTM2ZDhlOWMyMTEwMGQxNzMzOTVkZjEzMDQ4ZDdlYzE2MTI3MCIsInRoaXJkX3VzZXJfaWQiOiJhOGMyNzc4YWI0NjYzNjIwODYwNjZkZTNkMTBhNTQwYyIsInVzZXJfcmVnaXN0ZXJfdHlwZSI6IjEifQ%3D%3D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22a8c2778ab466362086066de3d10a540c%22%2C%22%24device_id%22%3A%2217423b85b0865c-05b424a5f49e49-3323766-1327104-17423b85b09609%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2217423b85b0865c-05b424a5f49e49-3323766-1327104-17423b85b09609%22%7D; CNZZDATA1279575163=1760653551-1610498406-https%253A%252F%252Fwww.baidu.com%252F%7C1620534556; Hm_lpvt_13687f8c0c21b8bf841e8dfa626d539e=1620540502',
    }
    # url ="https://www.zlketang.com/wxpub/api/video_show?from=web&channel=web&devtype=web&platform_type=web&v_date=&t=1620488939837&teacher_id=17&year=2020&course_id=5311&system=win"
    html = requests.get(url,cookies=c)
    html.encoding = 'utf-8'
    html_text = html.text
    # print(html_text)
    html_json = json.loads(html_text)
    # print(html_json["data"]["videos"][0]["name"])
    # 章节名称（课程名称）
    course_name = html_json["data"]["course_name"]
    # savePath_course_name = "D:\\Users\\Desktop\\会计实操课程\\"+course_name+"\\"
    savePath_course_name = "E:\\会计实操课程\\"+course_name+"\\"


    # 章节视频列表
    chapterVideoList = html_json["data"]["videos"]
    videoCount = len(chapterVideoList)
    currentVideoNum = 0
    for i in chapterVideoList:# 遍历视频列表
        currentVideoNum =currentVideoNum+1
        savePath = savePath_course_name
        first_dir_name = ""
        second_dir_name = ""
        name = ""
        #i.keys()
        #i.values()
        #print(i.keys())
        for key in i.keys():# 遍历视频列表中的元素
            savePathList = []
            # 小节名称（目录）
            if(key == "first_dir_name"):
                first_dir_name = i["first_dir_name"]+"\\"
                # print("first_dir_name:" + first_dir_name)
            # 小小节名称(第二目录),有的可能没有此小目录，直接就是课程名称
            elif (key == "second_dir_name"):
                second_dir_name = i["second_dir_name"]+ "\\"
                # print("second_dir_name:" + second_dir_name)
            # 视频名称
            elif (key == "name"):
                name = i["name"]
                name = name.replace(" ", "")
                name = name.replace("+", "")
                # print("name:" + name)
        # 视频存放路径
        savePath += first_dir_name + second_dir_name

        print(i["hls"])
        # videoUrl = "http://tvod.zlketang.com/03131334vodsh1253769091/a3f1963f5285890806069578848/playlist.m3u8?t=6097b313&rlimit=3&us=1620540115356_7847_1000&sign=c32df66ff65a13ff4a119daa7a9bdfae"
        videoUrl = i["hls"]
        videoUrlSplit = videoUrl.split('playlist')[0]

        html_videoUrl = requests.get(videoUrl, cookies=c)
        html_videoUrl.encoding = 'utf-8'
        html_videoUrl_text = html_videoUrl.text
        #ret = html.content

        # 判断视频是否已经存在，存在则跳过，不再下载
        print("判断视频是否已经存在:"+savePath + name+".mp4")
        if (os.path.exists(savePath + name+".mp4")):
            print("下载的第："+str(currentVideoNum)+"个视频文件" + savePath + name + "已存在（已跳过）")
            continue
        html_videoUrl_text_Split = html_videoUrl_text.split('\n')
        fragmentNum = 0
        savePath = savePath.replace(" ", "")
        for strVideoUrl in html_videoUrl_text_Split:# 遍历视频碎片
            #print(strVideoUrl[0])
            if(len(strVideoUrl)>100):
                fragmentNum = fragmentNum + 1
                saveFile(fragmentNum, savePath, videoUrlSplit + strVideoUrl)
                print(str(videoCount)+"/"+str(currentVideoNum)+"-"+str((len(html_videoUrl_text_Split)/2)-3)+"/"+str(fragmentNum) +":"+ videoUrlSplit + strVideoUrl+"-"+course_name)
            #break

        os.chdir(savePath)# 切换节本工作目录
        os.system("copy /b *.ts "+name+".mp4")# 合并碎片视频
        print("结束总视频碎片数为：{}".format(fragmentNum))
        print("合并为mp4成功：" + name+".mp4")
        print("下载视频总数：" + str(videoCount) + "已下载数量："+str(currentVideoNum))
        # 合并完成，删除碎片文件
        removeFile(savePath,".ts")
        os.chdir(currentWorkPath)
        #break
        #print(savePath)
    return

    # # 获取用户输入的链接
    # name = entry.get()
    # urls = name
    # print(urls)
    # #urls = "https://tvod.zlketang.com/03131334vodsh1253769091/a5d87e505285890806069615652/942949821cb44cb19cbddf34f7154983-5e8768451fd28c10522318b1bdaf848e-od-S00000001-100000-00004.ts?rlimit=3&sign=5051edc98f5e1fe13be3c2b51fe6ee23&t=6096b80c&us=1620475852702_6595_1000"
    # index = urls.find("?")
    # #srt = replaceString(urls, index - 8,8, 'a')
    # strUlr = urls[index-8:index]
    # path = entrySavePath.get()+"\\" + entryChapterName.get()+"\\" + entrySectionName.get()
    # # path = "D:/Users/Desktop/会计实操课程/会计必备基础知识(选修)/一、会计科目具体应用/2.复式借贷记账法/"
    # videoName = entryVideoName.get()
    # # videoName = "（2）记账规则与会计分录"

def saveFile(i,path,url):
    # for i in range(1,100000000):
    s = str(i)
    while len(s) < 5:
        s = "0" + s
    # print(s)
    # url = urls.replace(strUlr, s+".ts")
    zhiliaos(s,url,path)


def zhiliaos(i,url,path):
    #print(i)
    html = requests.get(url)
    html.encoding = 'utf-8'
    # html_gy = html.text
    # bf = BeautifulSoup(html_gy, 'html.parser',from_encoding='utf-8')
    # box_row_url = bf.find_all(class_="Box-row")
    headers = {}
    ret = html.content
    #videoName = ""

    isexists_dir_Create("", path)
    path = path+"{}.ts".format(i)
    print(path)
    with open(path, 'wb') as f:
        f.write(ret)
        # r = os.path.getsize(path) # 获取文件大小
    return 1
    #print(html_gy)
'''
    判断文件是否存在，存在无效果，不存在则生成文件夹
    path:路径的绝对路径，通过获取当前文件的绝对路径，再将文件夹文件拼接起来
'''
def isexists_dir_Create(self,path):
    if not os.path.exists(path):
        os.makedirs(path)

# 删除目录下制定后缀的文件
def removeFile(path,type_extension):
    filelist = os.listdir(path)
    for file in filelist:
        filepath = os.path.join(path,file)
        if os.path.isdir(filepath):
            removeFile(filepath,type_extension)
        else:
            if os.path.splitext(filepath)[1]==type_extension:
                os.remove(filepath)

# 替换字符串里的第N个字符
def replaceString(string, startNum,countNum, replace):
    string2 = ''
    for i in range(len(string)):
        if i == startNum:
            for j in range(countNum):
                string2 += replace
                i = i+1
                print(i)
                print(string[i])
        else:
            string2 += string[i]

    return string2

if __name__ == '__main__':
    main()

# # 创建窗口
# root = Tk()
# #标题
# root.title('视频下载')
# # 窗口大小
# root.geometry('540x300')
# # 窗口位置
# root.geometry('+600+300')
# # 标签控件
# label = Label(root,text = '请输入链接：',font = ('华文行楷',18),fg = 'red')
# label.grid()
# # 输入框
# entry = Entry(root,font = ('微软雅黑',20),width = 500)
# entry.grid(row = 0,column = 1)
#
# # 保存路径
# labelSavePath = Label(root,text = '请输入路径：',font = ('华文行楷',18),fg = 'red')
# labelSavePath.grid()
# # 输入框
# entrySavePath = Entry(root,font = ('微软雅黑',20),width = 500)
# entrySavePath.grid(row = 1,column = 1)
#
# # 章节名称
# labelChapterName= Label(root,text = '请输入章节名称：',font = ('华文行楷',18),fg = 'red')
# labelChapterName.grid()
# # 输入框
# entryChapterName = Entry(root,font = ('微软雅黑',20),width = 500)
# entryChapterName.grid(row = 2,column = 1)
#
# # 小节名称
# labelSectionName= Label(root,text = '请输入小节名称：',font = ('华文行楷',18),fg = 'red')
# labelSectionName.grid()
# # 输入框
# entrySectionName = Entry(root,font = ('微软雅黑',20),width = 500)
# entrySectionName.grid(row = 3,column = 1)
#
# # 视频名称
# labelVideoName = Label(root,text = '请输入视频名称：',font = ('华文行楷',18),fg = 'red')
# labelVideoName.grid()
# # 输入框
# entryVideoName = Entry(root,font = ('微软雅黑',20),width = 500,xscrollcommand='true')
# entryVideoName.grid(row = 4,column = 1)
#
#
#
# # 点击按钮
# button = Button(root,height='1',width='7',relief='ridge',fg='blue',text = '开始',font = ('微软雅黑',15),command = startLoading)
# button.grid(row = 5,column = 0)
#
# # 应用程序过程输出
# entryOutput = Entry(root,font = ('微软雅黑',9),width = 500)
# entryOutput.grid(row = 6,column = 1)
# # 消息循环  显示窗口
# root.mainloop()