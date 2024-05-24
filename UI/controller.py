import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._id_map_corsi = {}

    def handle_cerca_iscritti(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        corso_selezionato = self._view.dd_corso.value
        if corso_selezionato is None:
            self._view.create_alert("Selezionare un corso!")
            return
        iscritti = self._model.get_iscritti(corso_selezionato)
        if iscritti is None:
            self._view.create_alert("Problema nella connessione!")
            return
        self._view.txt_result.controls.clear()
        if len(iscritti) == 0:
            self._view.txt_result.controls.append(ft.Text(f"Nessun studente iscritto al corso {corso_selezionato}!"))
        else:
            self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(iscritti)} al corso {corso_selezionato}"))
            for studente in iscritti:
                self._view.txt_result.controls.append(ft.Text(f"{studente}"))
            self._view.update_page()

    def handle_cerca_studente(self, e):
        matricola = self._view.txt_matricola.value
        if matricola == "":
            self._view.create_alert("Inserire una matricola!")
            return
        studente = self._model.cerca_studente(matricola)
        if studente is None:
            self._view.create_alert("Matricola non presente nel database")
            return
        else:
            self._view.txt_name.value = f"{studente.nome}"
            self._view.txt_name.update()
            self._view.txt_cognome.value = f"{studente.cognome}"
            self._view.txt_cognome.update()
        self._view.update_page()

    # def cerca_corsi(self, e):
    #     matricola = self._view.txt_matricola.value
    #     if matricola == "":
    #         self._view.create_alert("Inserire una matricola")
    #         return
    #     else:
    #         corsi = self._model.cerca_corsi(matricola)
    #         if corsi is None:
    #             self._view.create_alert("Non risulta nessuno studente con la matricola indicata")
    #         elif len(corsi) == 0:
    #             self._view.create_alert("Matricola selezionata non risulta iscritta ad alcun corso")
    #         else:
    #             self._view.txt_result.controls.clear()
    #             self._view.txt_result.controls.append(ft.Text(f"Risultano {len(corsi)} corsi:"))
    #             for corso in corsi:
    #                 self._view.txt_result.controls.append(ft.Text(f"{corso}"))
    #             self._view.update_page()
    def handle_cerca_corsi(self, e):
        matricola = self._view.txt_matricola.value
        if matricola == "":
            self._view.create_alert("Inserire una matricola")
            return
        else:
            corsi = self._model.get_corsi_studente(matricola)
            if corsi is None:
                self._view.create_alert("Non risulta nessuno studente con la matricola indicata")
            elif len(corsi) == 0:
                self._view.create_alert("La matricola indicata non risulta iscritta ad alcun corso")
            else:
                self._view.txt_result.controls.clear()
                self._view.txt_result.controls.append(ft.Text(f"Risultano {len(corsi)} corsi:"))
                for corso in corsi:
                    self._view.txt_result.controls.append(ft.Text(f"{corso}"))
                self._view.update_page()

    def handle_iscrivi(self, e):
        matricola = self._view.txt_matricola.value
        codins = self._view.dd_corso.value
        if matricola == "":
            self._view.create_alert("Inserire una matricola")
            return
        if codins is None:
            self._view.create_alert("Scegliere un corso")
            return
        studente = self._model.cerca_studente(matricola)
        if studente is None:
            self._view.create_alert("La matricola selezionata non è presente nel database")
            return
        result = self._model.iscrivi_corso(matricola, codins)
        self._view.txt_result.controls.clear()
        if result:
            self._view.txt_result.controls.append(ft.Text(f"Studente correttamente inscritto al corso {codins}"))
        else:
            self._view.txt_result.controls.append(ft.Text("Iscrizione fallita"))
        self._view.update_page()

    def populate_dd_corso(self):
        for corso in self._model.get_corsi():
            self._id_map_corsi[corso.codins] = corso
            self._view.dd_corso.options.append(ft.dropdown.Option(key=corso.codins, text=corso))
        self._view.update_page()

    def leggi_corso(self, e):
        self._view.txt_result.controls.append(
                ft.Text(value="Corso correttamente selezionato:" + self._view.dd_corso.value))
        self._view.update_page()
