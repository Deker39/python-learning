from math import*

# thislist = ["apple", "banana", "cherry","kiwi","tomato","pineapple"]#6
# for x in range(len(thislist)):#6 0...6 if x==6:
#     print(x ,"-", thislist[x])
#
# i = 0
# while i < len(thislist):#6 if i < 6 , i > 6 , i == 6
#   print(thislist[i])
#   i = i + 1
#
# for x in thislist:
#     print(x)







# tropical = ["mango", "pineapple", "papaya"]
# print(thislist)
# thislist.insert( 2,"watermelon")
# print(thislist)
# thislist.append('orange')
# print(thislist)
# thislist.extend(tropical)
# # print(thislist)
# thislist.remove("apple")
# thislist.pop()
# del thislist
# thislist.clear()
# print(thislist)











# thislist.append("orange")
#В адересе [1] будет "orange"
# thislist[1:2] = ["potato", "rasspbwery"]
# print(thislist[-4:])

#запрос на "orange"
# if "orange" in thislist:
#     print("orange здесь")
# else:
#     print("Ёе здесь нету")

# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# list = list(my_dict.values())
# list.sort()
# for x in range(len(list)):
#     print(x , "-", list[x])









# print(my_dict.values()
# list_key = list(my_dict.values())
# print(list_key)
# list_key.sort()
# for x in my_dict:
#     print(x ,"-" ,my_dict[x])
# print(list_key)
# for x in range(len(list_key)):
#     print(x , "-", list_key[x]))
#

# kek = "apple"," tommato"
# mylist = ["one", "five","three"]
# thislist = ["one", "two","three"]
# # mylist1 = []
# # mylist.pop()
# mylist1 = mylist
# print(mylist1)
# mylist.append(thislist)
# print(mylist)
# vlad_list = list(kek)
# print(vlad_list)

# fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango","kiwi")
# for x in range(len(fruits)):
#     kek = fruits[x]
#     print()
# for x in fruits:
#     print(x)
# (green,yellow, *red) = fruits
#
# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2
#
# print(mytuple)
#




# del this_tuple
# print(this_tuple)
# this_list = list(this_tuple)
# print(this_list)
# this_list[4] = "python"
# print(this_list)
# this_tuple = tuple(this_list)
# print(this_tuple)





# print(thistuple[2:5])
# if "kiwi" in thistuple:
#     print("kiwi, this")
# print(thistuple)
# print(len(thistuple))
# print(type(thistuple))
# newtuple = ("minecraft",)#0,1
# print(type(newtuple))
# this_dict = dict({
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964})
# print(this_dict)
# this_set = {"apple", "banana", "cherry","apple"}
# this_set1 = {"apple12", "banana12", "cherry12","apple13"}
# this_set.add("orange")
# this_set.update(this_set1)
# print(this_set)



# this_set_new = {"apple", "banana", "cherry","apple","chocolat","milk","egg"}
# mylist = ("kiwi", "orange")
# this_set_new.remove("bananaa")
# this_set_new.discard("banana")
# this_set_new.update(mylist)
# x = this_set_new.pop()
# print(x)
# this_set_new.clear()
# print(this_set_new)

# for x in this_set:
#     for y in this_set_new:
#         print(y in x)
#         print(y)


# for x in range(len(this_set)):
#   print(this_set[x])

# print(len(this_set))
# print(this_set)
# print(type(this_set))

# x = {1,2,34,5,6}
#
# set_one = {"google", "microsoft", "facebook","apple","google"}
# set_two = {1,2,34,5,6}
# set_two.update(set_one)
# set_three = set_one.union(set_two)
# set_three = set_one.union(set_two)
# set_two.remove("sony")
# set_two.discard("sony")
# set_two.pop()
# set_two.clear()
# print(set_two)
# print("xbox" in y)

# print(x)
# z = x.isdisjoint(y)
#
# print(z)

# x = {"a": 2, "b" : 13, "c":"kek"}
# for i in x:
#   print(i , " - ",x[i])
# y = {"f", "e", "d", "c", "b", "a"}
#
# z = x.issubset(y)
#
# print(z)
#
#Create a set
# num_set = set([0,1,2,3,4,5])
# setp = set(["Red1", "Green"])
# setq = set(["Green", "Red"])
# #A shallow copy
# setr = setp.copy()
# print(setr)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.intersection_update(y)
# print(x)
# z = x.symmetric_difference(y)
# print(z)


