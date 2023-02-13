import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QToolBar, QAction, QStatusBar, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QWebEngineView to display the web content
        self.web_view = QWebEngineView()
        self.setCentralWidget(self.web_view)

        # Create a URL address bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self._load_url)

        # Create a back button
        self.back_button = QAction("<", self)
        self.back_button.triggered.connect(self.web_view.back)

        # Create a forward button
        self.forward_button = QAction(">", self)
        self.forward_button.triggered.connect(self.web_view.forward)

        # Add the URL address bar and the back and forward buttons to the toolbar
        toolbar = QToolBar()
        toolbar.addAction(self.back_button)
        toolbar.addAction(self.forward_button)
        toolbar.addWidget(self.url_bar)
        self.addToolBar(toolbar)

        # Create a progress bar and add it to the status bar
        self.progress_bar = QStatusBar()
        self.setStatusBar(self.progress_bar)

        # Connect the loadStarted and loadFinished signals to the appropriate slots
        self.web_view.loadStarted.connect(self._on_load_started)
        self.web_view.loadFinished.connect(self._on_load_finished)

        # Connect the urlChanged signal to the _update_url_bar slot
        self.web_view.page().urlChanged.connect(self._update_url_bar)

    def _load_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.web_view.load(QUrl(url))

    def _on_load_started(self):
        self.progress_bar.show()

    def _on_load_finished(self, success):
        self.progress_bar.hide()
        # if not success:
        #     self.web_view.setHtml("Failed to load page")

    def _update_url_bar(self, url):
        self.url_bar.setText(url.toString())
        self.url_bar.setCursorPosition(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = BrowserWindow()
    browser.show()
    sys.exit(app.exec_())
