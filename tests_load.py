import json
import os

question = []
answer = []
true_answer =[]
a = int(input("Скольок будет вопросов?\n"))
for x in range(a):
    x = input("Введите вопрос:\n")
    question.append(x)
    x = list(input("Введите отвты: \n").split('.'))
    answer.append(x)
    x = input("Введите правильный ответ:")
    true_answer.append(x)
print(question)
print(answer)
print(true_answer)

quest = {"quests":question,
         "answer":answer,
         "true_answer":true_answer
         }

to_json = {'test': quest}


# with open('tests1.json') as f:
#     data = json.load(f)
#
#     data['test']['quests'].extend(question)
#     data['test']['answer'].extend(answer)
#     data['test']['true_answer'].extend(true_answer)
#     print(data)
#
#
#
# with open('tests1.json', 'w') as f:
#     json.dump(data, f,sort_keys=True, indent=3,ensure_ascii=False )

if os.path.isfile('tests1.json') and os.access('tests1.json',os.R_OK):
    with open('tests1.json') as f:
        data = json.load(f)

    data['test']['quests'].extend(question)
    data['test']['answer'].extend(answer)
    data['test']['true_answer'].extend(true_answer)
    print(data)

    with open('tests1.json', 'w') as f:
        json.dump(data, f,sort_keys=True, indent=3,ensure_ascii=False )
else:
    with open('tests1.json', 'w') as f:
        json.dump(to_json, f,sort_keys=True, indent=3,ensure_ascii=False )


