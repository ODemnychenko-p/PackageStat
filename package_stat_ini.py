import sys
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from UI import package_stat_ui

class PackageStat(package_stat_ui.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(PackageStat, self).__init__()
        self.setupUi(self)

        self.btn_start.clicked.connect(lambda: self.on_click_start())
        self.btn_package_dir.clicked.connect(
            lambda: self.fld_package_dir.setText(self.on_click_get_path(self.fld_package_dir.text())))
        self.fld_tag.returnPressed.connect(lambda: self.enter_pressed())

    def enter_pressed(self):
        self.fld_tag.setText(self.fld_tag.text().strip() + ":")

    def on_click_start(self):
        if self.fld_tag.text() != "" and self.fld_package_dir.text() != "":
            masks = self.fld_tag.text().strip().split(":")
            statistic = Statistic(self.fld_package_dir.text().strip(), masks)
            self.statusbar.showMessage(statistic.getAllMasksSizes(), 3000)
        else:
            self.statusbar.showMessage("Fields must not be empty!", 3000)
    def on_click_get_path(self, start_dir = "" ):
        return QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory", start_dir.replace("\n", ""))

    def closeEvent(self, event):
        messagebox = QtWidgets.QMessageBox()
        messagebox.setIcon(QtWidgets.QMessageBox.Question)
        messagebox.setWindowTitle('Exit')
        messagebox.setText('Are you sure, you want to quit?')
        messagebox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        messagebox.setStyleSheet(
            "QLabel {color: rgb(203, 203, 203); }"
            "QMessageBox { background-color: rgb(81, 81, 81); }"
            "QPushButton { /* all types of tool button */\n"
            "    color: rgb(80, 80, 80);\n"
            "     border-left:1px solid rgb(75, 75, 75);\n"
            "    border-radius: 5px;\n"
            "    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(111, 111, 111, 255), stop:1 rgba(155, 155, 155, 255));\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(203, 203, 203, 255));\n"
            "}\n"
            "QPushButton:hover {\n"
            "    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(203, 203, 203, 255));\n"
            "}")
        buttonY = messagebox.button(QtWidgets.QMessageBox.Yes)
        buttonN = messagebox.button(QtWidgets.QMessageBox.No)
        buttonN.setFixedWidth(50)
        buttonY.setFixedWidth(50)
        buttonY.setFixedHeight(15)
        buttonN.setFixedHeight(15)
        res = messagebox.exec_()
        if res == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

class Statistic:
    def __init__(self, package_path, masks):
        self.package_path = package_path
        self.masks = masks
        self.size = 0
        self.out = {}
        self.all_size_for_mask = {}

    def getFolderSizeForMask(self, path):
        result = 0
        for dir, subdir, files in os.walk(path):
            for file in files:
                file_path = os.path.join(dir, file)
                result += os.path.getsize(file_path)
        return result

    def getAllMasksSizes(self):
        for dir in os.listdir(self.package_path):
            self.out[dir] = {}
            for mask in self.masks:
                self.out[dir][mask] = ""
                self.all_size_for_mask[mask] = 0
                for dirname, subdirs, files in os.walk(os.path.join(self.package_path, dir)):
                    if mask in subdirs:
                        self.size += self.getFolderSizeForMask(os.path.join(dirname, mask))
                self.out[dir][mask] = self.size/1000000
                self.size = 0

        with open("stat.txt", "w") as stat:
            for key in self.out:
                stat.write("{0}: \n".format(key))
                for k in self.out[key]:
                    stat.write("\t{0} = {1}Mb\n".format(k, self.out[key][k]))
                    self.all_size_for_mask[k] += self.out[key][k]
            stat.write("Total size:\n")
            for m in self.all_size_for_mask:
                stat.write("\t{0} = {1}Mb\n".format(m, self.all_size_for_mask[m]))
        return "Complete!"

if __name__=='__main__':
    qapp = QtWidgets.QApplication(sys.argv)
    package_stat = PackageStat()
    package_stat.show()
    qapp.exec_()