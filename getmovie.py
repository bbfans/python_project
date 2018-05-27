import re
import urllib
import os
import time


baseurl = 'http://fromv.ir/vip/Series/Ongoing/Breaking%20Bad/S01/'

url_all = [baseurl]


def schedule(a,b,c):
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print '%.2f%%' % per


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getMovie(html):
    reg = r'href="(.*?\.mkv)"'
    # reg = r'src="http://pic.+" />'
    movie_reg = re.compile(reg)
    movie_list = re.findall(movie_reg,html)
    return movie_list


for i in range(len(url_all)):
    html=getHtml(url_all[i])
    list1=getMovie(html)

    t = time.localtime(time.time())
    foldername = str(t.__getattribute__("tm_year"))+"-"+str(t.__getattribute__("tm_mon"))+"-"+str(t.__getattribute__("tm_mday")+i)
    picpath = 'E:\\ImageDownload\\%s' % (foldername)

    if not os.path.exists(picpath):
        os.makedirs(picpath)

    x=0
    for movie_list in list1:
        target = picpath + movie_list
        movie_url = baseurl + movie_list
        urllib.urlretrieve(movie_url, target, schedule)
        print 'Downloading movie to location: ' + target + '\nurl=' + movie_url
        x+=1

