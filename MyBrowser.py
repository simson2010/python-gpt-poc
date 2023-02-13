import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtCore import QUrl

class MyBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MyBrowser")

        # 地址栏
        self.url_line_edit = QLineEdit(self)
        self.url_line_edit.returnPressed.connect(self.load_url)

        # 浏览器视图
        self.web_engine_view = QWebEngineView(self)
        self.web_engine_view.urlChanged.connect(self.update_url_line_edit)

        #创建新窗口
        self.web_engine_view.createWindow(QWebEnginePage.WebBrowserWindow).connect(new_window)

        # 垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.url_line_edit)
        layout.addWidget(self.web_engine_view)

        # 中央窗口部件
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def load_url(self):
        url = self.url_line_edit.text()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        self.web_engine_view.load(QUrl(url))

    def update_url_line_edit(self, url):
        self.url_line_edit.setText(url.toString())

    def new_window(self, url):
        browser = MyBrowser()
        browser.web_engine_view.load(QUrl(url))
        browser.show()

app = QApplication(sys.argv)
browser = MyBrowser()
browser.show()
browser.load_url()
sys.exit(app.exec_())
