import random
from datetime import date

data = open("word_list.txt", "r") # Textfile mit den Wörtern
word_list = data.readlines() # Alle Wörter werden eingelesen

day = date.today() # Das aktuelle Datum wird geholt
s = day.day + day.month + day.year # Ein Seed für den jeweiligen Tag wird erstellt
random.seed(s) # Der seed wird festgesetzt

word = word_list[random.randint(0, len(word_list))] # Zufälliges Wort aus der Liste wird ausgewählt

l = 0
x = [0 for i in range(5)] # Liste mit 5 einträgen wird erstellt und mit 0 gefüllt
for j in range(6): # Die 5 versuche zum erraten
    if x.count(1) != 5: # Fragt ab, wie oft die 1 in der list "x" ist. Wenn 5 also alle Buchstaben richtig sind bricht er ab
        eingabe = input("Gib dein wort ein: ") # Das eingegebene Wort
        while len(eingabe) != 5: # Es wird so lange eine neue Eingabe gefordert, bis das eingegebene Wort 5 Buchstaben hat
            print("Das Wort ist zu lang oder kurz. Bitte gib ein Wort mit genau 5 Buchstaben ein!")
            eingabe = input("Bitte gib ein neues Wort mit 5 Buchstaben ein: ")
        print(eingabe)

        # Hier wird geprüft wie viele matches ich habe
        aa = [0 for i in range(5)]
        b = sorted(word)
        bb = [ord(b[i]) for i in range(5)]
        c = sorted(eingabe)
        cc = [ord(c[i]) for i in range(5)]

        for i in range(5):
            aa[i] = bb[i] - cc[i]
        richtig = aa.count(0)
        for k in range(5):
            if word.find(eingabe[k]) == -1: # Wenn der Buchstabe nicht vorhanden ist, wird ne 0 in die Liste eingetragen
                x[k] = 0
            elif word[k] == eingabe[k]: # Wenn der Buchstabe an der richtigen Position ist, eine 1
                x[k] = 1
            else: # Wenn der Buchstabe im Wort ist, jedoch an der falschen Stelle, dann eine 2
                if word.count(eingabe[k]) != eingabe.count(eingabe[k]): # wenn im wort und in der eingabe unterschiedlich oft der aktuelle Buchstabe vorkommen
                    if word.find(eingabe[k]) == eingabe.rfind(eingabe[k]): # Wenn hinterher noch ein buchstabe an der richtigen stelle ist
                        x[k] = 0
                    elif word.find(eingabe[k]) == eingabe.find(eingabe[k]): # Wenn vorher ein buchstabe an der richtigen stelle war
                        x[k] = 0
                    elif richtig == l:
                        x[k] = 0
                    else:
                        x[k] = 2
                        l = l + 1
                else:# word.count(eingabe[k]) == eingabe.count(eingabe[k]): # Buchstabe kommt genauso oft in der eingabe und ind er ausgabe vor
                    x[k] = 2
        print(x) # Die Liste wird ausgegeben
        l=0
    else:
        print("Top du hast das Wort richtig erraten! Gz!") # Wenn alle Einträge 1 sind.
        break