import flet as ft

from controllers.aurup_api_controller import AurupAPIController
from models.package import Package
from ui.views.card_view import CardView
from utils.icons import Icons

class SeachTab(ft.Column):
    def __init__(self, icons: Icons):
        super().__init__()
        self.icons = icons
        self.controller = AurupAPIController(icons)
        self.width=900
        self.alignment=ft.MainAxisAlignment.CENTER
        self.horizontal_alignment=ft.CrossAxisAlignment.CENTER
        self.scroll=ft.ScrollMode.ADAPTIVE

        self._search_results = ft.Column(
            width=900,
            spacing=5,
            visible=False,
            auto_scroll=False,
            scroll=ft.ScrollMode.ALWAYS
        )

        self._icon_clean_search = ft.IconButton(
            icon=ft.Icons.CLOSE,
            visible=False,
            right=5,
            tooltip='Clean Search',
            on_click=self._clean_search,
        )

        self._search = ft.TextField(
                                width=600,
                                border_radius=5,
                                text_size=18,
                                max_length=100,
                                hint_text='Search Package in AUR',
                                prefix_icon=ft.Icon(ft.Icons.SEARCH),
                                on_submit=self._search_package,
                                on_change=self._search_change
                            )

        self.controls = [
                ft.Container(
                    margin=ft.margin.only(top=10),
                    content=ft.Stack(
                        alignment=ft.alignment.center_right,
                        controls=[
                            self._search,
                            self._icon_clean_search
                        ]
                    )
                ),
                self._search_results
            ]
        
    def is_isolated(self):
        return True

    def _search_package(self, e):
        result = e.control.value.lower()
        self.controller.packages.clear()
        self.controller.search_packages(
            name=result, 
            searching=True
        )
        
        if self.controller.packages:  
            self._search_results.visible = True
            self._search_results.clean()

            for package in self.controller.packages:
                card = CardView(package, True)
                self._search_results.controls.append(card)
                self.update()
        else:
            self._search_results.visible = False
            self._search_results.clean()

            snackbar = ft.SnackBar(
                    content=ft.Text(
                        value='No results found',
                        color=ft.Colors.WHITE
                    ),
                    bgcolor=ft.Colors.RED_400,
                    duration=1000,
                    open=True
                )
            self.controls.append(snackbar)
            self.update()

    def _search_change(self, e):
        if e.control.value:
            self._icon_clean_search.visible = True
        else:
            self._icon_clean_search.visible = False
        
        self._icon_clean_search.update()

    def _clean_search(self, e):
        self._search.value = ''
        e.control.visible = False
        e.control.update()
        self._search.update()
            
           
