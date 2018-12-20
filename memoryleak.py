import psutil
import threading
import time

import __main__


def monitor_memory(log=False):
    import os
    import psutil
    process = psutil.Process(os.getpid())
    limit = 90
    highest_memory_usage = 0
    p = psutil.Process(__main__.os.getpid())
    while 1:
        percent = psutil.virtual_memory()[2]
        if percent > limit:
            print("Memory usage over {}.".format(limit))
            p.terminate()

        if log:
            memory_usage = p.memory_info().rss
            if memory_usage > highest_memory_usage:
                highest_memory_usage = memory_usage
                with open("memoryleak.log", "w") as f:
                    f.write("Highest memory usage: {}".format(memory_usage))

        time.sleep(1)


t = threading.Thread(target=monitor_memory)
t.daemon = True
t.start()
