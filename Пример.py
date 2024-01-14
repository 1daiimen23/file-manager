from tkinter import *
import os
from tkinter import messagebox, filedialog, ttk
from tkinter import messagebox as mb
import shutil

def open_file():
    file = filedialog.askopenfilename()
    os.startfile(file)
    messagebox.showinfo(message=file + " открыт")

def delete_file():
    file = filedialog.askopenfilename()
    os.remove(file)
    messagebox.showinfo(file, "был удален")

def change_name():
    file_name = ent.get()
    dir = os.path.dirname(path)
    new_name = os.path.join(dir, file_name)
    os.rename(path, new_name)
    fr.destroy()

def rename_file():
    global ent, path, fr
    file = filedialog.askopenfilename()
    path = os.path.abspath(file)
    fr = Frame(app, bg="grey")
    fr.grid(row=6, column=2)
    ent = Entry(fr)
    ent.grid(row=1, column=1)
    ok_button = Button(fr, text="Сохранить", command=change_name)
    ok_button.grid(row=2, column=1)
    cancel_button = Button(fr, text="Отменить", command=fr.destroy)
    cancel_button.grid(row=2, column=2)
    fr.mainloop()

def browse():
    global files_list
    files_list = list(filedialog.askopenfilenames())
    sourceText.insert('1', files_list)

def browse2():
    directoryy = filedialog.askdirectory()
    destinationText.insert('1', directoryy)

def copy_file():
    desdir = destination_location.get()
    for f in files_list:
        shutil.copy(f, desdir)
    messagebox.showinfo("Все ок")

def move_file():
    desdir = destination_location.get()
    for f in files_list:
        shutil.move(f, desdir)
    messagebox.showinfo("Все ок")

def copy_move_file():
    global sourceText, destinationText, destination_location, f1
    f1 = Frame(app, width=350, height=300, background="lavender")
    f1.grid(row=5, column=0, columnspan=4)

    source_location = StringVar()
    destination_location = StringVar()

    link_Label = Label(f1, text="Select The File To Copy ", font="bold", bg='lavender')
    link_Label.grid(row=0, column=0, pady=5, padx=5)

    sourceText = Entry(f1, width=50, textvariable=source_location, font="12")
    sourceText.grid(row=0, column=1, pady=5, padx=5)
    source_browseButton = Button(f1, text="Browse",bg='cyan2', width=15, font="bold", command=browse)
    source_browseButton.grid(row=0, column=2, pady=5, padx=5)

    destinationLabel = Label(f1, text="Select The Destination", bg="lavender", font="bold")
    destinationLabel.grid(row=1, column=0, pady=5, padx=5)

    destinationText = Entry(f1, width=50, textvariable=destination_location, font=12)
    destinationText.grid(row=1, column=1, pady=5, padx=5)
    dest_browseButton = Button(f1, text="Browse", bg='cyan2', width=15, font="12", command=browse2)
    dest_browseButton.grid(row=1, column=2, pady=5, padx=5)

    copyButton = Button(f1, text="Copy File", bg='dark green',fg='white', width=15, font=('bold',12), command=copy_file)
    copyButton.grid(row=2, column=0, pady=10, padx=10)

    moveButton = Button(f1, text="Move File", bg='dark green',fg='white', width=15, font=('bold',12), command=move_file)
    moveButton.grid(row=2, column=1, pady=10, padx=10)

    cancelButton = Button(f1, text="Cancel",bg='red2',fg='white', command= f1.destroy, width=15, font=('bold',12))
    cancelButton.grid(row=2, column=2, pady=10, padx=10)

def browse_folder():
    global folder_list
    directory = filedialog.askdirectory()
    folder_list = os.listdir()
    ent1.insert(0, directory)

def browse_folder2():
    directory = filedialog.askdirectory()
    ent2.insert(0, directory)

def delete_folder():
    directory = filedialog.askdirectory()
    if mb.askyesno(message="Удалить данную папку?"):
        shutil.rmtree(directory)
        messagebox.showinfo(message="Папка успешно удалена!")

def copy_folder():
    dir1 = ent1.get()
    dir2 = ent2.get()
    shutil.copy(dir1, dir2)
    messagebox.showinfo(message="Папка была успешно скопирована")

def move_folder():
    global folder_list
    folder_list = ent1.get()
    name2 = ent2.get()
    shutil.move(folder_list, name2)
    messagebox.showinfo(message="Папка успешно перемещена")

def look_folder():
    directory = filedialog.askdirectory()
    files = os.listdir(directory)
    fr = Frame(app, bg="white")
    fr.grid(row=3, column=1)
    #files_var = Variable(value=files)
    listbox = Listbox(fr, width=40)
    listbox.grid(row=1, column=1)
    for i in files:
        listbox.insert(0,i)

    fr.mainloop()
