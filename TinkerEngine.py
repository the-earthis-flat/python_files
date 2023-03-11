import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://duckduckgo.com/?t=ffab&q='))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        fw_btn = QAction('Forward', self)
        fw_btn.triggered.connect(self.browser.forward)
        navbar.addAction(fw_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.gohome)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_url)
        navbar.addWidget(self.url_bar)

        chrm_btn = QAction('   Chrome ', self)
        chrm_btn.triggered.connect(self.chrome_tab)
        navbar.addAction(chrm_btn)

        qwant_btn = QAction(' Qwant ', self)
        qwant_btn.triggered.connect(self.qwant_tab)
        navbar.addAction(qwant_btn)

    def navigate_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
        #a = self.browser.setUrl(QUrl('https://duckduckgo.com/?t=ffab&q='))
        #b = self.browser.setUrl(QUrl('https://google.com/?t=ffab&q='))
        #c = self.browser.setUrl(QUrl('https://www.qwant.com/?q='))
#-----------------------------------------------------------------------------------
        #if a == self.browser.setUrl(QUrl('https://duckduckgo.com/?t=ffab&q=')):
            #c
#-----------------------------------------------------------------------------------
        #if b == self.browser.setUrl(QUrl('https://google.com/?t=ffab&q=')):
            #self.browser.setUrl(QUrl('https://google.com/?t=ffab&q='+url+" "))
#-----------------------------------------------------------------------------------
        #if c == self.browser.setUrl(QUrl('https://www.qwant.com/?q=')):
            #self.browser.setUrl(QUrl('https://www.qwant.com/?q='+url+" "))
#-----------------------------------------------------------------------------------

    def gohome(self):
        self.browser.setUrl(QUrl('https://duckduckgo.com/?t=ffab&q='))

    def chrome_tab(self):
        self.browser.setUrl(QUrl('https://google.com/?t=ffab&q='))

    def qwant_tab(self):
        self.browser.setUrl(QUrl('https://www.qwant.com/?q='))

app = QApplication(sys.argv)
QApplication.setApplicationName("TinkerEngine")  
window = MainWindow()
app.exec_()