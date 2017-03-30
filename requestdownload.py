#encoding:utf-8
from __future__ import print_function
from contextlib import closing
import requests
import emailsend
import os
class ProgressBar(object):
    def __init__(self, title,
                 count=0.0,
                 run_status=None,
                 fin_status=None,
                 total=100.0,
                 unit='', sep='/',
                 chunk_size=1.0):
        super(ProgressBar, self).__init__()
        self.info = "[%s] %s %.2f %s"
        self.title = title
        self.total = total
        self.count = count
        self.chunk_size = chunk_size
        self.status = run_status or ""
        self.fin_status = fin_status or " " * len(self.status)
        self.unit = unit
        self.seq = sep

    def __get_info(self):
        _info = self.info % (self.title, self.status,
                             self.count/self.chunk_size, self.unit)
        return _info

    def refresh(self, count=1, status=None):
        self.count += count
        # if status is not None:
        self.status = status or self.status
        end_str = "\r"
        if self.count >= self.total:
            end_str = '\n'
            self.status = status or self.fin_status
        print(self.__get_info(), end=end_str)
def downloadopdata(urldata,oldlink,savelink):
    savefilelink=urldata.replace(oldlink,savelink)
    filename=urldata.split('/')[-1]
    savedir=savefilelink.replace(filename,'')
    # print(savedir)
    if not os.path.exists(savedir):
        os.makedirs(savedir)
    try:
        with closing(requests.get(urldata,stream=True)) as response:
            chunk_size=1024
            content_size=10000000000000000000

            if response.status_code !=200:
                print('返回码不正确....正在记录....')
                with open('errorcodelink'+'.txt','a') as f:
                        f.write(urldata+'\n')
            else:

                progress=ProgressBar(filename+"数据",total=content_size,unit="KB",chunk_size=chunk_size,run_status="正在下载...",fin_status='下载完成》》')
                with open(savefilelink,"wb") as file:
                    for data in response.iter_content(chunk_size=chunk_size):
                        file.write(data)
                        progress.refresh(count=len(data))
    except:
        print('发生请求错误.....正在记录...')
        with open('errorlink'+'.txt','a') as f:
            f.write(urldata+'\n')
            pass
if __name__ == '__main__':
    urldata="http://data.nodc.noaa.gov/opendap/woa/WOA13/DATA/salinity/csv/A5B2/0.25/woa13_A5B2_s10gp04.csv.gz"
    oldlink="http://data.nodc.noaa.gov/opendap/"
    savelink="D:/"
    downloadopdata(urldata,oldlink,savelink)
