# -*- coding: utf-8 -*- #gör så att åäö fungerar
import ui
import web



def alist(): #function för att printa en del utav ui
    ui.clear() #Clear call
    ui.line(False)  # printar en linje gjord utav -
    ui.header("ARTIST DATABASE")
    ui.line(True)  # printar en linje gjord utav *
    web.getart() #kallar på funktionen som tar fram listna av artister
    ui.line(False)  # printar en linje gjord utav -
    ui.echo("| Press enter to return ")  # Printar våra val
    ui.line(False)  # printar en linje gjord utav -
    ui.prompt()


def ainspect(): #function för att printa en del utav ui
    ui.clear() #Clear call
    ui.line(False)  # printar en linje gjord utav *
    ui.header("ARTIST DATABASE")
    ui.line(True)  # printar en linje gjord utav -
    web.inspectart() #kallar på funktionen som tar fram informationen på specifika artister.
    ui.line(False)  # printar en linje gjord utav *
    ui.echo("| Press enter to return ")  # Printar våra val
    ui.line(False)  # printar en linje gjord utav *
    ui.prompt()



while True: #kör en stor while sålänge som end variabeln inte innehåller
    ui.clear() #Clear call
    ui.line(False) #printar en linje gjord utav -
    ui.header("Welcome to the Music Library") #printar en header
    ui.line(False)#printar en linje gjord utav -
    ui.line(False)#printar en linje gjord utav -
    ui.echo("| L | Lista alla Artister") #Printar våra val
    ui.echo("| V | Inspektera Artist ")#Printar våra val
    ui.echo("| E | Stäng av ")
    ui.line(False)
    choice = ui.prompt()#variable input så att du kan kalla på

    if choice == "L": #gör så att vi kan välja olika val
        alist() #kallar på functionen alist
    if choice == "V": #gör så att vi kan välja olika val.
        ainspect() #kallar på functionen ainspect
    if choice == "E":
        break

