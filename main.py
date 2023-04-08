import random
import PySimpleGUI as sg

size = (800, 600)
input_size = (120,13)
theme = sg.theme("LightGray1")
font = "Cambria"
bg_color = "white"
text_color = "black"
layout = [
    [sg.Text("Entrez le texte à transformer.", font="Cambria")],
    [sg.Multiline(key="prompt", size= input_size, no_scrollbar=True,
                  background_color=bg_color, text_color=text_color, font=font)],
    [sg.Button("Encoder"), sg.Button("Décoder"),sg.Button("Clear")],
    [sg.Multiline(key="answer", size= input_size, no_scrollbar=True,
                  disabled= True, background_color="#A8A8A8",
                  text_color=text_color, font=font)]
    ]
window = sg.Window("Encodeur/Décodeur - Louchébem", layout= layout, size= size,
                   font=font)

argot_suffixes = ["ji", "oc", "euil", "uche", "ès", "em"]
exceptions = ['je', 'tu', 'il', 'elle', 'on', 'nous', 'vous', 'ils', 'elles',
              'me', 'te', 'se', 'nous', 'vous', 'le', 'la', 'les', 'lui', "j'",
              'leur', 'y', 'en', 'ce', 'cette', 'ces', 'celui', 'celle', 'ceux',
              'celles', 'mon', 'ma', 'mes', 'ton', 'ta', 'tes', 'son', 'sa',
              'ses', 'notre', 'nos', 'votre', 'vos', 'leur', 'leurs', 'qui',
              'que', 'quoi', 'dont', 'où', 'qui', 'que', 'quoi', 'lequel',
              'laquelle', 'lesquels', 'lesquelles', "quelqu'un", 'personne',
              'chacun', 'rien', 'tout', 'autre', 'certains', 'plusieurs',
              'un', 'une', 'des', 'aucun', 'quelque', 'maint', 'tel', 'tant',
              'certain', 'nul', 'suis', 'es', 'est', 'sommes', 'êtes', 'sont',
              'étais', 'étais', 'était', 'étions', 'étiez', 'étaient', 'fus',
              'fus', 'fut', 'fûmes', 'fûtes', 'furent', 'serai', 'seras',
              'sera', 'serons', 'serez', 'seront', 'serais', 'serais', 'serait',
              'serions', 'seriez', 'seraient', 'sois', 'sois', 'soit', 'soyons',
              'soyez', 'soient', 'fusse', 'fusses', 'fût', 'fussions',
              'fussiez', 'fussent', 'étant', 'été', 'ai', 'as', 'a', 'avons',
              'avez', 'ont', 'avais', 'avais', 'avait', 'avions', 'aviez',
              'avaient', 'eus', 'eus', 'eut', 'eûmes', 'eûtes', 'eurent',
              'aurai', 'auras', 'aura', 'aurons', 'aurez', 'auront', 'aurais',
              'aurais', 'aurait', 'aurions', 'auriez', 'auraient', 'aie',
              'aies', 'ait', 'ayons', 'ayez', 'aient', 'eusse', 'eusses', 'eût',
              'eussions', 'eussiez', 'eussent', 'ayant', 'eu', 'à', 'après',
              'avant', 'avec', 'chez', 'contre', 'dans', 'de', 'depuis',
              'derrière', 'devant', 'en', 'entre', 'jusque', "jusqu'à", 'hors',
              'par', 'pour', 'sans', 'sous', 'sur', 'vers', "j'ai","j'aime",
              'mais', 'ou', 'et', 'donc', 'or', 'ni', 'car']
points = [".", ';',':', "!","?"]
f_answer = ""
end_point = ""

while True :
    #Gère les différents events
    event,values = window.read()
    if event == "Encoder":
        #Récupère l'input du multiline key="text"
        text = window["prompt"].get()
        if text:
            if text[-1] in points :
                end_point += text[-1]
                text = text[:-1]
            words = text.lower().split()
            for word in words :
                #Analyse et gère le cas d'un point à la fin du mot
                if word in exceptions :
                    f_answer += " " + word
                elif word not in exceptions :
                    #Prends la première lettre du mot et la place en dernier
                    word += word[0]
                    #Coupe la première lettre du mot
                    word = word[1:]
                    #Ajoute un "l" comme première lettre
                    word = "l" + word
                    #Choisis et ajoute un suffixe aléatoire dans la liste prévue
                    suffixe = random.choice(argot_suffixes)
                    word += suffixe
                    f_answer += " " + word
                    #Actualise le mot à l'écran
            f_answer += " " + end_point
            window["answer"].update(f_answer.lstrip().capitalize())
            f_answer = ""
            end_point= ""
        else :
            pass
    if event == "Décoder":
        # Récupère l'input du multiline key="text
        text = window["prompt"].get()
        if text:
            if text[-1] in points :
                end_point += text[-1]
                text = text[:-1]
            words = text.lower().split()
            for word in words:
                if word in exceptions:
                    f_answer += " " + word
                elif word not in exceptions:
                    # Choisis et supprime le suffixe choisi aléatoirement
                    suffixe = word[-2:]
                    if suffixe in argot_suffixes :
                        word = word[:-2]
                    elif suffixe not in argot_suffixes :
                        suffixe = word[-4:]
                        word = word[:-4]
                    # Supprime le "l" à la première lettre
                    word = word[1:]
                    # Prends la dernière lettre du mot et la place en premier
                    last_char = word[-1:]
                    word = word[:-1]
                    word = last_char + word
                    f_answer += " " + word
            # Actualise le mot à l'écran
            f_answer += " " + end_point
            window["answer"].update(f_answer.lstrip().capitalize())
            f_answer = ""
            end_point = ""
        else:
            pass
    if event == "Clear" :
        t_clear_1 = window["prompt"].update("")
        t_clear_2 = window["answer"].update("")
        f_answer = ""
        end_point = ""
    if event == sg.WIN_CLOSED :
        break

window.close()
