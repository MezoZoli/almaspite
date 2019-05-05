# print("Szia "+"anya!")
#
#
# print("Látod "+"mondtam "+"hogy "+"foglalkozom "+"vele!!!")
#
#
# def my_function(str1, str2):
#     print(str2)
#     print(str1)
#     return
#
#
# my_function("alma1", "alma2")
#
#
# def print_something(name = "something", age = "unknown"):
#     print("MY name is", name, "and my age is", age)
#     return
#
#
# print_something("Zoli")
# print_something(age = "15")
#
#
# def print_people(*people):
#     for person in people:
#         print("This person is", person)
#     return
#
#
# print_people("Zoli", "Dan", "Jack", "King")
#
#
# def do_math(num1, num2):
#     return num1 + num2
#
# math1 = do_math(5, 6)
# math2 = do_math(11, 2)
#
#
# def mondjad_mar_pls(ezt = "something", eztet = "something1", azt = "something2"):
#     print("A", ezt, "jó tank és a", eztet, ", ami melesleg utána jön az is jó tank...")
#     print("De a", azt, "tizes szinten már nem olyan jó mint a", ezt, "nyolcas szinten...")
#     return
#
#
# mondjad_mar_pls(ezt = "VK 100.01 (P)", eztet = "Mäuschen", azt = "Maus")
#
#
# print(
#        )
#
#
# def tanks(*germany):
#     for tank in germany:
#         print("Van pl", tank)
#     return
#

# tanks("PZ I C", "PZ II G", "PZ III J", "PZ IV H", "PZ IV G", "VK 36.01 H", "(meg még sok jelentéktelenebb VK)", "Tiger", "SP I C", "Panther", "Tiger II", "RHM BWT", "JGpanter", "JGpanter II", "(az előtő két sorban szerepel három is)", "Löwe", "Jagdtiger", "Maus", "E100", "E75", "Grille 15", "Leopard PTA", "Leopard 1", "és még sok egyéb baszógép")


# valtozo = "narancs"
#
#
# if valtozo is "citrom":
#     print("ez citrom")
# elif valtozo == "narancs":
#     print("ez narancs")
# else:
#     print("ez nem az")
#
# if valtozo is not "ananász":
#     print("és nem ananász")
#
#
# valtozo1 = 4
#
#
# if valtozo1 < 5:
#     print("{:f} < 5".format(valtozo1))


# !/usr/bin/env python3

# 2000. 01. 01. szombat
import re


def check_date():
    while True:
        userdate = str(input("Adjon meg egy datumot YYYY.MM.DD:\n"))
        if len(userdate) != 10:
            print("Helytelen formatum")
        elif len(userdate.split('.')) != 3:
            print("Helytelen formatum")
        elif int(userdate.split('.')[1]) in [1, 3, 5, 7, 8, 10, 12] and int(userdate.split('.')[2]) > 31:
            print("Helytelen nap")
        elif int(userdate.split('.')[1]) in [4, 6, 9, 11] and int(userdate.split('.')[2]) > 30:
            print("Helytelen nap")
        # FEBRUÁR:
        elif int(userdate.split('.')[1]) is 2 and int(userdate.split('.')[2]) > 28:
            print("Február csak 28 napos")
        elif (userdate.split('.')[0] % 4) == 0 and int(userdate.split('.')[1]) is 2 and int(userdate.split('.')[2]) > 27:
            print("Szökőévben max 27 nap!")
        elif (userdate.split('.')[0] % 100) == 0 and int(userdate.split('.')[1]) is 2 and int(userdate.split('.')[2]) > 28:
            print("100 évente kimarad úgyhogy 28 napos!")
        elif (userdate.split('.')[0] % 400) == 0 and int(userdate.split('.')[1]) is 2 and int(userdate.split('.')[2]) > 27:
            print("400 meg megint van!")
        else:
            break
    userdate = re.sub('[a-zA-Z,:()" "]', "", userdate)
    return userdate


def count_days(date):
    passed = 0

    l = date.split('.')
    year = int(l[0])
    month = int(l[1])
    day = int(l[2])
    # eltelt egesz evenkent +365
    passed += ((year - 2000) * 365)
    # +1 a 2000 szokonap miatt
    # 2000 utani szokoevenkent +1 nap
    passed += int((year - 2000) / 4)
    if (year % 4) == 0 and month <= 2:
        passed -= 1 and print("Szokoev van, de meg nem volt szokonap!")
    elif (year % 4) == 0 and month >=2:
        passed += 1 and print("Elvileg most az van hogy szökőév és szökőnap után vagyunk...")
    if (year % 100) == 0 and month <= 2:
        passed -= 1 and print("100 évente kimarad a szökőév!")
    if (year % 400) == 0 and month <= 2:
        passed -= 1 and print("400 évente viszont megint van szökőév!")
    elif (year % 400) == 0 and month >= 2:
        passed += 1 and print("400 évente megint van és elvileg utána vagyunk")
    # szamoljuk a teljes honapokat
    if month > 1:
        passed += 31
    if month > 2:
        passed += 28
    if month > 3:
        passed += 31
    if month > 4:
        passed += 30
    if month > 5:
        passed += 31
    if month > 6:
        passed += 30
    if month > 7:
        passed += 31
    if month > 8:
        passed += 31
    if month > 9:
        passed += 30
    if month > 10:
        passed += 31
    if month > 11:
        passed += 30
    # szmoljuk a napokat az aktualis honapban
    passed += day
    return passed


def eltelt2nap(eltelt):
    maradek = eltelt % 7
    if maradek == 0:
        print("szombat")
    elif maradek == 1:
        print("vasarnap")
    elif maradek == 2:
        print("hetfo")
    elif maradek == 3:
        print("kedd")
    elif maradek == 4:
        print("szerda")
    elif maradek == 5:
        print("csutortok")
    else:
        print("pentek")
    return


if __name__ == "__main__":
    date = check_date()
    print("Megadott datum: {:s}".format(date))
    passed = count_days(date)
    print("Eltelt {:d} nap".format(passed))
    eltelt2nap(passed)
