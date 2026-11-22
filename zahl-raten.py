import random

geheime_zahl = random.randint(1, 10)
versuch = 0

print("Ich habe mir eine Zahl zwischen 1 und 10 ausgedacht.")

while versuch != geheime_zahl:
    versuch = int(input("Dein Tipp: "))
    
    if versuch < geheime_zahl:
        print("Zu klein!")
    elif versuch > geheime_zahl:
        print("Zu groß!")
    else:
        print("Richtig geraten!")
        input('Drücke die Enter-Taste, um das Fenster zu schließen...')


