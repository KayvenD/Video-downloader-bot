import threading


class multithread:
    def run(func, number_of_thread):
        lthreads = []
        for __n in range(number_of_thread):
            tprocess = threading.Timer(__n, func)
            tprocess.start()
            lthreads.append(tprocess)
        for __process in lthreads:
            __process.join()