# #1 Напишите программу Python для создания набора
# new_set = set((1,2,3))
# print(new_set)
# #2 Напишите программу Python для перебора наборов
# for x in new_set:
#     print(x)
# #3 Напишите программу Python для добавления єлемента в набор
# new_set.add(26)
# print(new_set)
# #4  Напишите программу Python для удаления элементов из набора
# new_set.remove(1)
# print(new_set)
# #5  Напишите программу Python для удаления элемента из набора,
# # если он присутствует в наборе.
# new_set.discard(26)
# print(new_set)
# #6 Напишите программу Python для создания пересечения множеств
# setx = set(["green", "blue"])
# sety = set(["blue", "yellow"])
# setz = setx.intersection(sety)
# print(setz)
# #7 Напишите программу на Python для создания объединения множеств
# x = set([1,2,3])
# y = set([4,2,6])
# z = x.union(y)
# print(z)
# #8 Напишите программу Python для создания различий между наборами
# setx = set(["apple", "mango"])
# sety = set(["mango", "orange"])
# setz = setx.symmetric_difference(sety)
# print(setz)
# #9 Напишите программу на Python для создания симметричной разницы
# x = set([1,2,3])
# y = set([4,2,6])
# z = x.symmetric_difference(y)
# print(z)
# #10  Напишите программу Python, чтобы проверить, является ли набор подмножеством другого набора
# x = {"a","b","c"}
# y = {"f", "e", "d", "c", "b", "a"}
# z = x.issubset(y)
# print(z)
# #14 Напишите программу на Python, чтобы найти максимальное и минимальное значение в наборе.
# set_set = set([15,13,2,4,5,7,8])
# print("max = ", max(set_set))
# print("min = ", min(set_set))
# #16 Напишите программу на Python, чтобы проверить, присутствует ли данное значение в наборе или нет.
# set_set = set([15,13,2,4,5,7,8])
# print(15 in set_set)
# #17 Напишите программу на Python, чтобы проверить, не имеют ли два заданных набора общих элементов.
# x = {1,2,3,4}
# y = {4,5,6,7}
# z = {8}
# print("If two given sets have no elements in common")
# print("Compare x and y:")
# print(x.isdisjoint(y))
# print("Compare x and z:")
# print(z.isdisjoint(x))
# print("Compare y and z:")
# print(y.isdisjoint(z))
#
# z = {"a":12,"b":2,"c":3}
# for x in z:
#     print(x , "-" ,z[x])

# import requests
# import json
# import urllib.request
#
#
# nbu_url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
# r = requests.get(nbu_url)
# j = json.loads(r.text)
# # print(j)
# # print (type(j))
#
# for x in j :
#     # print("Золото" in x["txt"])
#     print(x['txt'])
#     print(x)
# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "color": {"brand": "Ford", "model": "Mustang","year": 1964}
# }
#
# mydict = thisdict.copy()
# print(mydict)
# thisdict["color"] = "red"
# thisdict.update({"color": ["red","green","blue"],
#                 "year": 1998})
# thisdict.popitem()
# del thisdict
# thisdict.clear()
# print(thisdict)
# print(thisdict.items())
# for x,y  in thisdict.items():
#   print(x)
#   print(y)
  # print("{0} -> {1}".format(x,thisdict[x]))
  # print(x ," -> ", thisdict[x])
  # print("%s -> %s" % (x,thisdict[x]))

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
# print(myfamily.keys())
#
# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }
#
# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#     "child3" : child3
#   }
#
#

# if "color" in thisdict:
#   print('yes')
#
# print("color" in thisdict)
# print(len(thisdict))
# print(thisdict["color"]["model"])
# x = thisdict["color"]

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = car.setdefault("model", "Bronco")
#
# print(x)

# x = ('key1', 'key2', 'key3')
# y = 0
#
# thisdict = dict.fromkeys(x, y)
#
# print(thisdict)
# x = ('key1', 'key2', 'key3')
#
# thisdict = dict.fromkeys(x)
#
# print(thisdict)

