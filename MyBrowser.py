import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QHBoxLayout, QVBoxLayout, QAction, QToolBar, QProgressBar
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage


class WebEngineView(QWebEngineView):
    def __init__(self, parent=None):
        super().__init__(parent)

    def createWindow(self, windowType):
        return self.parent().create_new_window()


class BrowserWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widget = QWebEngineView()
        self.setCentralWidget(self.central_widget)

        self.address_bar = QLineEdit()
        self.address_bar.returnPressed.connect(self.load_url)

        self.toolbar = QToolBar()
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)

        self.back_button = QAction("<")
        self.back_button.triggered.connect(self.central_widget.back)
        self.toolbar.addAction(self.back_button)

        self.forward_button = QAction(">")
        self.forward_button.triggered.connect(self.central_widget.forward)
        self.toolbar.addAction(self.forward_button)

        self.toolbar.addWidget(self.address_bar)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.progress_bar.hide()

        self.status_bar = self.statusBar()
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.load_url)
        self.status_bar.addWidget(self.url_bar)


        self.status_bar().addPermanentWidget(self.progress_bar)
        self.central_widget.loadProgress.connect(self.update_progress)

        self.central_widget.urlChanged.connect(self.update_address_bar)

    def load_url(self):
        url = self.url_bar.text()
        self.web_engine_view.load(QUrl(url))

    def update_progress(self, progress):
        if progress == 100:
            self.progress_bar.hide()
        else:
            self.progress_bar.show()
        self.progress_bar.setValue(progress)

    def update_address_bar(self, url):
        self.address_bar.setText(url.toString())
        self.address_bar.setCursorPosition(0)

    def create_new_window(self):
        new_window = BrowserWindow()
        new_window.show()
        return new_window.central_widget


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec_())
