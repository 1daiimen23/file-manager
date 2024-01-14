from tkinter import*
import os

def dir():
    dir_list = os.listdir(current_path)

    i = 0

    for item in dir_list:
        if os.path.isdir(str(current_path) + '/' + str(item)):
            photo = PhotoImage(file="IMAGE/folder.png")

            icon = Label(image=photo, bg='white')
            icon.image = photo
            icon.grid(row=i+1, column=0)
            folder_name = Label(text=item, bg='white')
            folder_name.grid(row=i + 1, column=1, sticky='w')
            one_row.append(item)
    for j in one_row:
        b = (j + ' ' + "Папка").split()
        file_list.append(b)
        i +=1
    print(file_list)

win = Tk()

win.title("Файловый менеджер")
win.geometry("600x600")

current_path = "C:/"

file_list = []
one_row = []
columns = ("name", "type")
dir()
tree = Treeview()

win.mainloop()