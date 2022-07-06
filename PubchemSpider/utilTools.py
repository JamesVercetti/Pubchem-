

#下载文件
def download_file(url, file_dir,Suffix):
    list=url.split("=")
    filename=list[len(list)-1]+Suffix
    from requests import get
    reply = get(url, stream=True)
    file=open(file_dir+"\\"+filename, 'wb')
    for chunk in reply.iter_content(chunk_size=1024):
        if chunk:
            file.write(chunk)
    file.close()

#记录日志信息
def writeLog(filename,file_dir,log_id):
    f=open(filename,"w+",encoding="utf-8")
    f.write(file_dir+":"+log_id)
    f.close()