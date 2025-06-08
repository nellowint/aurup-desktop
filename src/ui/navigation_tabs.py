import flet as ft
from .tabs.search_tab import SeachTab
from .tabs.installed_tab import InstalledPackages
from utils.icons import Icons

class NavigationTab(ft.Tabs):
    def __init__(self, icons: Icons):
        super().__init__()
        self.icons = icons
        self.selected_index=0
        self.expand=True
        self.scrollable= True
        self.animation_duration=300
        self.indicator_tab_size=True
        self.label_padding=ft.padding.only(left=30, right=30)
        self.tab_alignment=ft.TabAlignment.CENTER
        self.tabs = self._tabs()
            
    def _tabs(self):
        return [   
            ft.Tab(
                adaptive=True,
                icon=ft.Icons.EXPLORE,
                text='Explore',
                content=SeachTab(self.icons)
            ),
            ft.Tab(
                adaptive=True,
                icon=ft.Icons.COMPUTER,
                text='Installed',
                content=InstalledPackages(self.icons)
            ),
            ft.Tab(
                icon=ft.Icons.SETTINGS,
                text='Settings',
                content=ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Text('Example 3')
                )
            )
        ]