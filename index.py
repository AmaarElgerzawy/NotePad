from NotePad import Ui_MainWindow
from PyQt6.QtWidgets import *
from PyQt6.QtPrintSupport import QPrinter , QPrintDialog,QPrintPreviewDialog
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys

class indexNoteOad(QMainWindow, Ui_MainWindow):
  def __init__(self) -> None:
    super().__init__()
    self.setupUi(self)
    self.show()

    self.actionSave.triggered.connect(self.save_file)
    self.actionNew.triggered.connect(self.new_file)
    self.actionOpen.triggered.connect(self.open_file)
    self.actionPrint.triggered.connect(self.print_file)
    self.actionPrint_Preview.triggered.connect(self.preview_dialog)
    self.actionExport_PDF.triggered.connect(self.export_pdf)
    self.actionQiet.triggered.connect(self.quit)

    self.actionUndo.triggered.connect(self.textEdit.undo)
    self.actionRedo.triggered.connect(self.textEdit.redo)
    self.actionCut.triggered.connect(self.textEdit.cut)
    self.actionCopy.triggered.connect(self.textEdit.copy)
    self.actionPaste.triggered.connect(self.textEdit.paste)

    self.actionBold.triggered.connect(self.bold)
    self.actionItalic.triggered.connect(self.italic)
    self.actionUnder_Line.triggered.connect(self.under_line)

    self.actionLeft.triggered.connect(lambda : self.textEdit.setAlignment(Qt.AlignmentFlag.AlignLeft))
    self.actionCenter.triggered.connect(lambda : self.textEdit.setAlignment(Qt.AlignmentFlag.AlignCenter))
    self.actionRight.triggered.connect(lambda: self.textEdit.setAlignment(Qt.AlignmentFlag.AlignRight))
    self.actionJustify.triggered.connect(lambda: self.textEdit.setAlignment(Qt.AlignmentFlag.AlignJustify))

    self.actionColor.triggered.connect(self.set_color)
    self.actionFont.triggered.connect(self.set_font)
    self.actionAbout_App.triggered.connect(lambda : QMessageBox.about(self , "About App" , "This Is Simple NotePad"))

  def save_file(self):
    filename = QFileDialog.getSaveFileName(self , "Save File")
    
    if filename[0]:
      with open(filename[0], "w") as f:
        text = self.textEdit.toPlainText()

        f.write(text)

        QMessageBox.about(self , "Save File" , "File has been saved")

  def new_file(self):
    if not self.textEdit.document().isModified():
      return False
    
    ret = QMessageBox.warning(
      self,
      "Application",
      "The Document Has Been Modified \n Do You Want To Save Your Changes ?" ,
      QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard |QMessageBox.StandardButton.Cancel)

    if ret == QMessageBox.StandardButton.Save :
      self.save_file()
      self.textEdit.clear()
    elif ret == QMessageBox.StandardButton.Cancel :
      return False  
    else:
      self.textEdit.clear()    
  
  def open_file(self):
    filename = QFileDialog.getOpenFileName(self , "Open File" , "/home")

    if filename[0]:
      with open(filename[0] , "r") as r:
        self.textEdit.setText(r.read())

  def print_file(self):
    printer = QPrinter(QPrinter.PrinterMode.HighResolution)
    dialog = QPrintDialog(printer)

    if dialog.exec() == QPrintDialog.DialogCode.Accepted:
      self.textEdit.print(printer=printer)

  def preview_dialog(self):
    printer = QPrinter(QPrinter.PrinterMode.HighResolution)
    previewDialog = QPrintPreviewDialog(printer , self)

    previewDialog.paintRequested.connect(lambda: self.textEdit.print(printer))
    previewDialog.exec()
  
  def export_pdf(self):
    fn , _ = QFileDialog.getSaveFileName(self , "Export PDF" , "PDF_File")
    if fn != "":
      if QFileInfo(fn).suffix() == "": fn+=".pdf"
      printer = QPrinter(QPrinter.PrinterMode.HighResolution)
      printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
      printer.setOutputFileName(fn)
      self.textEdit.document().print(printer)
  
  def quit(self):
    self.close()

  def bold(self):
    font = QFont()
    font.setBold(True)
    self.textEdit.setFont(font)

  def italic(self):
    font = QFont()
    font.setItalic(True)
    self.textEdit.setFont(font)
  
  def under_line(self):
    font = QFont()
    font.setUnderline(True)
    self.textEdit.setFont(font)

  def set_color(self):
    color = QColorDialog.getColor()
    if color.isValid():
      self.textEdit.setTextColor(color)

  def set_font(self):
    font,ok = QFontDialog.getFont()
    if ok:
      self.textEdit.setFont(font)

app = QApplication([])
MainWindow = indexNoteOad()

sys.exit(app.exec())
