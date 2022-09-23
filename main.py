from flickr import get_urls
from downloader import download_images
import os
import time

all_cameras = ['iphone 11', 'iphone 12']
images_per_cameras = 30

def download():
    for photo in all_cameras:

        print('Getting urls for', photo)
        urls = get_urls(photo, images_per_cameras)

        print('Downlaing images for', photo)
        path = os.path.join('data', photo)

        download_images(urls, path)

if __name__=='__main__':

    start_time = time.time()

    download()

    print('Took', round(time.time() - start_time, 2), 'seconds')
