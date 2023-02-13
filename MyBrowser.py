import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QToolBar, QAction, QStatusBar, QProgressBar
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage


class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.line_edit = QLineEdit()
        self.line_edit.returnPressed.connect(self.load_url)

        self.tool_bar = QToolBar()
        self.addToolBar(self.tool_bar)

        self.back_button = QAction("Back")
        self.back_button.triggered.connect(self.web_engine_view.back)
        self.tool_bar.addAction(self.back_button)

        self.forward_button = QAction("Forward")
        self.forward_button.triggered.connect(self.web_engine_view.forward)
        self.tool_bar.addAction(self.forward_button)

        self.tool_bar.addWidget(self.line_edit)

        self.web_engine_view = QWebEngineView()
        self.setCentralWidget(self.web_engine_view)
        self.web_engine_view.loadFinished.connect(self.update_url)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.status_bar.addPermanentWidget(self.progress_bar)

        self.web_engine_view.loadProgress.connect(self.update_progress)

    def load_url(self):
        url = self.line_edit.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.web_engine_view.setUrl(QUrl(url))

    def update_url(self):
        self.line_edit.setText(self.web_engine_view.url().toString())

    def update_progress(self, progress):
        self.progress_bar.setValue(progress)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = BrowserWindow()
    browser.show()
    sys.exit(app.exec_())
