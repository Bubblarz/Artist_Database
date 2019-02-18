# utf-8 är Svenska bokstäver.
#-*- coding: utf-8 -*-

import os
#importerar OS så vi kan komma åt funktionen clear


def line(user): #functionen som skapar linjer
    """ För att skapa linje som består av (*) eller (-). """
    if user == True:
        print("*"*26)
    else:
        print("-"*26)


def header(huvud): #en utskrifts funktion
    """ Centrerar text i huvud. """
    fill = str(huvud.center(22, " "))
    print("| " + str(fill) +  " |")


def echo(text):
    """ Text utskrift med stöd för mer än ett dictionary objekt. """
    print(text)


def prompt(): #våran funktion som hjälper oss att välja
    """ Prompt användaren med val """
    choice = input("| Val > ").upper() #Gör input till stora bokstäver som passar choice
    return choice


def clear():
    """ Clear funktion som kommer från OS, funkar endast för Windows" """
    os.system("cls")
    

