# Form implementation generated from reading ui file 'C:\Users\almnar\OneDrive\Desktop\work space\PyQt6\Note Pad\NotePad.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(779, 560)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 779, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuFormat = QtWidgets.QMenu(self.menubar)
        self.menuFormat.setObjectName("menuFormat")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionNew = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"C:\Users\almnar\OneDrive\Desktop\work space\PyQt6\Note Pad\images/new.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(r"C:\Users\almnar\OneDrive\Desktop\work space\PyQt6\Note Pad\images/open.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(r"C:\Users\almnar\OneDrive\Desktop\work space\PyQt6\Note Pad\images/save.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionPrint = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(r"C:\Users\almnar\OneDrive\Desktop\work space\PyQt6\Note Pad\images/print.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionPrint.setIcon(icon3)
        self.actionPrint.setObjectName("actionPrint")
        self.actionPrint_Preview = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(r"C:\Users\almnar\OneDrive\Desktop\work space\PyQt6\Note Pad\images/printprev.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionPrint_Preview.setIcon(icon4)
        self.actionPrint_Preview.setObjectName("actionPrint_Preview")
        self.actionExport_PDF = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(r"C:\Users\almnar\OneDrive\Desktop\work space\PyQt6\Note Pad\images/pdf.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionExport_PDF.setIcon(icon5)
        self.actionExport_PDF.setObjectName("actionExport_PDF")
        self.actionQiet = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(r"C:\Users\almnar\OneDrive\Desktop\work space\PyQt6\Note Pad\images/exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionQiet.setIcon(icon6)
        self.actionQiet.setObjectName("actionQiet")
        self.actionUndo = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(r"C:\Users\almnar\OneDrive\Desktop\work space\PyQt6\Note Pad\images/undo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionUndo.setIcon(icon7)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(r"C:\Users\almnar\OneDrive\Desktop\work space\PyQt6\Note Pad\images/redo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionRedo.setIcon(icon8)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(r"C:\Users\almnar\OneDrive\Desktop\work space\PyQt6\Note Pad\images/cut.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCut.setIcon(icon9)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(r"C:\Users\almnar\OneDrive\Desktop\work space\PyQt6\Note Pad\images/copy.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCopy.setIcon(icon10)
        self.actionCopy.setObjectName("actionCopy")
        self.actionBold = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(r"C:\Users\almnar\OneDrive\Desktop\work space\PyQt6\Note Pad\images/bold.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionBold.setIcon(icon11)
        self.actionBold.setObjectName("actionBold")
        self.actionItalic = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(r"C:\Users\almnar\OneDrive\Desktop\work space\PyQt6\Note Pad\images/italic.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionItalic.setIcon(icon12)
        self.actionItalic.setObjectName("actionItalic")
        self.actionUnder_Line = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(r"C:\Users\almnar\OneDrive\Desktop\work space\PyQt6\Note Pad\images/underline.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionUnder_Line.setIcon(icon13)
        self.actionUnder_Line.setObjectName("actionUnder_Line")
        self.actionLeft = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(r"C:\Users\almnar\OneDrive\Desktop\work space\PyQt6\Note Pad\images/left.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionLeft.setIcon(icon14)
        self.actionLeft.setObjectName("actionLeft")
        self.actionRight = QtGui.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(r"C:\Users\almnar\OneDrive\Desktop\work space\PyQt6\Note Pad\images/right.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionRight.setIcon(icon15)
        self.actionRight.setObjectName("actionRight")
        self.actionCenter = QtGui.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(r"C:\Users\almnar\OneDrive\Desktop\work space\PyQt6\Note Pad\images/center.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCenter.setIcon(icon16)
        self.actionCenter.setObjectName("actionCenter")
        self.actionJustify = QtGui.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(r"C:\Users\almnar\OneDrive\Desktop\work space\PyQt6\Note Pad\images/justify.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionJustify.setIcon(icon17)
        self.actionJustify.setObjectName("actionJustify")
        self.actionFont = QtGui.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(r"C:\Users\almnar\OneDrive\Desktop\work space\PyQt6\Note Pad\images/font.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionFont.setIcon(icon18)
        self.actionFont.setObjectName("actionFont")
        self.actionColor = QtGui.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(r"C:\Users\almnar\OneDrive\Desktop\work space\PyQt6\Note Pad\images/color.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionColor.setIcon(icon19)
        self.actionColor.setObjectName("actionColor")
        self.actionAbout_App = QtGui.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(r"C:\Users\almnar\OneDrive\Desktop\work space\PyQt6\Note Pad\images/about.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionAbout_App.setIcon(icon20)
        self.actionAbout_App.setObjectName("actionAbout_App")
        self.actionPaste = QtGui.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(r"C:\Users\almnar\OneDrive\Desktop\work space\PyQt6\Note Pad\images/paste.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionPaste.setIcon(icon21)
        self.actionPaste.setObjectName("actionPaste")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionPrint_Preview)
        self.menuFile.addAction(self.actionExport_PDF)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQiet)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuFormat.addAction(self.actionBold)
        self.menuFormat.addAction(self.actionItalic)
        self.menuFormat.addAction(self.actionUnder_Line)
        self.menuFormat.addSeparator()
        self.menuFormat.addAction(self.actionLeft)
        self.menuFormat.addAction(self.actionRight)
        self.menuFormat.addAction(self.actionCenter)
        self.menuFormat.addAction(self.actionJustify)
        self.menuFormat.addSeparator()
        self.menuFormat.addAction(self.actionFont)
        self.menuFormat.addAction(self.actionColor)
        self.menuAbout.addAction(self.actionAbout_App)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuFormat.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionPrint)
        self.toolBar.addAction(self.actionPrint_Preview)
        self.toolBar.addAction(self.actionExport_PDF)
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addAction(self.actionUndo)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NotePad App"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuFormat.setTitle(_translate("MainWindow", "Format"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionPrint.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionPrint_Preview.setText(_translate("MainWindow", "Print Preview"))
        self.actionPrint_Preview.setShortcut(_translate("MainWindow", "Ctrl+Shift+P"))
        self.actionExport_PDF.setText(_translate("MainWindow", "Export PDF"))
        self.actionExport_PDF.setShortcut(_translate("MainWindow", "Ctrl+Shift+O"))
        self.actionQiet.setText(_translate("MainWindow", "Quit"))
        self.actionQiet.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionBold.setText(_translate("MainWindow", "Bold"))
        self.actionBold.setShortcut(_translate("MainWindow", "Ctrl+B"))
        self.actionItalic.setText(_translate("MainWindow", "Italic"))
        self.actionItalic.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionUnder_Line.setText(_translate("MainWindow", "Under Line"))
        self.actionUnder_Line.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionLeft.setText(_translate("MainWindow", "Left"))
        self.actionLeft.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionRight.setText(_translate("MainWindow", "Right"))
        self.actionRight.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionCenter.setText(_translate("MainWindow", "Center"))
        self.actionCenter.setShortcut(_translate("MainWindow", "Ctrl+Space"))
        self.actionJustify.setText(_translate("MainWindow", "Justify"))
        self.actionJustify.setShortcut(_translate("MainWindow", "Ctrl+J"))
        self.actionFont.setText(_translate("MainWindow", "Font"))
        self.actionColor.setText(_translate("MainWindow", "Color"))
        self.actionAbout_App.setText(_translate("MainWindow", "About App"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
