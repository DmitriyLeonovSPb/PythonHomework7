from FileRenamer import group_rename
from FileMaker import filemaker
from NewFileMaker import newfilemaker
from FillFile import fillfile
from NameGenerator import namegenerator
from pathlib import Path

if __name__ == '__main__':
    fillfile(30, 'test1.txt')
    namegenerator(8, 5, 5, Path('test2.txt'))
    filemaker('txt', count=10)
    data = {
        'txt': 6,
        'zip': 1,
    }
    newfilemaker(data)
    group_rename(5, "txt", "exe", (3, 6), "abracadabra")