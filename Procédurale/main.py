ASCII_ORDER = 96
letters = [chr(c) for c in range(ASCII_ORDER+1,123)]

def owner_in(value: str, table: list) -> bool:
    for v in range(len(table)):
        if value.lower() == table[v]:
            return True
    return False


def get_symbol_right_answer(reps : list, answer :str ) -> str:
    for i in range(len(reps)):
        if answer == reps[i]:
            return chr(ASCII_ORDER + i + 1)

get_chars = lambda value, alphabet = letters: alphabet[:value]

def get_chars_2(value:int, alphabet: list = letters) -> list:
    new_list = []
    for c in range(value):
        new_list.append(alphabet[c])
    return new_list

def get_chars_3(value:int, alphabet: list = letters) -> list:
    return alphabet[:value]
#  const 96     
#  97 98 99
# [a, b, c]
#  0  1  2
# index = 97 - (96 + 1)
def get_answer_from_index(alpha :str, possible_answers : list):
    index = ord(alpha) - (ASCII_ORDER + 1) # Le position de la réponse dans la liste
    return possible_answers[index] # La réponse du client
    
        
"""
1. Quelle est la capitale de la France ?
a. Madrid
b. Rome
c. Paris
d. Berlin
Réponse : (c)

2. Combien de continents y a-t-il sur Terre ?
a. 5
b. 6
c. 7
d. 8
Réponse : (c)

3. Quel est le plus grand océan du monde ?
a. Atlantique
b. Indien
c. Arctique
d. Pacifique
Réponse : (d)

4. Quelle est la planète la plus proche du Soleil ?
a. Mars
b. Vénus
c. Mercure
d. Jupiter
Réponse : (c)

5. Qui a écrit Les Misérables ?
a. Victor Hugo
b. Émile Zola
c. Gustave Flaubert
d. Alexandre Dumas
Réponse : (a)

6. Quel est l'élément chimique dont le symbole est "O" ?
a. Or
b. Oxygène
c. Osmium
d. Ozone
Réponse : (b)

7. Quelle est la langue la plus parlée au monde en nombre de locuteurs natifs ?
a. Anglais
b. Espagnol
c. Chinois mandarin
d. Arabe
Réponse : (c)

8. Quelle est la monnaie officielle du Japon ?
a. Won
b. Yen
c. Yuan
d. Ringgit
Réponse : (b)

9. Dans quel sport utilise-t-on une balle de service ?
a. Football
b. Tennis
c. Basket-ball
d. Hockey
Réponse : (b)

10. Qui a peint la Joconde ?
a. Michel-Ange
b. Raphaël
c. Léonard de Vinci
d. Rembrandt
Réponse : (c)
"""
# question1 = [
#     "Quelle est la capitale de la France ?",
#     """ 
#         a. Madrid
#         b. Rome
#         c. Paris
#         d. Berlin
#         """,
#         "c"
# ]
# question2 = [
#     "Combien de continents y a-t-il sur Terre ?",
#     """ 
#         a. 5
#         b. 6
#         c. 7
#         d. 8
#         """,
#         "c"
# ]
# questions = [
#     question1,
#              question2]
# foreach
# for question in questions:
#     print(question)

# ["Titre de la question 1", "Titre de la question 2"]
#           0                        1
# for i in range(len(questions)):
#     print("Question ", (i + 1), " : ", questions[i])

# for index, question in enumerate(questions, start=1):
#     # print("Question ", index, " : ", question)
#     title = question[0]
#     responses = question[1]
#     answer = question[2]
#     print("Question ", index, " : ", title)
#     print(responses)
    
    
    
# range(1,len(questions) + 1)
# range(0,n-1) = range(1, len(question)+1)
    
# enumerate(list, int) = [list, int]
# question, index in  [[list1, list2, list..n], int]
# notes = [18,19, 0]
# note1, note2, note3 = notes
# note1 = notes[0]
# note2 = notes[1]
# note3 = notes[2]
# print(note1)
# print(note2)
# print(note3)
    # print(questions[i])
# range(10) = 0,1,2,3,4,5,6,7,8,9
# list(range(10)) = [0,1,2,3,4,5,6,7,8,9]
# foreach()
# for _ in range(10):
# for x in [0,1,2,3,4,5,6,7,8,9]:
    # print(x)
    # 0123456789
# print(len(questions)) # 2
# print(list(range(1,2))) # 1
# for item in items:
    # print(items)
# items = [1,2,3,4]
# word = "Bonjour"
# word_1 = ['B', 'o', 'n', 'j', 'o' ,'u' , 'r']
# for i in word:
    # print(i)
    # B o n j o u r
# len(word)
# len(items) = 4
# for i in range(len(items)):
    #pass

# ===================== Approche AB ===================
# question1 = [
#     "Quelle est la capitale de la France ?",
#     ["Madrid","Rome","Paris","Berlin"],
#     #   0         1     2        3
#     "Paris"
# ]

# question2 = [
#     "Combien de continents y a-t-il sur Terre ?",
#     ["5","6","7","8"],
#     "7"
# ]

# questions = [question1, question2]
import os

clear = lambda : os.system('cls')


