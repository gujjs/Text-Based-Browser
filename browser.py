import sys
import os
import requests
from _collections import deque
from bs4 import BeautifulSoup
from colorama import init, Fore, Style, Back


def folder():
    arguments = sys.argv
    if len(arguments) == 2:
        shit = os.path.join(arguments[1])
        try:
            os.mkdir(shit)
        except FileExistsError:
            pass
        return os.path.join(os.getcwd(), arguments[1], '')
    else:
        return os.path.join(os.getcwd(), '')


def user():
    ur = input()

    if ur == 'exit':
        return None
    elif ur == 'back':
        h = history()
        if h is not None:
            return h
        else:
            return user()
    elif ur in lib:
        return ur
    elif ur[:8] != 'https://':
        ur = 'https://' + ur
        return ur
    else:
        return ur


def history():
    try:
        a = stack.pop()
        b = stack.pop()
        stack.append(b)
        stack.append(a)
        return b
    except IndexError:
        return None
lib = []
stack = deque()


def page(pg):
    soup = BeautifulSoup(pg.content, "html.parser")

    requisites = ['p', 'a', 'header', 'li']

    required = []

    # for elem in soup(requisites):
    #     line = elem.text.strip()
    #     print(line)
    #     required.append(line)
    init()
    for child in soup(requisites):
        if child.name == 'a':
            required.append('\033[31m' + child.text.strip())
            print('\033[34m' + child.text.strip())
        elif child.name in requisites:
            required.append(child.text.strip())
            print(child.text.strip())

    return required


def start():
    path = folder()

    while True:
        u = user()
        if u is None:
            break
        elif u[:8] == 'https://':
            name = '.'.join(u.split('//')[1].split('.')[:-1])
            if name[:4] == "www.":
                name = name[4:]
            try:
                r = requests.get(u)
                pg = page(r)
                with open(path + name + ".txt", "w") as f:
                    try:
                        f.write('\n'.join(pg))
                    except TypeError:
                        pass
                lib.append(name)
                stack.append(name)
            except requests.exceptions.ConnectionError:
                print('error')


start()
#
# page(requests.get("https://docs.python.org"))
