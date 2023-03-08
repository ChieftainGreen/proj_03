import flet as ft

run_backend = None
def main(page: ft.Page):
    page.title = "Youtube Downloader"
    page.vertical_alignment = "center"
    page.window_height = 800
    page.window_width = 600

    def handle_submit(e):
        run_backend(url_input.value)
        page.update()

    url_input = ft.TextField(label="Video URL", on_submit=handle_submit)
    #
    selected_path = ft.Text()
    selected_path.value = "File Save Location"
    download_button = ft.TextButton("Download", on_click=handle_submit)

    page.add(
        ft.Column(
            [
                ft.Row([
                    url_input
                ]),
                ft.Row([
                    selected_path
                ]),
                ft.Row([
                    download_button
                ])
            ]
        )
    )

def run_gui():
    ft.app(target = main)

if __name__ == "__main__":
    run_gui()