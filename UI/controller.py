import flet as ft
from UI.view import View

from model.model import Model


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._id_map_corsi = {}

    def handle_cerca_iscritti(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        self._view.txt_result.controls.append(ft.Text(value=f"Ci sono {self._model.count_iscritti(self._view.dd_corso.value)} iscritto al corso:"))
        for iscritto in self._model.get_iscritti(self._view.dd_corso.value):
            self._view.txt_result.controls.append(ft.Text(value=iscritto))
        self._view.update_page()

    def populate_dd_corso(self):
        for corso in self._model.get_corsi():
            self._id_map_corsi[corso.codins] = corso
            self._view.dd_corso.options.append(ft.dropdown.Option(key=corso.codins, text=corso))
        self._view.update_page()

    def leggi_corso(self):
        self._view.txt_result.controls.append(
            ft.Text(value="Corso correttamente selezionato:" + self._view.dd_corso.value))
        self._view.update_page()
