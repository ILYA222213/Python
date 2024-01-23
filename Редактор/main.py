from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

# Функция для смены темы
def chenge_theme(theme):
    text_fild['bg'] = view_colors[theme]['text_bg']
    text_fild['fg'] = view_colors[theme]['text_fg']
    text_fild['insertbackground'] = view_colors[theme]['cursor']
    text_fild['selectbackground'] = view_colors[theme]['select_bg']

# Функция для смены шрифта
def chenge_fonts(fontss):
    text_fild['font'] = fonts[fontss]['font']

# Функция для выхода из приложения
def notepad_exit():
    answer = messagebox.askokcancel('Выход', 'Вы точно хотите выйти?')
    if answer:
        root.destroy()

# Функция для открытия файла
def open_file():
    file_path = filedialog.askopenfilename(title='Выбор файла', filetypes=(('Текстовые документы (*.text)', '*.text'), ('Все файлы', '*.*')))
    if file_path:
        text_fild.delete('1.0', END)
        text_fild.insert('1.0', open(file_path, encoding='utf-8').read())

# Функция для сохранения файла
def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы (*.text)', '*.text'), ('Все файлы', '*.*')))
    f = open(file_path, 'w', encoding='utf-8')
    text = text_fild.get('1.0', END)
    f.write(text)
    f.close()

# Создание основного окна
root = Tk()
root.title('Текстовый редактор')
root.geometry('600x700')

# Создание основного меню
main_menu = Menu(root)

# Пункт меню "Файл"
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Открыть', command=open_file)
file_menu.add_command(label='Сохранить', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Закрыть', command=notepad_exit)
root.config(menu=file_menu)

# Пункт меню "Вид"
view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label='Тёмная', command=lambda: chenge_theme('dark'))
view_menu_sub.add_command(label='Светлая', command=lambda: chenge_theme('ligth'))
view_menu.add_cascade(label='Тема', menu=view_menu_sub)

font_menu_sub.add_command(label='Arial', command=lambda: chenge_fonts('Arial'))
font_menu_sub.add_command(label='Comic Sand MS', command=lambda: chenge_fonts('CSMS'))
font_menu_sub.add_command(label='Time New Roman', command=lambda: chenge_fonts('TNR'))
view_menu.add_cascade(label='Шрифт...', menu=font_menu_sub)
root.config(menu=view_menu)

# Добавление пунктов в основное меню
main_menu.add_cascade(label='Файл', menu=file_menu)
main_menu.add_cascade(label='Вид', menu=view_menu)
root.config(menu=main_menu)

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

# Настройки цветов и шрифтов
view_colors = {
    'dark': {
        'text_bg': 'black', 'text_fg': 'lime', 'cursor': 'lime', 'select_bg': '#ff1100'
    },
    'ligth': {
        'text_bg': 'white', 'text_fg': 'black', 'cursor': 'black', 'select_bg': '#FAEEDD'
    }
}

fonts = {
    'Arial': {
        'font': 'Arial 14 bold'
    },
    'CSMS': {
        'font': ('Comic Sans MS', 14, 'bold')
    },
    'TNR': {
        'font': ('Time New Roman', 14, 'bold')
    }
}

# Создание текстового поля
text_fild = Text(f_text,
                 bg='black',
                 fg='lime',
                 padx=10,
                 pady=10,
                 wrap=WORD,
                 insertbackground='lime',
                 selectbackground='#ff1100',
                 spacing3=10,
                 width=30,
                 font='Arial 14 bold'
                 )
text_fild.pack(expand=1, fill=BOTH, side=LEFT)

scroll = Scrollbar(f_text, command=text_fild.yview)
scroll.pack(side=RIGHT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)

# Запуск приложения
root.mainloop()