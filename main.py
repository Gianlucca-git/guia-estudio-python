from datetime import datetime, timedelta, date
import unicodedata
# font https://equisd.com/normalizar-cadenas-con-python-elimina-esos-simbolos-y-caracteres-extranos/
from slugify import *


def main():
    # dates()
    normalized()
    print(" FINISH")


def dates():
    yesterday = datetime.now() + timedelta(days=-1)
    year = yesterday.strftime("%Y")
    month = yesterday.strftime("%m")
    day = yesterday.strftime("%d")
    yesterday_date = str(year) + str(month) + str(day)
    print(" LOG 1 -> ", yesterday.strftime("%Y%m%d"))


def normalized():
    # s = 'L' + chr(246) + 'wis'
    # t = 'L' + chr(111) + chr(776) + 'wis'

    # print(s)
    # print(t)
    # print(f' LOG #1 -> {s == t}')

    # nt = unicodedata.normalize('NFC', t)
    # print(nt)
    # print(f' LOG #2 -> {s == nt}')

    txt = ' liquidacióñ Salarial '
    r = slugify(txt)
    print(f' LOG #3 -> {r}')

    rr = slugify(txt, separator=" ", regex_pattern=r'[^-a-z0-9$]+')
    print(f' LOG #4 -> {rr}')


if __name__ == '__main__':
    main()
from datetime import datetime, timedelta, date
import unicodedata
# font https://equisd.com/normalizar-cadenas-con-python-elimina-esos-simbolos-y-caracteres-extranos/
from slugify import *


def main():
    # dates()
    normalized()
    print(" FINISH")


def dates():
    yesterday = datetime.now() + timedelta(days=-1)
    year = yesterday.strftime("%Y")
    month = yesterday.strftime("%m")
    day = yesterday.strftime("%d")
    yesterday_date = str(year) + str(month) + str(day)
    print(" LOG 1 -> ", yesterday.strftime("%Y%m%d"))


def normalized():
    # s = 'L' + chr(246) + 'wis'
    # t = 'L' + chr(111) + chr(776) + 'wis'

    # print(s)
    # print(t)
    # print(f' LOG #1 -> {s == t}')

    # nt = unicodedata.normalize('NFC', t)
    # print(nt)
    # print(f' LOG #2 -> {s == nt}')

    txt = ' liquidacióñ Salarial '
    r = slugify(txt)
    print(f' LOG #3 -> {r}')

    rr = slugify(txt, separator=" ", regex_pattern=r'[^-a-z0-9$]+')
    print(f' LOG #4 -> {rr}')


if __name__ == '__main__':
    main()
