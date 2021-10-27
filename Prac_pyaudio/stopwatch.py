import time

def get_time():
    start = time.time()
    print("start: ", start,"\n")
    end = time.time()

    print(end-start)
    print(time.ctime(end-start))


get_time()
