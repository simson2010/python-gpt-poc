import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QToolBar, QAction, QProgressBar
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.web_engine_view = QWebEngineView()
        self.setCentralWidget(self.web_engine_view)
        
        self.address_bar = QLineEdit()
        self.address_bar.returnPressed.connect(self.load_url)

        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)
        self.toolbar.addWidget(self.address_bar)

        back_button = QAction("Back", self)
        back_button.triggered.connect(self.web_engine_view.back)
        self.toolbar.addAction(back_button)

        forward_button = QAction("Forward", self)
        forward_button.triggered.connect(self.web_engine_view.forward)
        self.toolbar.addAction(forward_button)
        
        self.progress_bar = QProgressBar()
        self.statusBar().addPermanentWidget(self.progress_bar)
        self.web_engine_view.loadProgress.connect(self.update_progress_bar)

        self.setWindowTitle("Browser")

    def load_url(self):
        url = QUrl(self.address_bar.text())
        if not url.scheme():
            url.setScheme("http")
        self.web_engine_view.load(url)

    def update_progress_bar(self, progress):
        self.progress_bar.setValue(progress)

app = QApplication(sys.argv)
browser = BrowserWindow()
browser.show()
browser.load_url()
sys.exit(app.exec_())
