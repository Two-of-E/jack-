import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def downloader(img_name,img_url):
    req = urllib.request.urlopen(img_url)

    img_content = req.read()

    with open(img_name, "wb") as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader, "1.jpg","https://rpic.douyucdn.cn/live-cover/roomCover/2018/10/17/c323db33db5fa5f1f9874f240850b3ae_big.jpg"),
        gevent.spawn(downloader, "2.jpg","https://rpic.douyucdn.cn/live-cover/appCovers/2018/10/19/5230163_20181019161115_small.jpg")
    ])



if __name__ == "__main__":
    main()



