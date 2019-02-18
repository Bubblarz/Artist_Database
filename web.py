
# -*- coding: utf-8 -*-
import requests,ui



def getart(): #funktionen som tar ned en lista med namnen på artisterna.
    url = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/' #lägger in våran url i en variabel
    r = requests.get(url) #sparar ner listan till variabeln R
    svar = r.json() #gör om json listan så att vi kan använda den.
    artists = svar["artists"] #gör så att vi kan ta ut informationen med nyckel ordet Artists
    for artist in artists: #itererar igenom våra artister
        ui.echo(artist["name"]) #skriver ut namnet för varje artist.


def inspectart(): #funktionen som kombinerar urlen med artist Id så att vi kan komma åt djupare element i api'n.
    url = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/'#tar samma url som innan.
    r = requests.get(url) #sparar ned urlen i variabeln R
    svar = r.json() #gör om json listan så att vi kan använda den.
    artists = svar["artists"] #gör så att vi kan ta ut informationen med nyckel ordet Artists
    val = ui.prompt() #kallar på promt funktionen så att vi kan göra ett val utav vilken artist vi vill åt.

    for artist in artists: #itererar igenom våra artister så att vi kan komma längre in i dictionariet.
        if val.title() == artist["name"]: #kollar så att artisten i loopen nu stämmer med vårat val.
            ui.line(True)  # printar en linje gjord utav -
            Aid = artist["id"] #sparar ned Id's på våran matchande artist.
            newurl= str(url + Aid) #tar Id's och kombinerar det med våran url
            z = requests.get(newurl) #gör en request emot den nya urlen
            inspection = z.json()#sparar ned json objektet så att programmet kan agera med det.
            ui.echo("Name: " + inspection["artist"]["name"])
            ui.echo(" ")
            ui.echo("Genres")
            for genre in inspection["artist"]["genres"]:#loopar och printar ut genres på våra artister
                ui.echo(genre)
            ui.echo(" ")
            for years in inspection["artist"]["years_active"]:#loopar igenom och printar ut de åren som gruppen var aktiv
                ui.echo("Years active: " + years)
            print(" ")
            ui.echo("Members")
            for member in inspection["artist"]["members"]:#loopar igenom och printar ut de medlemar i bandet och deras stagenames, har de inte det så printar det bandnamnet.
                ui.echo(member)