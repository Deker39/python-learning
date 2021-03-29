import json
from termcolor import colored, cprint

with open('test/tests1.json') as f:
    templates = json.load(f)

new_x = []
user_true_answer = []
numbers_user_true_answer = 0
# print(len(templates['test']['']))

for x in range(len(templates['test']['quests'])):
    print("Вопрос: ",templates['test']['quests'][x])
    print("Ответы:")
    for y in range(len(templates['test']['answer'][x])):
        print(templates['test']['answer'][x][y])
        # print(templates['test']['answer'][x][y],end=' ')
    # print('\n')
    answer = input("Введи номер павильного овтета: ")
    user_true_answer.append(answer)
    if user_true_answer[x] == templates['test']['true_answer'][x]:
        new_x.append(x)
        numbers_user_true_answer +=1
    #     print(colored(templates['test']['quests'][x],'green'))
    # else:
    #     print(colored(templates['test']['quests'][x],'red'))





# print(colored(templates['test']['quests'][new_x], 'green'))

for x in range(len(templates['test']['true_answer'])):
    if user_true_answer[x] == templates['test']['true_answer'][x]:
        print(colored(templates['test']['quests'][x],'green'))
    else:
        print(colored(templates['test']['quests'][x],'red'))

print("сколько правильнх: ",numbers_user_true_answer,"/",len(templates['test']['answer']))
print("правильный ответ",new_x)