#task1
# onedict = { 1:10,
#             2:20}
# twodict = { 3:30,
#             4:40}
#
# threedict  = {}
#
# threedict.update(onedict)
# threedict.update(twodict)
# print(threedict)
#task2
# dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# a  = int(input("Введи ключ - "))
# print( a in dict)
# a = dict.keys()
# if 3 in a:
#     print("True")
# else:
#     print("False")
#task3
# dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# a = dict.keys()
# b = dict.values()
# for a,b in dict.items():
#     print(a,"->",b)
# for x in dict:
#     print(x  ,":",  dict[x])
#task4
# dict = {6: 60,3: 30, 4: 40,1: 10, 2: 20,  5: 50 }
#
# for key in sorted(dict):
#     print("%s : %s" % (key,dict[key]))
# dict = {3: 30,1: 10,4: 40, 5: 50, 2: 20, 6: 60}
# for a in sorted(dict.items()):
#   print(a)
# a = 0
# for x in dict.values():
#   a = a + x
# print(a)
# print(sum(dict.values()))
#
# result_str=""
# for row in range(0,7):
#     for column in range(0,7):
#       if ((column == 1 or column == 5) and row != 0 and row != 6):
#             result_str=result_str+"*"
#       else:
# #             result_str=result_str+" "
#
#       if ((row == 0 or row == 6) and column > 0 and column < 5 ):
#             result_str=result_str+"*"
#       else:
#             result_str=result_str+" "
#     result_str=result_str+"\n"
# print(result_str)

# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

# i = 10
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i  меньше 6")


# stydent = ['maxim','vlad','alex','max']
# for x in stydent:
#   if x =='alex':
#     continue
#   print(x)


# fruit = 'banana'
# for x in fruit:
#   print(x)

# for x in range(6):
#   if x == 3: break
#   print(x)
# else:
#   print("Finally finished!")

# color = ["red", "big", "tasty"]
# # fruits = ["apple", "banana", "cherry"]
# #
# # for x in color:
# #   for y in fruits:
# #     print(x, y)

# for x in range(0,10):
#   pass


# '''
# леша
# 22
# учитель
# максим
# 14
# ученик
# '''
# a = list(input("Enter your data ").split())
# print(a)
# list1 = list(a)
# name = list1[0]
# age =  list1[1]
# profession = list1[2]
# print( name,age,profession)

# def alex(*name):
#   print(name[1] + " hello")
#
# a = "alex"
# alex(a,'12','odess','str.Govorova 12')
# alex("max",'12')
# alex("vlad",'11')
# alex("maxim",'11')

# def my_function(*kids,name):
#   print("Самый младший ребенок " + kids[0])
#   print('Мой ключ ', name)
#
# my_function("Emili", "Tobias", "Linus",name='alex')


# def output(list):
#   for x in list:
#     print(x)

# name = list(input("Введи имя учеников ").split())
# food =list(input("Введи продукты ").split())

# output(name)
# output(food)

# output(thislist)

# def my_function(**kids):
#   print("last name " + kids["lname"]["k"])
# a = {'k' :"king",
#      'h' : "shevchemko"}
# my_function(fname = "Tobias", lname = a)

# def my_function(country = "None"):
#   print("i am from " + country)
#
# my_function("indiya")
# my_function("usa")
# my_function()
# my_function("russia")
#
# def my_function(x):
#   return 5*x
#
# print(my_function(5))
# print(my_function(4))
# print(my_function(3))

# def my_func():
#   x = 10
#   print("Значение внтури функции" , x)
#
# x = 20
# my_func()
# print("Значение вне функции" , x)

# def sum(number):
#   total = 0
#   for x in number:
#     total += x
#   return total
#
#
# a =5,456,3,22,100
# print(sum(a))

#
# def string_revers(str1):
#
#   rev_str1=''
#   index = len(str1)
#   while index > 0:
#     rev_str1 += str1[index - 1]
#     index -= 1
#   return  str1, rev_str1
#
#
# print(string_revers("hellow, world"))
import json



# with open('tests123.json') as f:
#   templates = json.load(f)
#
# # while x <= len((templates["test"]["quests"])):
# quest = iter(templates["test"]["quests"])
# answer = iter(templates["test"]['answer'])
# print(next(answer))
# print(next(answer))
# print(next(answer))
# print(next(quest))
# ui3.label_2.setText(quest[x])
# print(quest[x])
# answer = templates["test"]['answer'][x]
# ui3.radioButton.setText(str(answer[x]))
# ui3.radioButton_2.setText(str(answer[x+1]))
# ui3.radioButton_3.setText(str(answer[x+2]))

def on_click(i):
  i = i + 1
  print("i:",i)
x = 11
on_click(x)
print("x: ",x)