def mk_folder():
    def create():
        name_folder = ent4.get()
        os.mkdir(name_folder)

    fr3 = Frame(app, width=500, bg='grey')
    fr3.grid(row=3, column=2)

    directory = filedialog.askdirectory()
    os.chdir(directory)

    label = Label(fr3, text="Имя папки:")
    label.grid(row=3, column=1)

    ent4 = Entry(fr3)
    ent4.grid(row=3, column=2)

    ok_bnt = Button(fr3, text="Ок", command=create)
    ok_bnt.grid(row=3, column=3)

    cancel_btn = Button(fr3, text="Отменить", command=fr3.destroy)
    cancel_btn.grid(row=3, column=4)

    fr3.mainloop()

def create_folder():
    global ent5, dir
    dir = filedialog.askdirectory()
    fr = Frame(app, bg="white")
    fr.grid(row=6, column=1)
    ent5 = Entry(fr, width=20)
    ent5.grid(row=1, column=1)
    btn = Button(fr, text="Создать")
    btn.grid(row=1, column=2)
    fr.mainloop()

def make_folder():
    name = ent5.get()
    os.chdir(dir)
    os.makedirs(name)
    fr.destroy()

def rename_folder():
    global vvod, path, win
    dir = filedialog.askdirectory()
    path = os.path.abspath(dir)

    win = Frame(app, background='grey')
    win.grid(row=6, column=2)
    Label(win, text ="folder name").grid(row = 0, column=1,padx = 10, pady=10)

    vvod = Entry(win)
    vvod.grid(row=1, column=1,padx=10, pady=10)

    ok_btn = Button(win, text="Ок", command=change_folder).grid(row=2, column=2, padx=10, pady=10)

    win.mainloop()

def change_folder():
    new_name = vvod.get()
    dir = os.path.dirname(path)
    renamed = os.path.join(dir, new_name)
    os.rename(path, renamed)
    win.destroy()

def copy_move_folder():
    global directory, ent1, ent2

    fr2 = Frame(app, width=1000, height=1000, bg="light blue")
    fr2.grid(row=6, column=2)

    ent1 = Entry(fr2, width=30, font=('Times New Roman', 14))
    ent1.grid(row=1, column=1, padx=5, pady=5)

    ent2 = Entry(fr2, width=30, font=('Times New Roman', 14))
    ent2.grid(row=2, column=1, padx=5, pady=5)

    browse = Button(fr2, text="Выбрать", command=browse_folder, width=10, font=('Times New Roman', 10), bg="dark salmon")
    browse.grid(row=1, column=2, padx=5, pady=5)

    browse2_button = Button(fr2, text="Выбрать", command=browse_folder2, width=10, font=('Times New Roman', 10), bg="dark khaki")
    browse2_button.grid(row=2, column=2, padx=5, pady=5)

    copy_button = Button(fr2, text="Копировать", width=10, font=('Times New Roman', 10), command=copy_folder)
    copy_button.grid(row=3, column=1, padx=5, pady=5)

    move_button = Button(fr2, text="Переместить", width=10, font=('Times New Roman', 10), command=move_folder)
    move_button.grid(row=3, column=2, padx=5, pady=5)

    cancel_button = Button(fr2, text="Отменить", command=fr2.destroy, width=10, font=('Times New Roman', 10), bg="dark red", fg="white")
    cancel_button.grid(row=3, column=3, padx=5, pady=5)

    fr2.mainloop()


app = Tk()

app.title("Файловый менеджер")
app.attributes("-fullscreen", True)


open_button = Button(text="Открыть файла", command=open_file, width=15)
open_button.grid(row=1, column=1, padx=20, pady=20)

delete_button = Button(text="Удалить файл", command=delete_file, width=15)
delete_button.grid(row=1, column=2, padx=20, pady=20)

rename_button = Button(text="Для папок", command=rename_file, width=15)
rename_button.grid(row=1, column=3, padx=20, pady=20)

choose_button = Button(text="Выбрать файл", command=copy_move_file, width=15)
choose_button.grid(row=1, column=4, padx=20, pady=20)

delete_folder_btn = Button(text="Удалить папку", command=delete_folder, width=15)
delete_folder_btn.grid(row=2, column=1)

create_folder_btn = Button(text="Создать папку", command=mk_folder, width=15)
create_folder_btn.grid(row=2, column=2)

rename_folder_btn = Button(text="Переименовать папку", command=rename_folder, width=15)
rename_folder_btn.grid(row=2, column=3)

copy_move_folder_btn = Button(text="Коп, перем", command=copy_move_folder, width=15)
copy_move_folder_btn.grid(row=2, column=4)

look_btn = Button(text="Содержимое папки", command=look_folder)
look_btn.grid(row=2, column=5)

app.mainloop()