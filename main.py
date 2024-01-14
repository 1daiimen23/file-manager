from tkinter import *
from tkinter import simpledialog
import os, subprocess
import shutil


class Context_menu(Menu):
    ''' Контекстное меню для внутренней области директории'''

    def __init__(self, main_window, parent):
        super(Context_menu, self).__init__(parent, tearoff=0)
        self.main_window = main_window
        self.add_command(label="Создать папку", command=self.create_dir())
        self.add_command(label="Создать файл", command=self.create_dir())

    def popup_menu(self, event):
        ''' функция для активации контекстного меню'''
        # если активны другие меню - отменяем их
        if self.main_window.file_context_menu:
            self.main_window.file_context_menu.unpost()
        if self.main_window.dir_context_menu:
            self.main_window.dir_context_menu.unpost()
        self.post(event.x_root, event.y_root)

    '''
    def win_of_create(self):
        global ent, win
        win = Tk()

        win.geometry("200x50")
        win.resizable(False, False)

        ent = Entry(win)
        ent.grid(row=1, column=1, padx=5, pady=5)

        ok_btn = Button(win, text="Создать", command=self.create_dir)
        ok_btn.grid(row=1, column=2, padx=5, pady=5)

        win.mainloop()
    '''

    def create_dir(self):
        pass
        dirname = simpledialog.askstring("Имя папки", "Введите имя директории")
        command = "mkdir {0}".format(dirname).split(' ')
        process = subprocess.Popen(command, cwd=path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()



    def create_file(self):
        print("File")
        win.destroy()

    def insert_to_dir(self):
        pass


class File_сontext_menu(Menu):
    def __init__(self, main_window, parent):
        super(File_сontext_menu, self).__init__(parent, tearoff=0)
        self.main_window = main_window
        self.add_command(label="Открыть", command=self.open_file)
        self.add_command(label="Копировать", command=self.copy_file)
        self.add_command(label="Переименовать", command=self.rename_file)
        self.add_command(label="Удалить", command=self.delete_file)

    def open_file(self):
        pass
        file = filedialog.askopenfilename()
        os.startfile(file)


    def copy_file(self):
        pass
        for f in files_list:
            shutil.copy(f, desdir)

    def delete_file(self):
        pass

    def rename_file(self):
        pass

    def popup_menu(self, event):
        ''' функция для активации контекстного меню'''
        self.post(event.x_root, event.y_root)
        # если активны другие меню - отменяем их
        if self.main_window.main_context_menu:
            self.main_window.main_context_menu.unpost()
        if self.main_window.dir_context_menu:
            self.main_window.dir_context_menu.unpost()
        self.main_window.selected_file = event.widget["text"]


class Dir_context_menu(Menu):
    def __init__(self, main_window, parent):
        super(Dir_context_menu, self).__init__(parent, tearoff=0)
        self.main_window = main_window
        self.add_command(label="Переименовать", command=self.rename_dir)
        self.add_command(label="Копировать", command=self.copy_dir)
        self.add_command(label="Удалить", command=self.delete_dir)

    def copy_dir(self):
        pass

    def delete_dir(self, event):
        elem = event.widget
        dir_name = elem["text"]
        os.rmdir(dir_name)

    def change():
        new_name = vvod.get()
        dir = os.path.dirname(path)
        renamed = os.path.join(dir, new_name)
        os.rename(path, renamed)
        win.destroy()

    def rename_dir(self):
        pass
        global vvod, path, win

        path = os.path.abspath(dir)

        win = Frame(app, background='grey')
        win.grid(row=6, column=2)
        Label(win, text="folder name").grid(row=0, column=1, padx=10, pady=10)

        vvod = Entry(win)
        vvod.grid(row=1, column=1, padx=10, pady=10)

        ok_btn = Button(win, text="Ок", command=self.change).grid(row=2, column=2, padx=10, pady=10)

        win.mainloop()

    def popup_menu(self, event):
        ''' функция для активации контекстного меню'''
        self.post(event.x_root, event.y_root)
        # если активны другие меню - отменяем их
        if self.main_window.main_context_menu:
            self.main_window.main_context_menu.unpost()
        if self.main_window.file_context_menu:
            self.main_window.file_context_menu.unpost()
        self.main_window.selected_file = event.widget["text"]


class Win():

    def __init__(self):
        self.root = Tk()
        self.root.title("Файловый менеджер")
        self.root.resizable(width=False, height=False)
        self.root.geometry('450x300')

        self.hidden_dir = IntVar()
        self.buff = None
        self.all_program = os.listdir('C:/')

        self.root.bind('<Button-1>', self.root_click)
        self.root.bind('<FocusOut>', self.root_click)

        # frame всего окна
        self.title_fr = Frame(self.root)
        self.title_fr.pack(fill='both', expand=True)

        # back button
        self.back_button = Button(self.title_fr, text="Назад", command=self.back, width=5, height=1)
        self.back_button.pack(side='left')

        # path entry
        self.path_text = StringVar()
        self.path_text.set('C:/')
        self.current_path = Entry(self.title_fr, textvariable=self.path_text, width=40, state='readonly')
        self.current_path.pack(side='left')

        # button show/hidde hidden dir/file
        self.check_button = Checkbutton(self.title_fr, text="Hidden", font=("Helvetica", 10), padx=1, pady=1,
                                        variable=self.hidden_dir, command=self.refresh_window)
        self.check_button.pack(side='left')

        # main frame
        self.main_frame = Frame(self.root)
        self.main_frame.pack()

        # scroll bar
        self.scrollbar_vert = Scrollbar(self.main_frame, orient="vertical")
        self.scrollbar_vert.pack(side='right', fill='y')

        self.scrollbar_hor = Scrollbar(self.main_frame, orient="horizontal")
        self.scrollbar_hor.pack(side='bottom', fill='x')

        # canvas для отображения каталогов
        self.canvas = Canvas(self.main_frame, borderwidth=0, bg='white')
        self.inner_frame = Frame(self.canvas, bg='white')

        # команды для прокрутки
        self.scrollbar_vert["command"] = self.canvas.yview
        self.scrollbar_hor["command"] = self.canvas.xview

        self.canvas.configure(yscrollcommand=self.scrollbar_vert.set, xscrollcommand=self.scrollbar_hor.set, width=400, heigh=250)

        self.canvas.pack(side='left', fill='both', expand=True)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        # отрисовываем содержимое лиректории
        self.dir_content()

    def back(self):
        new_path = path[:len(path)-1]
        self.path_text.set(path[:new_path.rfind('/')+1])
        self.refresh_window()


    def root_click(self, event):
        ''' функция для обработки события клика в root'''
        # если есть контекстные меню - отменяем
        if self.file_context_menu:
            self.file_context_menu.unpost()
        if self.main_context_menu:
            self.main_context_menu.unpost()
        if self.dir_context_menu:
            self.dir_context_menu.unpost()

    def dir_content(self):
        global path
        dir_list = os.listdir(self.path_text.get())  # список папок и файлов из текущего каталога
        path = self.path_text.get()

        if not dir_list:
            # общее контекстное меню
            self.main_context_menu = Context_menu(self, self.canvas)
            self.canvas.bind('<Button-3>', self.main_context_menu.popup_menu)
            if self.buff:
                self.main_context_menu.add_command(label="Вставить", command=self.main_context_menu.insert_to_dir)
            self.inner_frame.bind('<Button-3>', self.main_context_menu.popup_menu)
            # контекстное меню для файлов
            self.file_context_menu = None
            # контекстное меню для директории
            self.dir_context_menu = None
            return None

        # общее контекстное меню
        self.main_context_menu = Context_menu(self, self.canvas)
        self.canvas.bind('<Button-3>', self.main_context_menu.popup_menu)
        if self.buff:
            self.main_context_menu.add_command(label="Вставить", command=self.main_context_menu.insert_to_dir)
        # контекстное меню для файлов
        self.file_context_menu = File_сontext_menu(self, self.inner_frame)
        # контекстное меню для директории
        self.dir_context_menu = Dir_context_menu(self, self.inner_frame)

        i = 0
        for item in dir_list:

            if os.path.isdir(str(path) + item):
                # обрабатываем директории
                if os.access(str(path) + item, os.R_OK):
                    if (not self.hidden_dir.get() and not item.startswith('.')) or self.hidden_dir.get():
                        photo = PhotoImage(file="IMAGE/folder.png")

                        icon = Label(self.inner_frame, image=photo, bg='white')
                        icon.image = photo
                        icon.grid(row=i + 1, column=0)

                        folder_name = Label(self.inner_frame, text=item, bg='white')
                        folder_name.bind("<Button-1>", self.move_to_dir)
                        folder_name.bind("<Button-3>", self.dir_context_menu.popup_menu)
                        folder_name.grid(row=i + 1, column=1, sticky='w')
                else:
                    if (not self.hidden_dir.get() and not item.startswith('.')) or self.hidden_dir.get():
                        photo = PhotoImage(file="img/folder_access.png")

                        icon = Label(self.inner_frame, image=photo, bg='white')
                        icon.image = photo
                        icon.grid(row=i + 1, column=0)

                        folder_name = Label(self.inner_frame, text=item, bg='white')
                        folder_name.bind("<Button-1>", self.move_to_dir)
                        folder_name.grid(row=i + 1, column=1, sticky='w')

            else:
                # обрабатываем файлы
                if (not self.hidden_dir.get() and not item.startswith('.')) or self.hidden_dir.get():
                    ext = self.take_extention_file(item)
                    # фото, картинки
                    if ext in ['jpeg', 'jpg', 'png', 'gif']:
                        photo = PhotoImage(file="IMAGE/photo.png")

                        icon = Label(self.inner_frame, image=photo, bg='white')
                        icon.image = photo
                        icon.grid(row=i + 1, column=0)

                        file_name = Label(self.inner_frame, text=item, bg='white')
                        file_name.grid(row=i + 1, column=1, sticky='w')

                        file_name.bind("<Button-3>", self.file_context_menu.popup_menu)
                    else:
                        # другие файлы
                        if os.access(str(path) + item, os.R_OK):
                            photo = PhotoImage(file="IMAGE/file.png")

                            icon = Label(self.inner_frame, image=photo, bg='white')
                            icon.image = photo
                            icon.grid(row=i + 1, column=0)

                            folder_name = Label(self.inner_frame, text=item, bg='white')
                            folder_name.grid(row=i + 1, column=1, sticky='w')

                            folder_name.bind("<Button-3>", self.file_context_menu.popup_menu)

                        else:
                            photo = PhotoImage(file="IMAGE/file_access.png")

                            icon = Label(self.inner_frame, image=photo, bg='white')
                            icon.image = photo
                            icon.grid(row=i + 1, column=0)

                            folder_name = Label(self.inner_frame, text=item, bg='white')
                            folder_name.grid(row=i + 1, column=1, sticky='w')
            i += 1
        # обновляем inner_frame и устанавливаем прокрутку для нового содержимого
        self.inner_frame.update()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def move_to_dir(self, event):
        ''' функция для перехода в выбранную директорию'''
        elem = event.widget
        dir_name = elem["text"]
        fool_path = self.path_text.get() + dir_name
        if os.path.isdir(fool_path) and os.access(fool_path, os.R_OK):
            old_path = self.path_text.get()
            self.path_text.set(old_path + dir_name + '/')
            self.root_click('<Button-1>')
            self.refresh_window()

    def parent_dir(self):
        pass

    def take_extention_file(self, file_name):
        ''' функция для получения расширения файла'''
        ls = file_name.split('.')
        if len(ls) > 1:
            return ls[-1]
        else:
            return None

    def refresh_window(self):
        ''' функция для обновления текущего отображения директорий/файлов'''
        for widget in self.inner_frame.winfo_children():
            widget.destroy()
        self.dir_content()
        self.canvas.yview_moveto(0)


vin = Win()

vin.root.mainloop()