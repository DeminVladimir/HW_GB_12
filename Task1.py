# Создайте функцию для сортировки файлов по директориям:
# видео, изображения, текст и т.п. Каждая группа включает
# файлы с несколькими расширениями. В исходной папке должны
# остаться только те файлы, которые не подошли для сортировки.


import os
import pathlib

def sort_files(path: pathlib.Path, groups=None) -> None:
    os.chdir(path)

    if groups is None:
        groups = {
            pathlib.Path('video'): ['.mp4', '.avi'],
            pathlib.Path('music'): ['.mp3', '.wav', '.wma'],
            pathlib.Path('image'): ['.png', '.jpg' , '.bmp', '.svg', '.pdf'],
            pathlib.Path('text'): ['.txt', '.doc', '.docx']
        }

    for target_dir, extension_list in groups.items():
        if not target_dir.is_dir():
            target_dir.mkdir()

    path_lib = {}

    for keys, values in groups.items():
        for value in values:
            path_lib[value] = keys

    for file in path.iterdir():
        if file.is_file() and file.suffix in path_lib.keys():
            file.replace(path_lib[file.suffix] / file.name)


sort_files(pathlib.Path('C:/Users/user/Desktop/всякое'))