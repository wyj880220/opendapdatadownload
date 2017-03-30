#encoding:utf-8
import requests
import re
import time
import requestdownload
def getchildlink(url):
        try:
            linksall=[]
            data=requests.get(url)
            content=data.text
            link_pat=re.compile(r'<td align="left">[\S\s]*?<a href="(.*?)">.*?</a>[\S\s]*?</td>',re.S)
            links=set(re.findall(link_pat,content))
            linkl=list(links)
            if 'stnd_header.html' in linkl:
                # linkl.
                # print('zai')
                linkl.remove(u"stnd_header.html")
                # print(linkl)
            if 'stnd_footer.html' in linkl:
                linkl.remove(u"stnd_footer.html")
            # print(linkl)

            for l in linkl:
                # print(l)
                if l.split('/')[-1]=='contents.html':
                    # print(url+l.split('/')[0])
                    getchildlink(url+l.split('/')[0]+'/')
                else:
                    downloadlink=url+l
                    # linksall.append(downloadlink)
                    if downloadlink.find('.html')>0:
                        end=downloadlink.find('.html')
                        downloadlink=downloadlink[0:end]
                    print(downloadlink)
                # linksall.append("http://data.nodc.noaa.gov/opendap/"+l)
                #     linksall.append(downloadlink)
                    with open('download'+'.txt','a') as f:
                        f.write(downloadlink+'\n')
            # print(link)
            # return linksall
        except Exception,e:
            print(e)
if __name__ == '__main__':
    # link=getchildlink('http://data.nodc.noaa.gov/opendap/woa/WOA13/')
    file = open("download.txt")
    i=0
    while 1:
        i=i+1
        line = file.readline()
        # print i
        # if line=='\n' or line=='':
        #     print('this is an empty line')
        #     break
        if i%1000==0:
            time.sleep(90)
        line=line.strip('\n')
        # print(line)
        if not line:
            break
        oldlink="http://data.nodc.noaa.gov/opendap/"
        savelink="/home/msdcdatasdb/"
        requestdownload.downloadopdata(line,oldlink,savelink)

    print 'All is Finished,please check the directory'
    # for i in link:
    #     oldlink="http://data.nodc.noaa.gov/opendap/"
    #     savelink="E:/"
    #     requestdownload.downloadopdata(i,oldlink,savelink)
