# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'umbcproject.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from process import DataProcessing
import pandas as pd
import datetime, time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1043, 860)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBoxType1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxType1.setGeometry(QtCore.QRect(260, 160, 111, 27))
        self.comboBoxType1.setObjectName("comboBoxType1")
        self.comboBoxType1.addItem("")
        self.comboBoxType1.setItemText(0, "")
        self.comboBoxType1.addItem("")
        self.comboBoxType1.addItem("")
        self.comboBoxType1.addItem("")
        self.comboBoxType1.addItem("")
        self.comboBoxType1.addItem("")
        self.comboBoxType1.addItem("")
        self.comboBoxType1.addItem("")
        self.comboBoxType1.addItem("")
        self.comboBoxType1.addItem("")
        self.comboBoxType1.addItem("")
        self.comboBoxType1.addItem("")
        self.comboBoxType1.addItem("")
        self.comboBoxType1.addItem("")
        self.comboBoxType1.addItem("")
        self.comboBoxType1.addItem("")
        ####################### get selected value for type1###############
        #self.comboBoxType1.currentIndexChanged.connect(self.selectionchange)
        ####################################################################
        self.comboBoxType2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxType2.setGeometry(QtCore.QRect(480, 160, 101, 27))
        self.comboBoxType2.setObjectName("comboBoxType2")
        self.comboBoxType2.addItem("")
        self.comboBoxType2.setItemText(0, "")
        self.comboBoxType2.addItem("")
        self.comboBoxType2.addItem("")
        self.comboBoxType2.addItem("")
        self.comboBoxType2.addItem("")
        self.comboBoxType2.addItem("")
        self.comboBoxType2.addItem("")
        self.comboBoxType2.addItem("")
        self.comboBoxType2.addItem("")
        self.comboBoxType2.addItem("")
        self.comboBoxType2.addItem("")
        self.comboBoxType2.addItem("")
        self.comboBoxType2.addItem("")
        self.comboBoxType2.addItem("")
        self.comboBoxType2.addItem("")
        self.comboBoxType2.addItem("")
        ####################### get selected value for type2 ###############
        self.comboBoxType2.currentIndexChanged.connect(self.selectionchange)
        ####################################################################
        self.comboBoxType3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxType3.setGeometry(QtCore.QRect(700, 160, 101, 27))
        self.comboBoxType3.setObjectName("comboBoxType3")
        self.comboBoxType3.addItem("")
        self.comboBoxType3.setItemText(0, "")
        self.comboBoxType3.addItem("")
        self.comboBoxType3.addItem("")
        self.comboBoxType3.addItem("")
        self.comboBoxType3.addItem("")
        self.comboBoxType3.addItem("")
        self.comboBoxType3.addItem("")
        self.comboBoxType3.addItem("")
        self.comboBoxType3.addItem("")
        self.comboBoxType3.addItem("")
        self.comboBoxType3.addItem("")
        self.comboBoxType3.addItem("")
        self.comboBoxType3.addItem("")
        self.comboBoxType3.addItem("")
        self.comboBoxType3.addItem("")
        self.comboBoxType3.addItem("")
        ####################### get selected value for type3 ###############
        self.comboBoxType3.currentIndexChanged.connect(self.selectionchange)
        ####################################################################
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 130, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 130, 121, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(710, 130, 101, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 60, 291, 61))
        self.label_4.setObjectName("label_4")
        self.pushButtonSearch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSearch.setGeometry(QtCore.QRect(890, 200, 101, 41))
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        ######################## Search button click ####################
        self.pushButtonSearch.clicked.connect(self.search)
        #################################################################
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(50, 260, 941, 471))
        self.tableView.setObjectName("tableView")
        self.pushButtonDownload = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDownload.setGeometry(QtCore.QRect(868, 760, 121, 51))
        self.pushButtonDownload.setObjectName("pushButtonDownload")
        ######################## Search button click ####################
        self.pushButtonDownload.clicked.connect(self.download)
        #################################################################
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1043, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBoxType1.setItemText(1, _translate("MainWindow", "SNP"))
        self.comboBoxType1.setItemText(2, _translate("MainWindow", "cellular component"))
        self.comboBoxType1.setItemText(3, _translate("MainWindow", "complex/PPI"))
        self.comboBoxType1.setItemText(4, _translate("MainWindow", "disease"))
        self.comboBoxType1.setItemText(5, _translate("MainWindow", "drug/chemical compound"))
        self.comboBoxType1.setItemText(6, _translate("MainWindow", "environment"))
        self.comboBoxType1.setItemText(7, _translate("MainWindow", "gene/protein"))
        self.comboBoxType1.setItemText(8, _translate("MainWindow", "gene/protein mutant"))
        self.comboBoxType1.setItemText(9, _translate("MainWindow", "mRNA/protein variant"))
        self.comboBoxType1.setItemText(10, _translate("MainWindow", "ncRNA/miRNA"))
        self.comboBoxType1.setItemText(11, _translate("MainWindow", "organism model"))
        self.comboBoxType1.setItemText(12, _translate("MainWindow", "phenotype"))
        self.comboBoxType1.setItemText(13, _translate("MainWindow", "process"))
        self.comboBoxType1.setItemText(14, _translate("MainWindow", "protein modification"))
        self.comboBoxType1.setItemText(15, _translate("MainWindow", "tissue/cell line"))
        self.comboBoxType2.setItemText(1, _translate("MainWindow", "SNP"))
        self.comboBoxType2.setItemText(2, _translate("MainWindow", "cellular component"))
        self.comboBoxType2.setItemText(3, _translate("MainWindow", "complex/PPI"))
        self.comboBoxType2.setItemText(4, _translate("MainWindow", "disease"))
        self.comboBoxType2.setItemText(5, _translate("MainWindow", "drug/chemical compound"))
        self.comboBoxType2.setItemText(6, _translate("MainWindow", "environment"))
        self.comboBoxType2.setItemText(7, _translate("MainWindow", "gene/protein"))
        self.comboBoxType2.setItemText(8, _translate("MainWindow", "gene/protein mutant"))
        self.comboBoxType2.setItemText(9, _translate("MainWindow", "mRNA/protein variant"))
        self.comboBoxType2.setItemText(10, _translate("MainWindow", "ncRNA/miRNA"))
        self.comboBoxType2.setItemText(11, _translate("MainWindow", "organism model"))
        self.comboBoxType2.setItemText(12, _translate("MainWindow", "phenotype"))
        self.comboBoxType2.setItemText(13, _translate("MainWindow", "process"))
        self.comboBoxType2.setItemText(14, _translate("MainWindow", "protein modification"))
        self.comboBoxType2.setItemText(15, _translate("MainWindow", "tissue/cell line"))
        self.comboBoxType3.setItemText(1, _translate("MainWindow", "SNP"))
        self.comboBoxType3.setItemText(2, _translate("MainWindow", "cellular component"))
        self.comboBoxType3.setItemText(3, _translate("MainWindow", "complex/PPI"))
        self.comboBoxType3.setItemText(4, _translate("MainWindow", "disease"))
        self.comboBoxType3.setItemText(5, _translate("MainWindow", "drug/chemical compound"))
        self.comboBoxType3.setItemText(6, _translate("MainWindow", "environment"))
        self.comboBoxType3.setItemText(7, _translate("MainWindow", "gene/protein"))
        self.comboBoxType3.setItemText(8, _translate("MainWindow", "gene/protein mutant"))
        self.comboBoxType3.setItemText(9, _translate("MainWindow", "mRNA/protein variant"))
        self.comboBoxType3.setItemText(10, _translate("MainWindow", "ncRNA/miRNA"))
        self.comboBoxType3.setItemText(11, _translate("MainWindow", "organism model"))
        self.comboBoxType3.setItemText(12, _translate("MainWindow", "phenotype"))
        self.comboBoxType3.setItemText(13, _translate("MainWindow", "process"))
        self.comboBoxType3.setItemText(14, _translate("MainWindow", "protein modification"))
        self.comboBoxType3.setItemText(15, _translate("MainWindow", "tissue/cell line"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Select Type</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Select Type</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Select Type</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Search Database</span></p></body></html>"))
        self.pushButtonSearch.setText(_translate("MainWindow", "Search"))
        self.pushButtonDownload.setText(_translate("MainWindow", "Download CSV"))

    #get selected fields from combobox
    def selectionchange(self):
        if(self.comboBoxType1.currentText() != None):
            self.type1 = self.comboBoxType1.currentText()
            

        if(self.comboBoxType2.currentText() != None):
            self.type2 = self.comboBoxType2.currentText()

        if(self.comboBoxType3.currentText() != None):
            self.type3 = self.comboBoxType3.currentText()

    #set combox value to class variable
    #calls DataProcessing class and carrys out the dataframe processing
    #returns dataframe back
    def search(self):
        
        self.selectionchange()
        ls = [self.type1,self.type2,self.type3]
        ls2 = list(filter(None,ls))#remove emty string from list
        
        getClass = DataProcessing()
        self.processedData = getClass.process(ls2)
        model = PandasModel(self.processedData)
        #self.tableView.setHorizontalHeaderLabels(["Subject", "Subject type", "Object", "Object type","Disease"])
        self.tableView.setModel(model)
        
    #TO download as csv
    def download(self):
        if not self.processedData.empty:
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
            self.processedData.to_csv('data'+str(st)+'.csv')
            self.showMessage("Success","Download was succesful")

    def showMessage(self,title,msg):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(msg)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
        

#Class to polulate table
Qt = QtCore.Qt

class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return QtCore.QVariant(str(
                    self._data.values[index.row()][index.column()]))
        return QtCore.QVariant()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

