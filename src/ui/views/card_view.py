import flet as ft

from models.package import Package
from .card_button import CardButton
from .card_button_items import CardButtonItems

class CardView(ft.Card):
    def __init__(self, package: Package, home: bool):
        super().__init__()
        self.package = package
        self.home = home

        self.button_update = (
            CardButton(
                data=self.package,
                content=CardButtonItems(
                    icon=ft.Icons.INSTALL_DESKTOP, 
                    text='Install'
                )
            ) if self.home 
            else CardButton(
                data=self.package,
                content=CardButtonItems(
                    icon=ft.Icons.UPDATE, 
                    text='Update'
                ),
                bgcolor=ft.Colors.BLUE_400
            )  
        )

        self.content = ft.Container(
            padding=10,
            margin=ft.margin.only(left=0),
            content=ft.Column(
                controls=[
                    self._fields(self.package),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            self.button_update
                            ]
                        )
                    ]
                )
            )        

    def _fields(self, package):
        return ft.Row(
            controls=[
                ft.Image(
                    width=80,
                    height=80,
                    border_radius=100,
                    fit=ft.ImageFit.COVER,
                    src=f'icons/{package.icon}'
                ),
                ft.Column(
                    controls=[
                        ft.Text(
                            value=f'{package.name}',
                            size=20,
                            weight='bold'
                        ),
                        ft.Text(
                            width=500,
                            value=f'{package.description}',
                            size=18,
                            max_lines=3,
                            expand=True
                        ),
                        ft.Text(
                            value=f'version: {package.version}',
                            size=14,
                        )
                    ]
                )
            ]
        )