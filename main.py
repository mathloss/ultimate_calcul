from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from random import *



class MainWidget(BoxLayout):
    pass


class BoxLayout(BoxLayout):
    pass


class MyScreenManager(ScreenManager):

    def choix1(self):
        self.choix = 1
        return self.choix

    def choix2(self):
        self.choix = 2
        return self.choix

    def choix3(self):
        self.choix = 3
        return self.choix

    def choix4(self):
        self.choix = 4
        return self.choix



    def press(self):
        if self.choix == 1:
            # Les variables
            a = randint(0,10)
            b = randint(0,10)
            # print(a, b)
            self.ids.nbr_A.text = str(a)
            self.ids.nbr_B.text = str(b)
        elif self.choix == 2:
            # Les variables
            a = randint(50,500)
            b = randint(50,500)
            # print(a, b)
            self.ids.nbr_A.text = str(a)
            self.ids.nbr_B.text = str(b)

        elif self.choix == 3:
            liste = [0,1,2,3,4,5,10]
            a = choice(liste)
            b = choice(liste)
            # print(a, b)
            self.ids.nbr_A.text = str(a)
            self.ids.nbr_B.text = str(b)

        elif self.choix == 4:
            # Les variables
            a = randint(0,10)
            b = randint(0,10)
            # print(a, b)
            self.ids.nbr_A.text = str(a)
            self.ids.nbr_B.text = str(b)

    def compare(self):
        if self.choix == 1 or self.choix == 2:
            c = int(self.ids.sol_input.text)
            # print(c)
            enigme = int(self.ids.nbr_A.text) + int(self.ids.nbr_B.text)
            if c == enigme:
                self.ids.resultat.text = "Gagné !!"
            else:
                self.ids.resultat.text = "Perdu..."
        elif self.choix == 3 or self.choix == 4:
            c = int(self.ids.sol_input.text)
            # print(c)
            enigme = int(self.ids.nbr_A.text)*int(self.ids.nbr_B.text)
            if c == enigme:
                self.ids.resultat.text = "Gagné !!"
            else:
                self.ids.resultat.text = "Perdu..."

    def rep_ok(self):
        if self.choix == 1 or self.choix == 2:
            rep = int(self.ids.rep_ok.text)
            if int(self.ids.nbr_A.text) + int(self.ids.nbr_B.text) == int(self.ids.sol_input.text):
                rep += 1
            self.ids.rep_ok.text = str(rep)
        elif self.choix == 3 or self.choix == 4:
            rep = int(self.ids.rep_ok.text)
            if int(self.ids.nbr_A.text) * int(self.ids.nbr_B.text) == int(self.ids.sol_input.text):
                rep += 1
            self.ids.rep_ok.text = str(rep)

    def essai(self):
        ess = int(self.ids.essai.text)
        ess += 1
        self.ids.essai.text = str(ess)

    def image(self):
        if self.choix == 1 or self.choix == 2:
            if int(self.ids.nbr_A.text) + int(self.ids.nbr_B.text) == int(self.ids.sol_input.text):
                self.ids.image.source = "image/ok.png"
            else:
                self.ids.image.source = "image/no.png"
        elif self.choix == 3 or self.choix == 4:
            if int(self.ids.nbr_A.text) * int(self.ids.nbr_B.text) == int(self.ids.sol_input.text):
                self.ids.image.source = "image/ok.png"
            else:
                self.ids.image.source = "image/no.png"

    def clear(self):
        self.ids.resultat.text = ""
        self.ids.image.source = "image/noir.png"
        self.ids.sol_input.text = "0"

    def reset_partie(self):
        self.ids.nbr_A.text = "0"
        self.ids.nbr_B.text = "0"
        self.ids.sol_input.text = "0"
        self.ids.image.source = "image/noir.png"
        self.ids.essai.text = "0"
        self.ids.rep_ok.text = "0"
        self.ids.resultat.text = ""

    def quit_partie(self):
        quit()

    def titre_signe1(self):
        self.ids.titre.text = "Addition :"
        self.ids.signe.text = "+"

    def titre_signe2(self):
        self.ids.titre.text = "Multiplication :"
        self.ids.signe.text = "X"





class Ultimate_CalculApp(App):
    pass


Ultimate_CalculApp().run()