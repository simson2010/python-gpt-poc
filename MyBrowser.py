import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QToolBar, QAction, QVBoxLayout, QProgressBar
from PyQt5.QtCore import Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile

class MyBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QLineEdit for the address bar
        self.address_bar = QLineEdit()

        # Create a QWebEngineView for displaying the web page
        self.web_view = QWebEngineView()

        # Connect the address bar to the web view's load function
        self.address_bar.returnPressed.connect(self.load_url)

        # Create a progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)

        # Create a QToolBar and add the address bar, back button, and forward button
        tool_bar = QToolBar()
        tool_bar.addWidget(self.address_bar)

        back_action = QAction("<", self)
        back_action.triggered.connect(self.web_view.back)
        tool_bar.addAction(back_action)

        forward_action = QAction(">", self)
        forward_action.triggered.connect(self.web_view.forward)
        tool_bar.addAction(forward_action)

        # Add the tool bar and web view to the main window
        layout = QVBoxLayout()
        layout.addWidget(tool_bar)
        layout.addWidget(self.web_view)
        layout.addWidget(self.progress_bar)

        central_widget = QMainWindow()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def load_url(self):
        url = self.address_bar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.web_view.load(QUrl(url))

    def update_title(self):
        title = self.web_view.page().title()
        self.setWindowTitle("My Browser - " + title)

    def update_url(self, url):
        self.address_bar.setText(url.toString())
        self.update_title()

    def update_load_progress(self, progress):
        self.progress_bar.setValue(progress)
        if progress == 100:
            self.progress_bar.setVisible(False)
        else:
            self.progress_bar.setVisible(True)

app = QApplication(sys.argv)
browser = MyBrowser()
browser.show()
sys.exit(app.exec_())
