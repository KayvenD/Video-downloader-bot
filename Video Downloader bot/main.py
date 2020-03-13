

from webtools import download_media
from fstool import collection_management
from mptool import multithread
from timelog import watcher


########################################################################
##*** Multithread Scenario

watcher.start_time()
## setup
biglist = collection_management.getlist_from_a_file("downloadlist.txt")

def task():
    while True:
        if (biglist):
            __popitem = collection_management.poplist(biglist)
            download_media.video(__popitem)
        else:
            break

multithread.run(task,10)   ## multithreading
watcher.end_time()
