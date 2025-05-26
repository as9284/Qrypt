import flet as ft
import secrets
import string

CHARSET = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{};:,.<>?/|"


def generate_secure_password(length: int):
    """Generate a cryptographically secure password using the secrets library."""
    return "".join(secrets.choice(CHARSET) for _ in range(length))


def main(page: ft.Page):
    page.title = "Qrypt"
    page.window.width = 500
    page.window.height = 600
    page.window.alignment = ft.alignment.center
    page.window.resizable = False
    page.window.maximizable = False
    page.window.title_bar_hidden = True
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLACK

    def on_minimize_click(e):
        page.window.minimized = True
        page.update()

    def on_close_click(e):
        page.window.close()

    title_bar = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text(
                    "Qrypt",
                    weight=ft.FontWeight.BOLD,
                    size=20,
                    color=ft.Colors.WHITE,
                ),
                ft.Container(expand=True),
                ft.IconButton(
                    icon=ft.Icons.MINIMIZE,
                    icon_color=ft.Colors.WHITE,
                    tooltip="Minimize",
                    on_click=on_minimize_click,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=4),
                        overlay_color=ft.Colors.with_opacity(0.2, ft.Colors.WHITE),
                    ),
                ),
                ft.IconButton(
                    icon=ft.Icons.CLOSE,
                    icon_color=ft.Colors.WHITE,
                    tooltip="Close",
                    on_click=on_close_click,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=4),
                        overlay_color=ft.Colors.with_opacity(0.2, ft.Colors.WHITE),
                    ),
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=5,
        ),
        padding=ft.padding.symmetric(horizontal=10),
        bgcolor=ft.Colors.BLACK,
        height=40,
    )

    title = ft.Text(
        "Secure Passwords",
        size=30,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )
    subtitle = ft.Text(
        "Generate a password quickly", size=14, weight=ft.FontWeight.NORMAL
    )

    status_message = ft.Text(
        "",
        size=14,
        text_align=ft.TextAlign.CENTER,
        color=ft.Colors.GREEN_300,
        weight=ft.FontWeight.W_600,
    )

    def set_status(message: str, color: str):
        status_message.value = message
        status_message.color = color
        page.update()

    def generate_password(e):
        raw_val = (length_input.value or "").strip()
        set_status("", ft.Colors.GREEN_300)

        if not raw_val.isdigit():
            set_status("Please enter a valid number.", ft.Colors.RED_300)
            return

        length = int(raw_val)
        if length < 8 or length > 256:
            set_status("Length must be between 8 and 256.", ft.Colors.RED_300)
            return

        try:
            password = generate_secure_password(length)
            page.set_clipboard(password)
            set_status(
                "Password generated and copied to clipboard.", ft.Colors.GREEN_300
            )
        except Exception as err:
            set_status(str(err), ft.Colors.RED_300)

    length_input = ft.TextField(
        value="16",
        border=None,
        text_align=ft.TextAlign.CENTER,
        keyboard_type=ft.KeyboardType.NUMBER,
        on_submit=generate_password,
        bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
        cursor_color=ft.Colors.WHITE,
        color=ft.Colors.WHITE,
        label="Password Length (8–256)",
    )

    input_container = ft.Container(
        content=length_input,
        width=300,
        border_radius=10,
        padding=10,
        bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
    )

    generate_button = ft.Container(
        content=ft.Text("Generate Password", size=16, weight=ft.FontWeight.BOLD),
        width=200,
        height=45,
        alignment=ft.alignment.center,
        bgcolor=ft.Colors.BLUE,
        border_radius=10,
        ink=True,
        padding=10,
        on_click=generate_password,
    )

    content_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Column(
                    controls=[title, subtitle],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=2,
                ),
                input_container,
                generate_button,
                status_message,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
        padding=ft.padding.only(top=90, left=50, right=50, bottom=50),
        expand=True,
        alignment=ft.alignment.center,
    )

    page.add(
        ft.Stack(
            controls=[
                content_container,
                ft.Container(
                    content=title_bar,
                    left=10,
                    right=0,
                    top=6,
                ),
            ],
            expand=True,
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
