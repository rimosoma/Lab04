import time
import flet as ft
import model as md
import view


class SpellChecker:

    def __init__(self, v : view.View):
        self._multiDic = md.MultiDictionary()
        self._view = v



    def handle_lingua_tendina(self, e):
        if self._view._dd1.value:
            self._view.selezioneLingua.value =  f"Selezione andata a buon fine: {self._view._dd1.value}"
        else:
            self._view.selezioneLingua.value = "Selezione non valida"
        self._view.page.update()


    def handle_modo_tendina(self, e):
        if self._view._dd2.value:
            self._view.selezionaModo.value = f"Selezione andata a buon fine: {self._view._dd2.value}"
        else:
            self._view.selezionaModo.value = "Selezione non valida"
        self._view.page.update()

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text