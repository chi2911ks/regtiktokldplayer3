from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from main import RegTikTokLD
from CBAutoHelper import LDPlayer

import os, time, subprocess
class Ui_RegTikTok(object):
    def setupUi(self, RegTikTok):
        RegTikTok.setObjectName("RegTikTok")
        RegTikTok.resize(806, 446)
        RegTikTok.setMaximumSize(QtCore.QSize(806, 446))
        RegTikTok.closeEvent = lambda event:self.closeEvent(event)
        self.centralwidget = QtWidgets.QWidget(RegTikTok)
        self.centralwidget.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.startreg = QtWidgets.QPushButton(self.centralwidget)
        self.startreg.setGeometry(QtCore.QRect(10, 180, 75, 23))
        self.startreg.setObjectName("startreg")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 210, 781, 221))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.settings = QtWidgets.QGroupBox(self.centralwidget)
        self.settings.setGeometry(QtCore.QRect(10, 10, 281, 161))
        self.settings.setStyleSheet("")
        self.settings.setObjectName("settings")
        self.label_2 = QtWidgets.QLabel(self.settings)
        self.label_2.setGeometry(QtCore.QRect(10, 52, 81, 23))
        self.label_2.setObjectName("label_2")
        self.delayopenld = QtWidgets.QSpinBox(self.settings)
        self.delayopenld.setGeometry(QtCore.QRect(90, 53, 41, 20))
        self.delayopenld.setMinimum(0)
        self.delayopenld.setMaximum(1000)
        self.delayopenld.setProperty("value", 25)
        self.delayopenld.setObjectName("delayopenld")
        self.threadcount = QtWidgets.QSpinBox(self.settings)
        self.threadcount.setGeometry(QtCore.QRect(90, 24, 41, 20))
        self.threadcount.setMinimum(1)
        self.threadcount.setMaximum(200)
        self.threadcount.setObjectName("threadcount")
        self.label = QtWidgets.QLabel(self.settings)
        self.label.setGeometry(QtCore.QRect(10, 23, 81, 23))
        self.label.setObjectName("label")
        self.randompass = QtWidgets.QCheckBox(self.settings)
        self.randompass.setGeometry(QtCore.QRect(190, 82, 71, 17))
        self.randompass.setChecked(True)
        self.randompass.setObjectName("randompass")
        self.password = QtWidgets.QLineEdit(self.settings)
        self.password.setEnabled(False)
        self.password.setGeometry(QtCore.QRect(80, 81, 106, 20))
        self.password.setObjectName("password")
        self.label_3 = QtWidgets.QLabel(self.settings)
        self.label_3.setGeometry(QtCore.QRect(10, 81, 61, 20))
        self.label_3.setObjectName("label_3")
        self.filedialogld = QtWidgets.QPushButton(self.settings)
        self.filedialogld.setGeometry(QtCore.QRect(250, 23, 30, 23))
        self.filedialogld.setMinimumSize(QtCore.QSize(30, 0))
        self.filedialogld.setMaximumSize(QtCore.QSize(30, 16777215))
        self.filedialogld.setObjectName("filedialogld")
        self.folderldplayer = QtWidgets.QLineEdit(self.settings)
        self.folderldplayer.setGeometry(QtCore.QRect(140, 24, 100, 20))
        self.folderldplayer.setMinimumSize(QtCore.QSize(100, 0))
        self.folderldplayer.setObjectName("folderldplayer")
        self.folderavt = QtWidgets.QLineEdit(self.settings)
        self.folderavt.setGeometry(QtCore.QRect(140, 53, 100, 20))
        self.folderavt.setMinimumSize(QtCore.QSize(100, 0))
        self.folderavt.setObjectName("folderavt")
        self.filedialogavt = QtWidgets.QPushButton(self.settings)
        self.filedialogavt.setGeometry(QtCore.QRect(250, 50, 30, 23))
        self.filedialogavt.setMinimumSize(QtCore.QSize(30, 0))
        self.filedialogavt.setMaximumSize(QtCore.QSize(30, 16777215))
        self.filedialogavt.setObjectName("filedialogavt")
        self.upavt = QtWidgets.QCheckBox(self.settings)
        self.upavt.setGeometry(QtCore.QRect(10, 110, 70, 17))
        self.upavt.setObjectName("upavt")
        self.publictim = QtWidgets.QCheckBox(self.settings)
        self.publictim.setGeometry(QtCore.QRect(90, 110, 81, 17))
        self.publictim.setObjectName("publictim")
        self.ldviewer = QtWidgets.QCheckBox(self.settings)
        self.ldviewer.setGeometry(QtCore.QRect(180, 110, 81, 17))
        self.ldviewer.setChecked(True)
        self.ldviewer.setObjectName("ldviewer")
        self.changename = QtWidgets.QCheckBox(self.settings)
        self.changename.setGeometry(QtCore.QRect(10, 130, 101, 17))
        self.changename.setObjectName("changename")
        self.proxy = QtWidgets.QGroupBox(self.centralwidget)
        self.proxy.setGeometry(QtCore.QRect(550, 10, 251, 161))
        self.proxy.setObjectName("proxy")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.proxy)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chooseproxy = QtWidgets.QComboBox(self.proxy)
        self.chooseproxy.setObjectName("chooseproxy")
        self.chooseproxy.addItems(["", "", "", ""])
        self.verticalLayout.addWidget(self.chooseproxy)
        self.listkeyproxy = QtWidgets.QPlainTextEdit(self.proxy)
        self.listkeyproxy.setEnabled(False)
        self.listkeyproxy.setFrameShape(QtWidgets.QFrame.Box)
        self.listkeyproxy.setLineWidth(1)
        self.listkeyproxy.setMidLineWidth(0)
        self.listkeyproxy.setObjectName("listkeyproxy")
        self.verticalLayout.addWidget(self.listkeyproxy)
        self.success = QtWidgets.QLabel(self.centralwidget)
        self.success.setGeometry(QtCore.QRect(110, 180, 101, 21))
        self.success.setObjectName("success")
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(220, 180, 91, 21))
        self.error.setObjectName("error")
        self.hotmail = QtWidgets.QGroupBox(self.centralwidget)
        self.hotmail.setGeometry(QtCore.QRect(300, 10, 241, 161))
        self.hotmail.setStyleSheet("")
        self.hotmail.setObjectName("hotmail")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.hotmail)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listhotmail = QtWidgets.QPlainTextEdit(self.hotmail)
        self.listhotmail.setFrameShape(QtWidgets.QFrame.Box)
        self.listhotmail.setObjectName("listhotmail")
        self.gridLayout_2.addWidget(self.listhotmail, 0, 0, 1, 1)
        self.counthotmail = QtWidgets.QLabel(self.centralwidget)
        self.counthotmail.setGeometry(QtCore.QRect(320, 180, 101, 21))
        self.counthotmail.setObjectName("counthotmail")
        RegTikTok.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegTikTok)
        QtCore.QMetaObject.connectSlotsByName(RegTikTok)

    def retranslateUi(self, RegTikTok):
        _translate = QtCore.QCoreApplication.translate
        RegTikTok.setWindowTitle(_translate("RegTikTok", "RegTikTok V1.0"))
        self.startreg.setText(_translate("RegTikTok", "Start"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("RegTikTok", "UserName"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("RegTikTok", "Password"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("RegTikTok", "Hotmail"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("RegTikTok", "Status"))
        self.settings.setTitle(_translate("RegTikTok", "Settings"))
        self.label_2.setText(_translate("RegTikTok", "DeleyOpenLD"))
        self.label.setText(_translate("RegTikTok", "ThreadCount"))
        self.randompass.setText(_translate("RegTikTok", "Random"))
        self.password.setText(_translate("RegTikTok", "CBcoder@2004"))
        self.label_3.setText(_translate("RegTikTok", "Password"))
        self.filedialogld.setText(_translate("RegTikTok", "..."))
        self.folderldplayer.setPlaceholderText(_translate("RegTikTok", "Folder LDPlayer"))
        self.folderavt.setPlaceholderText(_translate("RegTikTok", "Folder Avatar"))
        self.filedialogavt.setText(_translate("RegTikTok", "..."))
        self.upavt.setText(_translate("RegTikTok", "UpAvatar"))
        self.publictim.setText(_translate("RegTikTok", "Public Tim"))
        self.ldviewer.setText(_translate("RegTikTok", "LDViewer"))
        self.changename.setText(_translate("RegTikTok", "ChangeName"))
        self.proxy.setTitle(_translate("RegTikTok", "Proxy"))
        self.chooseproxy.setItemText(0, _translate("RegTikTok", "NoProxy"))
        self.chooseproxy.setItemText(1, _translate("RegTikTok", "Tinsoft"))
        self.chooseproxy.setItemText(2, _translate("RegTikTok", "TMProxy"))
        self.chooseproxy.setItemText(3, _translate("RegTikTok", "Proxy.shoplike.vn"))
        self.success.setText(_translate("RegTikTok", "<p><span style=\" color:#00aa00;\">Success: 0</span></p>"))
        self.error.setText(_translate("RegTikTok", "<p><span style=\" color:#ff0000;\">Error: 0</span></p>"))
        self.hotmail.setTitle(_translate("RegTikTok", "Hotmail"))
        self.listhotmail.setPlaceholderText(_translate("RegTikTok", "email|pass"))
        if self.LoadKey() != True: 
            os.remove('key.txt')
            sys.exit()
        self.counthotmail.setText(_translate("RegTikTok", "<p><span style=\" color:#00aa00;\">Hotmail: 0</span></p>"))
        self.Mesagebox(text="Tải <a href='https://www.ldplayer.net/other/version-history-and-release-notes.html?log=3'>LDPlayer 3.1.26</a></br><p style='color:red;'>Lưu ý: Phải bật ADB lên và chuyển LDPlayer về Tiếng Việt</p></br><p style='color:green;'>Cài đặt 3 file apk ở trong folder apk, muốn sử dụng nhiều luồng thì nhân bản cái đầu tiên ra</p>")
        self.indexsuccess = 0
        self.indexerror = 0
        self.listthread = []
        
        self.LoadData()
        self.filedialogavt.clicked.connect(self.FileDialogAvt)
        self.filedialogld.clicked.connect(self.FileDialogLD)
        self.listhotmail.textChanged.connect(self.SaveHotmail)
        self.listkeyproxy.textChanged.connect(self.SaveKeyProxy)
        self.chooseproxy.currentTextChanged.connect(self.EnableOrDisableListProxy)
        self.randompass.stateChanged.connect(self.EnableOrDisablePassword)
        self.startreg.clicked.connect(self.StartReg)
    def LoadKey(self):
        # import subprocess, requests
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= (
            subprocess.STARTF_USESTDHANDLES | subprocess.STARTF_USESHOWWINDOW
        )
        startupinfo.wShowWindow = subprocess.SW_HIDE
        code = str(subprocess.Popen('systeminfo', creationflags=subprocess.CREATE_NO_WINDOW, stdout=subprocess.PIPE, shell=False, startupinfo=startupinfo).stdout.read().decode("utf-8")).split('Product ID:                ')[1].split("\r\n")[0]
        print(code)
        if os.path.exists("key.txt") == False:
            text, ok = QtWidgets.QInputDialog().getText(self.centralwidget, "Nhập Key", f"Lấy mã máy rồi gửi chủ tool để lấy key(đã có thì xóa đi rồi nhập key):", text=code)
            if ok:
                open('key.txt', 'w').write(text)
            else: sys.exit()
        key = open('key.txt').read()
        keys = requests.get('https://pastebin.com/raw/hg8H7qbw').text
        for i in keys.splitlines():
            ma = i.split('|')
            print(ma)
            if code == ma[0] and key == ma[1]:
                open('key.txt', 'w').write(key)
                return True
    def closeEvent(self, event):
        sys.exit()
    def EnableOrDisableListProxy(self):
        if self.chooseproxy.currentText() != "NoProxy": self.listkeyproxy.setEnabled(True)
        else: self.listkeyproxy.setEnabled(False)
    def EnableOrDisablePassword(self):
        if self.randompass.isChecked(): self.password.setEnabled(False)
        else: self.password.setEnabled(True)
    def SaveKeyProxy(self):
        keys = self.listkeyproxy.toPlainText()
        open('./data/keyproxy.txt', 'w+').write(keys)
    def SaveHotmail(self):
        hotmail = self.listhotmail.toPlainText()
        self.counthotmail.setText(f"<p><span style=\" color:#00aa00;\">Hotmail: {len(hotmail.splitlines())}</span></p>")
        open('./data/hotmail.txt', 'w+').write(hotmail)
    def LoadData(self):
        if os.path.exists("./data/pathavt.txt"): self.folderavt.setText(open("./data/pathavt.txt").read())
        if os.path.exists("./data/pathld.txt"): self.folderldplayer.setText(open("./data/pathld.txt").read())
        if os.path.exists("./data/hotmail.txt"): self.listhotmail.setPlainText(open("./data/hotmail.txt").read())
        if os.path.exists("./data/keyproxy.txt"): self.listkeyproxy.setPlainText(open("./data/keyproxy.txt").read())
        hotmail = self.listhotmail.toPlainText()
        self.counthotmail.setText(f"<p><span style=\" color:#00aa00;\">Hotmail: {len(hotmail.splitlines())}</span></p>")
    def Mesagebox(self, title="Thông báo", text=""):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Warning)
        self.msg.setWindowTitle(title)
        self.msg.setText(text)
        self.msg.show()
    def FileDialogAvt(self):
        self.filepath = QtWidgets.QFileDialog()
        self.filepath.setFileMode(QtWidgets.QFileDialog.Directory)
        self.filepath.show()
        if self.filepath.exec_() == QtWidgets.QDialog.Accepted: 
            folder = self.filepath.selectedFiles()[0]
            self.folderavt.setText(folder)
            open("./data/pathavt.txt", "w+").write(folder)
    def FileDialogLD(self):
        self.filepath2 = QtWidgets.QFileDialog()
        self.filepath2.setFileMode(QtWidgets.QFileDialog.Directory)
        self.filepath2.show()
        if self.filepath2.exec_() == QtWidgets.QDialog.Accepted: 
            folder = self.filepath2.selectedFiles()[0]
            self.folderldplayer.setText(folder)
            open("./data/pathld.txt", "w+").write(folder)
    def LDViewer(self):
        from Viewer import Ui_LDPlayerViewer
        try: self.view 
        except:
            self.LDPlayerViewer = QtWidgets.QWidget()
            self.view = Ui_LDPlayerViewer()
            self.view.setupUi(self.LDPlayerViewer)
            self.LDPlayerViewer.show()
    def Delay(self, countdelay):
        loop = QtCore.QEventLoop()
        QtCore.QTimer.singleShot(int(countdelay*1000), loop.quit)
        loop.exec()
    def EnableStart(self): #Lười chưa muốn sửa lại, ở dưới nó xóa hết rồi đây vẫn có xóa
        self.startreg.setText('Start')
    def ShowTable(self, row, column, text):
        self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(text))
    def ChangeTextSuccessAndError(self, check, mail):
        self.listhotmail.setPlainText(self.listhotmail.toPlainText().replace(mail+"\n", '').replace(mail, ''))
        if check:
            self.indexsuccess += 1
            self.success.setText(f"<p><span style=\" color:#00aa00;\">Success: {self.indexsuccess}</span></p>")
        else:
            self.indexerror += 1
            self.error.setText(f"<p><span style=\" color:#ff0000;\">Error: {self.indexerror}</span></p>")
    def StartReg(self):
        if self.startreg.text() == "Start":
            if os.path.exists(self.folderldplayer.text()) == False:
                self.Mesagebox(text="Vui lòng nhập đúng folder LDPlayer!")
                return
            index = 0
            if self.ldviewer.isChecked(): self.LDViewer()
            self.listmail = self.listhotmail.toPlainText()

            keys = self.listkeyproxy.toPlainText().splitlines()
            if self.listmail == "":
                self.Mesagebox(text="Vui lòng nhập hotmail!")
                return
            self.listmail = iter(self.listmail.splitlines())
            self.startreg.setText("Stop")
            info = LDPlayer()
            info.pathLD = self.folderldplayer.text()
            listvm = info.GetDevices2()
            for vm in listvm:
                if index == self.threadcount.value():
                    break
                key = "" if len(keys) == index else keys[index] if self.chooseproxy.currentText() != "NoProxy" else ""
                self.threadreg = Reg(self, vm["index"], key)
                self.threadreg.start()
                self.threadreg.delete.connect(self.EnableStart)
                self.threadreg.show.connect(self.ShowTable)
                self.threadreg.checksuccess.connect(self.ChangeTextSuccessAndError)
                self.listthread.append(self.threadreg)
                index += 1
                # index2 += 1
                self.Delay(0.01)
        else:
            for thread in self.listthread: thread.Stop()
            self.startreg.setText('Start')
class Reg(QtCore.QThread):
    delete = QtCore.pyqtSignal()
    show = QtCore.pyqtSignal(int, int, str)
    checksuccess = QtCore.pyqtSignal(bool, str)
    def __init__(self, ref, index, key) -> None:
        super().__init__()
        self.ref = ref
        self.index = index
        self.key = key
    def Stop(self):
        try:
            self.reg.Stop()
        except: pass
        self.terminate()
    def run(self):
        while True:
            try: mail = next(self.ref.listmail)
            except: 
                self.delete.emit()
                return
            row = self.ref.tableWidget.rowCount()
            self.ref.tableWidget.insertRow(row)
            self.reg = RegTikTokLD(self.index, mail, self.key, row)
            self.reg.ref = self
            self.reg.run()
            time.sleep(10)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    RegTikTok = QtWidgets.QMainWindow()
    RegTikTok.setWindowIcon(QtGui.QIcon('icon.ico'))
    ui = Ui_RegTikTok()
    ui.setupUi(RegTikTok)
    RegTikTok.show()
    sys.exit(app.exec_())
# 7h15