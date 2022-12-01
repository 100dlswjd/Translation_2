import sys

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QCloseEvent

from ui.main_form import Ui_MainWindow

from threading import Thread, Event

class Mainwindow(QMainWindow, Ui_MainWindow):
    LANGUAGE_DIC = {"한국어" : "ko"
                , "영어" : "en"
                , "중국어(간체)" : "zh-CN"
                , "중국어(번체)" : "zh-TW"
                , "일본어": "ja" }
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.setupUi(self)
        self.chrome_driver_path = ""
        self.driver_papago = False
        self.driver_google = False

        # 버튼 핸들러
        self.pushButton_select_chrome_driver.clicked.connect(self.btn_select_chrome_driver_handler)
        self.pushButton_translation.clicked.connect(self.btn_translation_handler)

        self.clip = QApplication.clipboard()
        self.clip.dataChanged.connect(self.clip_dataChanged_handler)

    @Slot()
    def clip_dataChanged_handler(self):
        if self.checkBox_auto.checkState() == Qt.CheckState.Checked:
            self.textEdit_translation_before.setText(self.clip.text())

    @Slot()
    def btn_select_chrome_driver_handler(self):
        file = QFileDialog.getOpenFileName(caption = "크롬 드라이버 선택", filter= "크롬 드라이버 (*.exe)")
        if file[0]:
            self.label_select_chrome_driver.setText(file[0])
            self.chrome_driver_path = file[0]

    @Slot()
    def btn_translation_handler(self):
        papago_text = self.papago_translation()
        self.textBrowser_papago.setText(papago_text)
        google_text = self.google_translation()
        self.textBrowser_google.setText(google_text)
        pass

    def papago_translation(self) -> str:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        if not self.driver_papago:
            self.driver_papago = webdriver.Chrome(executable_path=self.chrome_driver_path, options=options)

        url = 'https://papago.naver.com/?sk=auto&tk=ko&st=' + self.textEdit_translation_before.toPlainText()
        self.driver_papago.get(url)
        wait = WebDriverWait(self.driver_papago, 10)
        elem = wait.until(EC.presence_of_element_located((By.ID, 'txtTarget')))
        if elem:
            html = self.driver_papago.page_source
            soup = BeautifulSoup(html, 'html.parser')
            translation = soup.find_all(id = "txtTarget")
            return str(translation[0].text)

    def google_translation(self) -> str:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        if not self.driver_google:
            self.driver_google = webdriver.Chrome(executable_path=self.chrome_driver_path, options=options)

        url = "https://translate.google.co.kr/?hl=ko&tab=rT&sl=auto&tl=ko&text=" + self.textEdit_translation_before.toPlainText() + "&op=translate"
        self.driver_google.get(url)
        wait = WebDriverWait(self.driver_google, 10)
        x_path = '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[8]/div/div[1]/span[1]/span/span'
        elem = wait.until(EC.presence_of_element_located((By.XPATH, x_path)))
        if elem:
            translation = self.driver_google.find_element(By.XPATH,x_path).text
            return str(translation)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    app.setStyle('Fusion')
    app.exec()