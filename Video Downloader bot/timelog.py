import time

class watcher:
    def start_time():
        __start = time.time()
        return __start
    def end_time():
        __end = time.time()
        print("Time taken in seconds : ", __end - watcher.start_time())