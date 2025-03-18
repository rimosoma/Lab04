import flet as ft

import controller


class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        self.row1 = None
        self._dd1 = None
        self.selezioneLingua = ft.Text(value="In attesa di selezione")

        self.row2 = None
        self._dd2 = None
        self.selezionaModo = ft.Text(value="In attesa di selezione")
        self._parolaInput = ft.TextField(label="Parola Ricercata")

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ], alignment=ft.MainAxisAlignment.START))

        self._dd1 = ft.Dropdown(label="Lingue",
                     hint_text="Seleziona la lingua",
                     options=[ft.dropdown.Option("Italiano"),
                              ft.dropdown.Option("Inglese"),
                              ft.dropdown.Option("Spagnolo")], on_change=self.__controller.handle_lingua_tendina)

        self.row1 = ft.Row(spacing=10, controls=[self._dd1, self.selezioneLingua])
        self.page.add(self.row1)



        self._dd2 = ft.Dropdown(label="Modo di ricerca",
                                hint_text="Seleziona il modo di ricerca",
                                options=[ft.dropdown.Option("Default"),
                                         ft.dropdown.Option("Lineare"),
                                         ft.dropdown.Option("Dicotomica")], on_change=self.__controller.handle_modo_tendina)

        self.row2 = ft.Row(spacing=10, controls=[self._dd2, ft.Text(value="                                                 "), self.selezionaModo ,self._parolaInput],)
        self.page.add(self.row2)

        # Add your stuff here


        self.page.update()

    def update(self):
        self.page.update()
    def setController(self, c : controller):
        self.__controller = c
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
