import os, sys, pathlib
import color

try:
    from tkinter import filedialog, Tk
    tkinter_stat=1
except ModuleNotFoundError:
    tkinter_stat=0

class status:
    success = 'Переименование успешно!'
    lose = 'Неверный путь!'

def start():
    cls()
    if os.name=='nt':
        os.system('mode  con: cols=75 lines=20')
    import logo

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit():
    os.system(color.reset)
    sys.exit()

def select_type():
    print('1: Microsoft Word\n2: Фото\n3: Видео\n4: Текстовый документ\n5: PDF\n0: Выход')
    type = input('Выберите тип файлов для переименования: ')
    cls()
    if type == '0':
        exit()
    
    elif type == '1':
        x = ['.doc', '.docx']
    
    elif type == '2':
        x = ['.jpg', '.jpeg', '.png', '.bmp']
    
    elif type == '3':
        x = ['.mp4', '.3gp', '.mpeg', '.avi', '.waw']
    
    elif type == '4':
        x = ['.txt']
    
    elif type == '5':
        x = ['.pdf']
    
    else:
        cls()
        print('Неверный выбор!\n')
        x=select_type()
    return x
	
def select_folder(folder):
    root = Tk()
    root.withdraw()
    old_folder = filedialog.askdirectory(title="Выберите папку с файлами для переименования")
    win_folder = pathlib.Path(old_folder)
    folder = win_folder if os.name == 'nt' else old_folder
    return folder
	
def rename():
    x = select_type()
    name = input('Введите название: ')
    path = input('Введите полный путь: ') if tkinter_stat == 0 else select_folder(None)
    a = str(path)
    if '\\' in a:
        a = a
    elif '/' in a:
        a = a
    else:
        cls()
        print (status.lose)
        exit()
    
    i = 1
    for file_name in os.listdir(path): 
        # Имя файла и его формат 
        base_name, ext = os.path.splitext(file_name) 
        # Нужны файлы определенного формата	
        if ext.lower() not in x:
            continue 
        # Полный путь к текущему файлу 
        abs_file_name = os.path.join(path, file_name) 
        # Полный путь к текущему файлу с новым названием 
        new_abs_file_name = os.path.join(path, str(name) + ".temp." + str(i) + ext)
        os.rename(abs_file_name, new_abs_file_name)
        i += 1
    i = 1
    for file_name in os.listdir(path):
        # Имя файла и его формат
        base_name, ext = os.path.splitext(file_name)
        # Нужны файлы определенного формата
        if ext.lower() not in x:
            continue
        # Полный путь к текущему файлу
        abs_file_name = os.path.join(path, file_name)
        # Полный путь к текущему файлу с новым названием
        new_abs_file_name = os.path.join(path, str(name) + " " + str(i) + ext)
        os.rename(abs_file_name, new_abs_file_name)
        i += 1
		
start()

try:
    rename()
    cls()
    print (status.success)
    exit()
except FileNotFoundError:
    cls()
    print (status.lose)
    exit()
