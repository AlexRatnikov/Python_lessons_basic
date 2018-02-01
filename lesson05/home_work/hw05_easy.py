# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os

def create_dirs():
    try:
        for i in range(1, 10):
            name = "dir_" + str(i)
            dir_path = os.path.join(os.getcwd(), name)
            os.mkdir(dir_path)
            name.replace(str(i), str(i+1))
    except FileExistsError:
        print('The directories are exist already!')

def remove_dirs():
    try:
        for i in range(1, 10):
            name = "dir_" + str(i)
            dir_path = os.path.join(os.getcwd(), name)
            os.rmdir(dir_path)
            name.replace(str(i), str(i + 1))
    except FileNotFoundError:
        print('Cannot find directories to delete. Probably, nothing to delete!')

create_dirs()
# remove_dirs()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def show_me_all_dirs_here():
    print(sorted([d for d in os.listdir() if os.path.isdir(d)]))

show_me_all_dirs_here()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_me():
    scr_path = os.getcwd()
    if os.name == "posix":
        os.system("cp " + scr_path + "/hw05_easy.py "+scr_path+"/hw05_easy_copy.py")
        print("You are working on MacOs. File was copied.")
    elif os.name == "nt":
        os.system("copy " + scr_path + "/hw05_easy.py " + scr_path + "/hw05_easy_copy.py")
        print("You are working on Windows. File was copied.")

copy_me()