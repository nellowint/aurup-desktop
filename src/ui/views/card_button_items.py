import flet as ft

class CardButtonItems(ft.Row):
    def __init__(self, icon, text):
        super().__init__()
        self.controls = [
            ft.Icon(
                icon,
                color=ft.Colors.WHITE                                        
            ),
            ft.Text(
                value=text,
                color=ft.Colors.WHITE
            )
        ]