# def ask_question(index, question) -> str:
#     print(f"Question, {index} : {question[0]} (eg : a)")
#     for i,rep in enumerate(question[1], start=1):
#         print(f"    {chr(ASCII_ORDER + i)}. {rep}")
#     return input("-> ")

# score = 0

# for index, question in enumerate(questions, start=1):
#     answers_size = len(question[1])
#     answer = question[2]
#     # client_answer = ""
#     while True:
#         client_answer = ask_question(index, question)
#         if not owner_in(client_answer, get_chars(answers_size)):
#             clear()
#             continue
#         break
#     if get_answer_from_index(client_answer, question[1]) == answer:
#         print("Bravo bonne réponse !")
#         score += 1
#     else:
#         print("Orrhh, Erreur")
#         print(f"La réponse était : {question[2]}")
# print(f"Vous avez {score} / {len(questions)}")
    


    
        

# print(get_chars_2(alphabet=letters, value=6))
# print(get_chars_2(6, letters))
# print(get_chars_2(6))



# print(get_chars_3(alphabet=letters, value=6))
# print(get_chars_3(6, letters))
# print(get_chars_3(6)) 
# Comprehension de liste
# for i in range(10)
#     pass


# ============ Recursivité =============
# 1234567890

# def get_int_1() -> int:
#     value = input("Entrez un nombre : ")
#     while value not in ['0','1','2', '3', '4', '5', '6', '7', '8', '9']:
#         print("ERROR : Veuillez réssayer !")
#         value = input("Entrez un nombre : ")
#     return int(value)
# list_chiffres = list(range(10))



# def get_int_2() -> int:
#     while True:
#         try:
#             value = input("Entrez un nombre : ")
#             if int(value) in list_chiffres:
#                 break
#         except ValueError:
#             print("ERROR : Veuillez réssayer !")
#     return int(value)



# def get_int() -> int:
#     value = input("Entrez un nombre : ")
#     if not value.isdigit():
#         return get_int()
#     return int(value)


# print(get_int())
# print(get_int_1())
# print(get_int_2())




# ============= Approche BIEN =============

TITLE = "title"
REPONSES_POSSIBLE = "reponses_possible"
REPONSE = "reponse"

# question1 = {
#     TITLE : "Quelle est la capitale de la France ?",
#     REPONSES_POSSIBLE : ["Madrid", "Rome", "Paris", "Berlin"],
#     REPONSE : "Paris"
# }


# question2 = {  
#     TITLE :"Combien de continents y a-t-il sur Terre ?",
#     REPONSES_POSSIBLE : ["5","6","7","8"],
#     REPONSE : "7"
# }

def ask_question_2(index : int, question: dict) -> str:
    print(f"Question, {index} : {question.get("title")} (eg : a)")
    for i,rep in enumerate(question.get(REPONSES_POSSIBLE), start=1):
        print(f"    {chr(ASCII_ORDER + i)}. {rep}")
    return input("-> ")

# score = 0

# questions = []

# question.get("reponse") = question["reponse"]

# for index, question in enumerate(questions, start=1):
#     answers_size = len(question.get(REPONSES_POSSIBLE))
#     answer = question.get(REPONSE)
#     while True:
#         client_answer = ask_question_2(index, question)
#         if not owner_in(client_answer, get_chars(answers_size)):
#             clear()
#             continue
#         break
#     if get_answer_from_index(client_answer, question.get(REPONSES_POSSIBLE)) == answer:
#         print("Bravo bonne réponse !")
#         score += 1
#     else:
#         print("Orrhh, Erreur")
#         print(f"La réponse était : {question.get(REPONSE)}")
# print(f"Vous avez {score} / {len(questions)}")

# ============= Approche BIEN avec source externe txt =============

# question1 = {
#     TITLE :title,
#     REPONSES_POSSIBLE : reponses_possibles,
#     REPONSE : reponse
# }
questions = []
PATH = "db/questions.txt"
file = open(PATH, "r")
# lines = ["Quelle est la capitale de la France ?#Madrid,Rome,Paris,Berlin#c","Combien de continents y a-t-il sur Terre ?#5,6,7,8#c"]
lines = file.readlines()
for line in lines:
    line = line.replace("\n", "").split("#")
    line[1] = line[1].split(',')
    
    question = {}
    question[TITLE] = line[0]
    question[REPONSES_POSSIBLE] = line[1]
    question[REPONSE] = line[2]
    print(question.get(REPONSE))
    questions.append(question)
file.close()




# RECOMMANDE
# with open(PATH, "r") as file:
#     pass




score = 0

for index, question in enumerate(questions, start=1):
    reps = question.get(REPONSES_POSSIBLE)
    answers_size = len(reps)
    answer = question.get(REPONSE)
    while True:
        client_answer = ask_question_2(index, question)
        if not owner_in(client_answer, get_chars(answers_size)):
            clear()
            continue
        break
    if get_answer_from_index(client_answer, reps) == answer:
        print("Bravo bonne réponse !")
        score += 1
    else:
        print("Orrhh, Erreur")
        print(f"La réponse était {get_symbol_right_answer(reps, question.get(REPONSE))} : {question.get(REPONSE)}")
print(f"Vous avez {score} / {len(questions)}")
