#Напишите функцию группового переименования файлов.

import os
def group_rename(lengnt_c: int, extension: str, new_extension: str, interval: list[int], new_name=''):
    count = 0
    for filename in os.listdir("."):
        if filename.endswith(extension):
            count += 1
            a = str(count)
            os.rename(filename, filename[interval[0]:interval[1]]+new_name+"0"*lengnt_c+a+"."+new_extension)
#group_rename(5, "txt", "exe", (3, 6), "abracadabra")
