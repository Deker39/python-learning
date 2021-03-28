import json
from termcolor import colored, cprint

with open('question.json') as f:
    templates = json.load(f)

new_x = []
numbers_user_true_answer = 0
# print(len(templates['test']['']))

for x in range(len(templates['test']['quests'])):
    print("Вопрос: ",templates['test']['quests'][x])
    print("Ответы:")
    for y in range(len(templates['test']['answer'][x])):
        print(templates['test']['answer'][x][y])
        # print(templates['test']['answer'][x][y],end=' ')
    # print('\n')
    user_true_answer = int(input("Введи номер павильного овтета: "))
    if user_true_answer == templates['test']['true_answer'][x]:
        new_x.append(x)
        numbers_user_true_answer +=1


# print(colored(templates['test']['quests'][new_x], 'green'))



print("сколько правильнх: ",numbers_user_true_answer,"/",len(templates['test']['answer']))
print("правильный ответ",new_x)



