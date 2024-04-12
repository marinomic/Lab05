import flet as ft

from model import corso


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self.btn_cerca_iscritti = None
        self.txt_name = None
        self.txt_result = None
        self.btn_hello = None
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

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW 0
        # Dropdown menu
        self.dd_corso = ft.Dropdown(
                width=550,
                label="corso",
                hint_text="Selezionare il corso",
                options=[],
                autofocus=True,
                on_change=self._controller.leggi_corso
        )
        self.controller.populate_dd_corso()
        self.txt_matricola = ft.TextField(
                label="Matricola",
                width=200,
                hint_text="Inserire il numero di matricola"
        )

        # button for the cerca iscritti reply
        self.btn_cerca_iscritti = ft.ElevatedButton(text="cerca iscritti", on_click=self._controller.handle_cerca_iscritti)
        row1 = ft.Row([self.btn_cerca_iscritti],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

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
