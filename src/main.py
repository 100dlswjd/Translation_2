import sys

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PySide6.QtCore import Slot, Qt, QObject, Signal
from PySide6.QtGui import QCloseEvent

from ui.main_form import Ui_MainWindow

from threading import Thread, Event

class Msg_signal(QObject):
    msg = Signal(str)

class Trans_signal(QObject):
    transaltion = Signal(str)

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

        # 콤보 박스 관련
        self.comboBox.currentIndexChanged.connect(self.comboBox_change_handler)
        self.after_language = self.LANGUAGE_DIC[self.comboBox.currentText()]

        # 버튼 핸들러
        self.pushButton_select_chrome_driver.clicked.connect(self.btn_select_chrome_driver_handler)
        self.pushButton_translation.clicked.connect(self.btn_translation_handler)

        # 번역 시그널
        self.papago_transaltion_completion = Trans_signal()
        self.google_transaltion_completion = Trans_signal()
        self.papago_transaltion_completion.transaltion.connect(self.papago_trans_completion_handler)
        self.google_transaltion_completion.transaltion.connect(self.google_trans_completion_handler)

        # 메시지 시그널
        self.msg_signal = Msg_signal()
        self.msg_signal.msg.connect(self.msg_signal_handler)

        # 클립보드 이벤트
        self.clip = QApplication.clipboard()
        self.clip.dataChanged.connect(self.clip_dataChanged_handler)

        # 쓰레드
        self.work_thread = Thread(target = self.work_proc, args= (self.papago_transaltion_completion, self.google_transaltion_completion, self.msg_signal))
        self.exit_event = Event()
        self.wait_event = Event()
        self.exit_event.set()
        self.wait_event.clear()
        self.work_thread.start()

    def work_proc(self, papago_signal : Trans_signal, google_signal : Trans_signal, msg_signal : Msg_signal):
        while self.wait_event.is_set() == False:
            while self.exit_event.is_set() == False:
                try:
                    msg_signal.msg.emit("번역중입니다.")
                    papago_translation_text = self.papago_translation()
                    google_translation_text = self.google_translation()
                    papago_signal.transaltion.emit(papago_translation_text)
                    google_signal.transaltion.emit(google_translation_text)
                    msg_signal.msg.emit("완료")
                    self.exit_event.set()
                except OSError:
                    msg_signal.msg.emit("크롬 드라이버를 선택해주세요")
                    self.exit_event.set()
                except:
                    msg_signal.msg.emit("버그가 발생하였습니다\n다시 시도해주세요")
                    self.exit_event.set()

    @Slot()
    def comboBox_change_handler(self):
        self.after_language = self.LANGUAGE_DIC[self.comboBox.currentText()]

    @Slot(str)
    def papago_trans_completion_handler(self, text : str):
        self.textBrowser_papago.setText(text)

    @Slot(str)
    def google_trans_completion_handler(self, text : str):
        self.textBrowser_google.setText(text)

    @Slot(str)
    def msg_signal_handler(self, text):
        self.label_info.setText(text)

    @Slot()
    def clip_dataChanged_handler(self):
        if self.checkBox_auto.checkState() == Qt.CheckState.Checked:
            self.textEdit_translation_before.setText(self.clip.text())
            self.pushButton_translation.click()

    @Slot()
    def btn_select_chrome_driver_handler(self):
        file = QFileDialog.getOpenFileName(caption = "크롬 드라이버 선택", filter= "크롬 드라이버 (*.exe)")
        if file[0]:
            self.label_select_chrome_driver.setText(file[0])
            self.chrome_driver_path = file[0]

    @Slot()
    def btn_translation_handler(self):
        self.exit_event.clear()

    def papago_translation(self) -> str:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        if not self.driver_papago:
            self.driver_papago = webdriver.Chrome(executable_path=self.chrome_driver_path, options=options)

        url = "https://papago.naver.com/?sk=auto&tk="+ self.after_language + "&st=" + self.textEdit_translation_before.toPlainText()
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

        url = "https://translate.google.co.kr/?hl=ko&tab=rT&sl=auto&tl=" + self.after_language + "&text=" + self.textEdit_translation_before.toPlainText() + "&op=translate"
        self.driver_google.get(url)
        wait = WebDriverWait(self.driver_google, 10)
        x_path = '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[8]/div/div[1]/span[1]/span/span'
        elem = wait.until(EC.presence_of_element_located((By.XPATH, x_path)))
        if elem:
            translation = self.driver_google.find_element(By.XPATH,x_path).text
            return str(translation)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.exit_event.set()
        self.wait_event.set()
        self.work_thread.join(3)
        if self.driver_google:
            self.driver_google.close()
        if self.driver_papago:
            self.driver_papago.close()
        return super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    app.setStyle('Fusion')
    app.exec()