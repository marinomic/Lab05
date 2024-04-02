import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def cerca_iscritti(self,e):
        codice_corso = self._view.dd_corso.value
        if codice_corso is None:
            self._view.create_alert("Selezionare un corso!")
            return
        iscritti = self._model.get_iscritti_corso(codice_corso)
        if len(iscritti) == 0:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Non ci sono iscritti al corso"))
        else:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(iscritti)} iscritti al corso:"))
            for iscritto in iscritti:
                self._view.txt_result.controls.append(ft.Text(f"{iscritto}"))
            self._view.update_page()


    def cerca_studente(self,e):
        matricola = self._view.txt_matricola.value
        if matricola == "":
            self._view.create_alert("inserire una matricola")
            return
        studente = self._model.cerca_studente(matricola)
        if studente is None:
            self._view.create_alert("Matricola non presente nel database")
            return
        else:
            self._view.txt_nome.value = f"{studente.nome}"
            self._view.txt_cognome.value = f"{studente.cognome}"
        self._view.update_page()

    def cerca_corsi(self,e):
        matricola = self._view.txt_matricola.value
        if matricola == "":
            self._view.create_alert("inserire una matricola")
            return
        else:
            corsi = self._model.get_corsi_studente(matricola)
            if len(corsi) == 0:
                self._view.create_alert("La matricola indicata non risulta iscritta ad alcun corso")
            else:
                self._view.txt_result.controls.clear()
                self._view.txt_result.controls.append(ft.Text(f"Risultano {len(corsi)} corsi:"))
                for corso in corsi:
                    self._view.txt_result.controls.append(ft.Text(f"{corso}"))
                self._view.update_page()

    def iscrivi(self,e):
        matricola = self._view.txt_matricola.value
        if matricola == "":
            self._view.create_alert("inserire una matricola")
            return
        studente = self._model.cerca_studente(matricola)
        if studente is None:
            self._view.create_alert("Matricola non presente nel database")
            return
        codice_corso = self._view.dd_corso.value
        if codice_corso is None:
            self._view.create_alert("Selezionare un corso!")
            return
        result = self._model.iscrivi_corso(matricola,codice_corso)
        self._view.txt_result.controls.clear()
        if result:
            self._view.txt_result.controls.append(ft.Text("Iscrizione avvenuta con successo"))
        else:
            self._view.txt_result.controls.append(ft.Text("Iscrizione fallita"))
        self._view.update_page()



    def populate_dd_corso(self):
        for corso in self._model.get_corsi():
            self._view.dd_corso.options.append(ft.dropdown.Option(corso.codins))
        self._view.update_page()

    def visualizza_nome_corso(self, e):
        codice_corso = self._view.dd_corso.value
        corso = self._model.get_corso(codice_corso)
        if corso is not None:
            self._view.txt_corso.value = f"{corso.nome}"
            self._view.update_page()

