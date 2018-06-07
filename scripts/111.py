import time

import sys


def load_get():
    loading_start = "../Image/"
    now_time = time.strftime("%Y_%m_%d %H_%M_%S")
    loading_end = "--" + sys.exc_info()[1] + ".jpg"
    loading_file = loading_start + now_time+ loading_end
    return loading_file

print(load_get())