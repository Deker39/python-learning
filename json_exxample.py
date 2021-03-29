import json
#
quest = { "quests":["сколько лет",
                    "сколкьо милионов",
                    "где живешь"],
          "answer" : [[1,2,3],
                      [100,200,300],
                      ["odessa","kiev","lviv"]
                      ]
          }

to_json = {'test': quest}


with open('test/tests1.json', 'w') as f:
    json.dump(to_json, f,sort_keys=True, indent=3,ensure_ascii=False )

with open('test/tests1.json') as f:
    kek = f.read()
    print(kek)



# import json
#
# with open('tests1.json') as f:
#     templates = json.load(f)
#
# print(templates)
# for x in templates["quests"]["quest1"]:
#     print(x)
# for x in range(len(templates["quests"]['answer'])):
#     kek = templates["quests"]['answer'][x]
#     print(kek[0],kek[1],kek[2])
# # print("{1}\n{2}\n{3}".format(kek[0],kek[1],kek[2]) )
# for x in templates["quests"]['answer'][0]:
#     print(x)

# for section, commands in templates.items():
#     print(section)
#     print('\n'.join(commands))
