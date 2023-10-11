# Напишите функцию группового переименования файлов. Она должна:
# 1 принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# 2 принимать параметр количество цифр в порядковом номере.
# 3 принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# 4 принимать параметр расширение конечного файла.
# 5 принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.


import os

def files_rename(signature_name: str, digits_num: int, source_ext: str, new_ext: str, range_num=None):
    files = [f.split(source_ext)[0] for f in os.listdir() if os.path.isfile(f) and f.endswith(source_ext)]

    if not files:
        print('Файлов с данным расширением не найдено')
        return

    for i, file in enumerate(files, 1):
        base = file
        if range_num:
            start, end = range_num
            base = file[start - 1: end]

        new_name = base + signature_name + f'{i:0{digits_num}}' + new_ext

        os.rename(f'{file}{source_ext}', new_name)
        print(f'{file} to {new_name}')

files_rename('_new', 0, '.txt', '.doc')