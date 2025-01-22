import docker
from textual.app import App
from textual.widgets import Footer, Header, Button, DataTable
from textual.containers import Grid, Container
from textual.screen import Screen

class WelcomePage(Screen):
    def __init__(self, message, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = message
        self.containers_list = DataTable(id="containers-list", classes="containers-list")
        self.containers_list.add_columns("id", "name", "status")

    def show_containers(self):
        for container in dock.containers.list():
            container = [
                    container.id,
                    container.name,
                    container.status, ]
            self.containersList.add_row(*container)


    def compose(self):
        yield Header()
        yield Grid(
            Button("Containers", variant="primary", id="containers"),
            Button("Images", variant="default", id="images"),
            Button("Services", variant="default", id="services"),
            Button("Stacks", variant="default", id="stacks"),
            Button("Nodes", variant="default", id="nodes"),
            Container(
                self.containers_list,
                id="containers-wrapper",
            ),
            id="main-grid",
        )
        yield Footer()

class MyApp(App):
    CSS_PATH = "main.tcss"

    def on_mount(self):
        self.push_screen(WelcomePage("Welcome to the sys admin app"))

if __name__ == "__main__":
    MyApp().run()
