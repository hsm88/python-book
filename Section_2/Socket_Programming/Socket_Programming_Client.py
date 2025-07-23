## SocketProgramming_Code_Client
from flet import (Page, Container, Row, Column, Text, TextField,
                   IconButton, Colors, Icons, FontWeight, app)
import socket
import threading

# socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12345))

def send_to_server(text):
    client_socket.send(text.encode())

def receive_from_server():
    return client_socket.recv(1024).decode()

def main(page: Page):
    
    # page
    page.title = "Client"
    page.window.width = 400
    page.window.height = 600
    page.window.resizable = False
    page.window.maximizable = False

    # actions
    def send(e):
        if textField.value != "":
            send_to_server(textField.value)
            container_column.controls.append(
                                    Text(f"Client: {textField.value}", color=Colors.BLUE,
                                         size=20, weight=FontWeight.BOLD
                                    ))
            textField.value = ""
            page.update()

    def receive():
        while True:
            received_data = receive_from_server()
            container_column.controls.append(
                                    Text(f"Server: {received_data}", color=Colors.RED,
                                         size=20, weight=FontWeight.BOLD
                                    ))
            page.update()

    threading.Thread(target=receive).start()

    container_column = Column()
    container = Container(content=container_column, width=380, height=470, 
                          border_radius=2, padding=10, bgcolor=Colors.AMBER_100
                )
    textField = TextField(label="Send your message to server ...")
    button = IconButton(icon=Icons.SEND, icon_color=Colors.BLUE,
                            icon_size=45, on_click=send
             )
    row = Row(controls=[textField, button])
    column = Column(controls=[container, row])

    page.add(column)

app(target=main)

