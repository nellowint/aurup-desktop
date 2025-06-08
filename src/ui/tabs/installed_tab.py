import os
import flet as ft
from controllers.aurup_api_controller import AurupAPIController
from models.package import Package
from ui.views.card_view import CardView
from utils.icons import Icons

class InstalledPackages(ft.Column):
    def __init__(self, icons: Icons):
        super().__init__()
        self.icons = icons
        self.controller = AurupAPIController(icons)
        self.width=900
        self.has_update = False
        self.alignment=ft.MainAxisAlignment.CENTER
        self.horizontal_alignment=ft.CrossAxisAlignment.CENTER
        self.scroll=ft.ScrollMode.ADAPTIVE

        self._local_results = ft.Column(
            width=900,
            spacing=5,
            visible=False,
            auto_scroll=False,
            scroll=ft.ScrollMode.ALWAYS,
        )

        self.controls = [
            self._local_results
        ]

    def build(self):
        self.controller.load_packages()

    def did_mount(self):
        self._populate_page()
    
    def is_isolated(self):
        return True

    def _populate_page(self):
        if self.controller.packages:
            self._local_results.visible = True
            self._local_results.clean()
            
            for package in self.controller.packages:
                if package.version > package.local_version:
                    self.has_update = True
                card = CardView(package, False)
                self._local_results.controls.append(card)
                self.update()

            if self.has_update:
                self.has_update = False
                self._show_message(
                    message='There are packages to be updated',
                    color=ft.Colors.BLUE_400
                )
        else:
            self._local_results.visible = False
            self._local_results.clean()
            self._show_message(
                message='There are no AUR packages installed',
                color=ft.Colors.RED_400
            )

    def _show_message(self, message, color):
        snackbar = ft.SnackBar(
                    content=ft.Text(
                        value=message,
                        color=ft.Colors.WHITE
                    ),
                    bgcolor=color,
                    duration=1000,
                    open=True
                )
        self.controls.append(snackbar)
        self.update()   
