import flet as ft
from models.package import Package

class CardButton(ft.Container):
    def __init__(
            self, 
            data, 
            content,
            bgcolor=ft.Colors.GREEN_400,
        ):
        super().__init__()
        self.width=100
        self.padding=8
        self.margin=5
        self.border_radius=10
  
        self.data = data
        self.disabled = True
        self.bgcolor_temp = bgcolor
        self.bgcolor = '#5f5f5f'
  
        self.alignment=ft.alignment.center
        self.content = content
        self.on_click = self.on_click_listener
        self.outdated = self.data.local_version < self.data.version

    def build(self):
        if self.outdated:
            self.disabled = False
            self.bgcolor = self.bgcolor_temp

    def on_click_listener(self, e):
        print(self.data)
