import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QToolBar, QAction, QStatusBar
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QLineEdit for the address bar
        self.address_bar = QLineEdit(self)
        self.address_bar.returnPressed.connect(self.load_url)

        # Create a QToolBar to hold the address bar and navigation buttons
        self.toolbar = QToolBar(self)
        self.toolbar.addWidget(self.address_bar)

        # Create a QWebEngineView to display the web pages
        self.web_engine_view = QWebEngineView(self)
        self.web_engine_view.loadFinished.connect(self.update_address_bar)

        # Create back and forward buttons
        self.back_button = QAction("Back", self)
        self.back_button.triggered.connect(self.web_engine_view.back)
        self.toolbar.addAction(self.back_button)

        self.forward_button = QAction("Forward", self)
        self.forward_button.triggered.connect(self.web_engine_view.forward)
        self.toolbar.addAction(self.forward_button)

        # Create a progress bar
        self.progress_bar = QStatusBar(self)

        # Add the toolbar and web view to the main window
        self.addToolBar(self.toolbar)
        self.setCentralWidget(self.web_engine_view)
        self.setStatusBar(self.progress_bar)

    def load_url(self):
        url = QUrl(self.address_bar.text())
        self.web_engine_view.load(url)

    def update_address_bar(self, success):
        if success:
            self.address_bar.setText(self.web_engine_view.url().toString())

app = QApplication(sys.argv)
browser = BrowserWindow()
browser.show()
sys.exit(app.exec_())
