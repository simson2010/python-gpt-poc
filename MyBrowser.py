import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextBrowser, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MyBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Web Browser")
        self.setGeometry(100,100,800,600)

        self.web_engine_view = QWebEngineView(self)
        self.line_edit = QLineEdit(self)
        self.line_edit.returnPressed.connect(self.load_url)
        self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.web_engine_view.back)
        self.forward_button = QPushButton("Forward", self)
        self.forward_button.clicked.connect(self.web_engine_view.forward)

        layout = QVBoxLayout()
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.back_button)
        buttons_layout.addWidget(self.forward_button)
        layout.addLayout(buttons_layout)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.web_engine_view)

        central_widget = QMainWindow(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def load_url(self):
        url = self.line_edit.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.web_engine_view.setUrl(QUrl(url))

app = QApplication(sys.argv)
browser = MyBrowser()
browser.show()
sys.exit(app.exec_())