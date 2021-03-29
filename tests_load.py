import json

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

with open('test/tests1.json', 'w') as f:
    json.dump(to_json, f,sort_keys=True, indent=3,ensure_ascii=False )


