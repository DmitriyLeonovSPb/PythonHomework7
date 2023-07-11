#Доработаем предыдущую задачу. Создайте новую функцию которая генерирует файлы с разными расширениями

from FileMaker import filemaker

def newfilemaker(extensions: dict):
    for extension, count in extensions.items():
        filemaker(extension=extension, count=count)