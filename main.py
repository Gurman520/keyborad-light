from time import sleep
from keyboard import press, release
from sys import exit
from ctypes import windll
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw
from threading import Thread

# Настройки программы
settings = {
    'interval': 15,
    'running': True
}

def is_admin():
    try:
        return windll.shell32.IsUserAnAdmin()
    except:
        return False

def about_inform():
    windll.user32.MessageBoxW(
        0,
        "Keyboard Backlight Keeper v1.0\n\n"
        "A program to keep the keyboard illuminated\n"
        "Developer: Sulima Roman\n"
        "GitHub: https://github.com/Gurman520/keyborad-light\n\n"
        "Working principle: emulates pressing F15\n"
        "every 15 seconds to maintain the backlight.",
        "About the program",
        0x40 | 0x0  # MB_ICONINFORMATION | MB_OK
    )

def create_image():
    """Создаем иконку для трея"""
    # Половина черная, половина белая - как клавиатура с подсветкой
    image = Image.new('RGB', (16, 16), color='black')
    dc = ImageDraw.Draw(image)
    dc.rectangle([0, 8, 16, 16], fill='white')  
    return image

def keep_alive():
    while settings['running']:
        press('F15')
        sleep(0.1)
        release('F15')
        sleep(settings['interval'])

def exit_program(icon):
    settings['running'] = False
    icon.stop()

if not is_admin():
    windll.user32.MessageBoxW(
        0,
        "This program requires administrator rights to work.\n\n"
        "Please run the program as an administrator.",
        "Access rights error",
        0x10  # Значок ошибки
    )
    exit(1)

# Запускаем поток с основной логикой
thread = Thread(target=keep_alive, daemon=True)
thread.start()

# Создаем меню для иконки в трее
menu = Menu(
    MenuItem('About the program', about_inform),
    Menu.SEPARATOR,
    MenuItem('EXIT', exit_program)
)

# Создаем иконку в трее
icon = Icon(
    'Keyboard Backlight', 
    icon=create_image(),
    menu=menu,
    title="Keyboard backlight support"
)

icon.run()