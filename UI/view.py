import flet as ft

from model import corso


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self.btn_cerca_corsi = None
        self.btn_iscrivi = None
        self.btn_cerca_studente = None
        self._controller = None
        self.txt_cognome = None
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_matricola = None
        self.dd_corso = None
        self.btn_cerca_iscritti = None
        self.txt_name = None
        self.txt_result = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW 0
        # Dropdown menu
        self.dd_corso = ft.Dropdown(
                label="corso",
                width=550,
                hint_text="Selezionare un corso",
                options=[],
                autofocus=True,
                on_change=self._controller.leggi_corso
        )
        self._controller.populate_dd_corso()
        # button for the cerca iscritti reply
        self.btn_cerca_iscritti = ft.ElevatedButton(text="cerca iscritti",
                                                    on_click=self._controller.handle_cerca_iscritti,
                                                    tooltip="cerca gli iscritti al corso selezionato")
        row0 = ft.Row([self.dd_corso, self.btn_cerca_iscritti],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row0)

        # ROW 1
        # dati dello studente
        self.txt_matricola = ft.TextField(
                label="matricola",
                width=150,
                hint_text="Inserire matricola")

        self.txt_name = ft.TextField(
                label="nome",
                width=250,
                read_only=True)

        self.txt_cognome = ft.TextField(
                label="cognome",
                width=250,
                read_only=True
        )
        row1 = ft.Row([self.txt_matricola, self.txt_name, self.txt_cognome],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # ROW2
        # Bottoni per cercare e iscrivere studenti
        self.btn_cerca_studente = ft.ElevatedButton(text="cerca studente",
                                                    on_click=self._controller.handle_cerca_studente,
                                                    tooltip="cerca lo studente della matricola selezionata")

        self.btn_cerca_corsi = ft.ElevatedButton(text="cerca corsi",
                                                 on_click=self._controller.handle_cerca_corsi,
                                                 tooltip="cerca i corsi a cui è iscritta la matricola selezionata")

        self.btn_iscrivi = ft.ElevatedButton(text="iscrivi",
                                             on_click=self._controller.handle_iscrivi,
                                             tooltip="iscrivi lo studente della matricola selezionata")

        row2 = ft.Row([self.btn_cerca_studente, self.btn_cerca_corsi, self.btn_iscrivi],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
