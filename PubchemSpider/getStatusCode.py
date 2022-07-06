import requests
from selenium import webdriver
import substance
import os
import threading
import time
import utilTools
from selenium.webdriver.chrome.options import Options
#创建隐式Chrome浏览器
def disopenChromeDriver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(options=chrome_options)
    return browser

#检查网址状态，判断是否存在
def checkStatusCode(url):
    r=requests.get(url).status_code
    if r == 404:
        return 404
    else:
        browser=disopenChromeDriver()
        return browser

#爬取主函数
def RunMain(id,seed,save_dir):
    url = seed + id  #链接拼接，id为序号
    leaf_dir = "SID-" + id
    browser = checkStatusCode(url)
    file_dir = save_dir + leaf_dir
    if browser == 404:
        pass
    else:
        try:
            if not os.path.exists(file_dir):
                os.makedirs(file_dir)
                substance.getSpecificInfo(url, browser, file_dir)
                browser.quit()
            print("下载ok")
        except:
            print("error")
            utilTools.writeLog("substanceLog.txt", file_dir, leaf_dir)
            browser.quit()

#读取开始爬取序号
def readStartId(filename):
    f=open(filename,"r",encoding="utf-8")
    startId=f.readline()
    f.close()
    return startId

#写入下次开始序号
def writeStartId(filename,new_startId):
    f=open(filename,"w",encoding="utf-8")
    f.write(new_startId)
    f.close()


def main(thread_num,url_num,seed,save_dir):
    thread_list=[]
    start_id=readStartId("SID.txt").strip("\n")
    for i in range(int(start_id),url_num+1):
        t=threading.Thread(target=RunMain,args=(str(i),seed,save_dir,))
        #加入线性池并启动
        thread_list.append(t)
        t.start()

        #当线性池满了后，等待线程结束
        while len(thread_list)>thread_num:
            thread_list=[x for x in thread_list if x.is_alive()]
            time.sleep(2)
            writeStartId("SID.txt",str(i+1))
        pass

if __name__ == '__main__':
    #   thread_num为线程数
    thread_num = 5
    #   url_num为爬取链接最大序号
    url_num = 80000000
    #种子链接，即主网页
    seed="https://pubchem.ncbi.nlm.nih.gov/substance/"
    #下载文件所存放位置
    save_dir='/home/lhf/saveSubstance1/'
    main(thread_num=thread_num,url_num=url_num,seed=seed,save_dir=save_dir)