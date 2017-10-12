import re
import urllib
import os
import time

'''
This is the simplest grab tools
'''

'''
I am in Task1 branch
'''


# url_all=['http://www.bing.com/images/search?q=%E6%85%B5%E6%87%92%E5%B0%91%E5%A5%B3%E5%86%99%E7%9C%9F&form=ISTRTH&id=A87C17F9A484F4078C72BEB0FE1EC509BA1F59C8&cat=%E7%BE%8E%E5%A5%B3&mkt=zh-CN&first=1&cw=1588&ch=843']
url_all=['http://site.6park.com/chan8/index.php?app=forum&act=threadview&tid=13893663'
         '']

def schedule(a,b,c):
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print '%.2f%%' % per


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getImage(html):
    reg = r'src="(.*?\.jpg)"'
    # reg = r'src="http://pic.+" />'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist


for i in range(len(url_all)):
    html=getHtml(url_all[i])
    list1=getImage(html)

    t = time.localtime(time.time())
    foldername = str(t.__getattribute__("tm_year"))+"-"+str(t.__getattribute__("tm_mon"))+"-"+str(t.__getattribute__("tm_mday")+i)
    picpath = 'E:\\ImageDownload\\%s' % (foldername)

    if not os.path.exists(picpath):
        os.makedirs(picpath)

    x=0
    for imgurl in list1:
        target = picpath+'\\%s.jpg' % x
        urllib.urlretrieve(imgurl,target,schedule)
        print 'Downloading image to location: ' + target + '\nurl=' + imgurl
        x+=1

