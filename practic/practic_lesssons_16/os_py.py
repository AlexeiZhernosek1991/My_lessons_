import shutil
import os

dir_file = r'C:\Users\Alex\Downloads'
dir_sort = r'D:\sort'
dict_dir = {
    'image': ['png', 'jpeg', 'gif', 'raw', 'tiff', 'bmp', 'psd'],
    'text': ['txt', 'rtf', 'doc', 'docx', 'xls', 'xlcx', 'pptx', 'pdf'],
    'web': ['htm', 'html'],
    'audio': ['wav', 'mp3', 'midi', 'kar', 'ogg'],
    'archive': ['rar', 'zip', 'arj'],
    'exe_file': ['exe', 'com'],
    'video': ['avi', 'flv', 'mp4', '3gp', 'wmv', 'wedm', 'mpeg', 'mov', 'dvd']
}


def sort_file(dir_file, dir_sort, dict_dir):
    list_newfile = os.listdir(dir_file)
    if list_newfile != []:
        for file_ in list_newfile:
            type_file = file_[file_.find('.') + 1:]
            for dir_ in dict_dir:
                if type_file in dict_dir[dir_]:
                    print(f' файл {file_} перемещен в папку {dir_}')
                    shutil.move(dir_file + '\\' + file_, dir_sort + '\\' + dir_)
                    break
                else:
                    pass
            else:
                print(f' файл {file_} перемещен в папку other file')
                shutil.move(dir_file + '\\' + file_, dir_sort + '\\' + 'other file')
    else:
        print('Нет новых файлов')


sort_file(dir_file, dir_sort, dict_dir)

