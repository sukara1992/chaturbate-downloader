import os
import multiprocessing
import sys
import time
def download(url):
    try:
        while True:
            print("正在下载"+url+"上面的视频")
            a=os.system("youtube-dl" + " " + url + " " + "--config-location ./config.txt ")
            print(a)
            #print(url+"执行完了")
            # 十分钟后再次执行
            time.sleep(600);
        return True
    except KeyboardInterrupt:
        sys.exit(1)
if __name__ == '__main__':
    baseurl="https://zh.chaturbate.com/"
    names=["annabellasweet98","kishorny_99","aimilu","diamond_jackson","chinesesweety"]
    fullurls=map(lambda x:baseurl+x, names)
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    for fullurl in fullurls:
        pool.apply_async(download,args=(fullurl,))
    pool.close()
    pool.join()

