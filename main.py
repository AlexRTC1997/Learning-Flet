import flet as ft


def main(page: ft.Page):
    page.title = "My Digital Library"
    page.theme_mode = ft.ThemeMode.DARK

    def change_theme(e):
        page.theme_mode = ft.ThemeMode.LIGHT if page.theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.DARK
        theme_icon_button.icon = ft.icons.LIGHT_MODE if page.theme_mode == ft.ThemeMode.DARK else ft.icons.DARK_MODE
        page.update()

    theme_icon_button = ft.IconButton(
        icon=ft.icons.LIGHT_MODE,
        tooltip="Change theme",
        on_click=change_theme
    )

    title = ft.Text("Digital Library")

    page.add(title, theme_icon_button)


ft.app(target=main)
