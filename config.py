"""Configuration file. There are some constants for customize the app"""

WINDOW_SIZE = (1024,  576)
MINIMUM_WIDTH = 440
MINIMUM_HEIGHT = 350
APP_NAME = "Improve your typing skills"
MAX_SPEED = 1000
DEBUG = False
HINT_TEXT = ''
STAT_FILE_NAME = 'stat.json'
BACKGROUND_COLOR = (.9, .9, .9, 1)

e2E = {'`': '~', '1': '!', '2': '@', '3': '#', '4': '$', '5': '%', '6': '^',
       '7': '&', '8': '*', '9': '(', '0': ')', '-': '_', '=': '+', 'q': 'Q',
       'w': 'W', 'e': 'E', 'r': 'R', 't': 'T', 'y': 'Y', 'u': 'U', 'i': 'I',
       'o': 'O', 'p': 'P', '[': '{', ']': '}', '\\': '|', 'a': 'A', 's': 'S',
       'd': 'D', 'f': 'F', 'g': 'G', 'h': 'H', 'j': 'J', 'k': 'K', 'l': 'L',
       ';': ': ', "'": '"', 'z': 'Z', 'x': 'X', 'c': 'C', 'v': 'V', 'b': 'B',
       'n': 'N', 'm': 'M', ', ': '<', '.': '>', '/': '?'}
e2r = {'`': 'ё', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6',
       '7': '7', '8': '8', '9': '9', '0': '0', '-': '-', '=': '=', 'q': 'й',
       'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш',
       'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ', '\\': '\\', 'a': 'ф', 's': 'ы',
       'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д',
       ';': 'ж', "'": 'э', 'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и',
       'n': 'т', 'm': 'ь', ', ': 'б', '.': 'ю', '/': '.'}
e2R = {'`': 'Ё', '1': '!', '2': '"', '3': '№', '4': ';', '5': '%', '6': ': ',
       '7': '?', '8': '*', '9': '(', '0': ')', '-': '_', '=': '+', 'q': 'Й',
       'w': 'Ц', 'e': 'У', 'r': 'К', 't': 'Е', 'y': 'Н', 'u': 'Г', 'i': 'Ш',
       'o': 'Щ', 'p': 'З', '[': 'Х', ']': 'Ъ', '\\': '/', 'a': 'Ф', 's': 'Ы',
       'd': 'В', 'f': 'А', 'g': 'П', 'h': 'Р', 'j': 'О', 'k': 'Л', 'l': 'Д',
       ';': 'Ж', "'": 'Э', 'z': 'Я', 'x': 'Ч', 'c': 'С', 'v': 'М', 'b': 'И',
       'n': 'Т', 'm': 'Ь', ', ': 'Б', '.': 'Ю', '/': ', '}
