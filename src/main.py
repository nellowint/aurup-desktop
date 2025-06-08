import os
import flet as ft

from ui.navigation_tabs import NavigationTab
from utils.icons import Icons

def dark_mode(page: ft.Page, theme_mode):
    page.theme_mode = theme_mode

def main(page: ft.Page):

    theme_mode = 'light'
    dark_mode(page, theme_mode)
    path = os.path.join(os.path.dirname(__file__), 'assets', 'icons')
    icons = Icons(path)

    '''def on_dark_mode_event(e):
        if page.theme_mode == 'dark':
            theme_mode = 'light'
        else:
            theme_mode = 'dark'
        dark_mode(page, theme_mode)
        page.update()'''

    def notifications(e):
        pass

    notification_icon = ft.IconButton(
        icon=ft.Icons.NOTIFICATIONS,
        on_click=notifications,
        badge='10',
    )

    page.appbar = ft.AppBar(
        title=ft.Text('Aurup Desktop'),
        bgcolor=ft.Colors.WHITE30,
        leading_width=0,        
        actions=[
            notification_icon
        ]
    )

    nav = NavigationTab(icons)
    page.add(nav)
    
if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')