import sys
import requests

from PyQt6.QtCore import(Qt,QUrl)

from PyQt6.QtNetwork import (QAuthenticator)
from client_secret import(clientID,secret)
from PyQt6.QtWebEngineCore import (QWebEngineUrlScheme,QWebEngineCookieStore,QWebEngineHttpRequest)
from PyQt6.QtWebEngineWidgets import (QWebEngineView)
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QWidget,
    QMainWindow,
    QVBoxLayout,
)

class Window(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("AllDeck")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool | Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setStyleSheet("QMainWindow { background-color:black; min-width: 400px; min-height: 800px;}")
        self.grid = QGridLayout()

         #auth the app
        auth = requests.Request.auth(clientID,secret)
        response = requests.post("https://www.reddit.com/api/v1/access_token", data={"grant_type": "client_credentials"}))
        accessToken= requests.Response.json()["access_token"]


        centralWidget = QWidget(self)
        #centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)



if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())