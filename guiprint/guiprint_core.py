"""Main module."""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

def print(msgText):
	app = QApplication([])
	msg = QMessageBox()
	msg.setText(msgText)
	msg.exec()
	del app

def input(promptText, mode=None, options=["options", "parameter", "missing"]):
	if mode=="yesno":
		app = QApplication([])
		msg = QMessageBox()
		msg.setText(promptText)
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		val = msg.exec()
		del app
		if val == QMessageBox.Yes:
			return "yes"
		elif val == QMessageBox.No:
			return "no"
		else:
			return None
	elif mode == "multiple":
		app = QApplication([])
		d = QDialog()
		toplayout = QVBoxLayout()
		topwidget = QWidget()
		toplayout.addWidget(topwidget)
		layout = QHBoxLayout()
		topwidget.setLayout(layout)
		opt = QComboBox()
		label = QLabel()
		label.setText(promptText)
		layout.addWidget(label)
		layout.addWidget(opt)
		for option in options:
			opt.addItem(option)

		ok_button = QPushButton("OK")
		ok_button.clicked.connect(lambda:d.accept())
		toplayout.addWidget(ok_button)

		d.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.CustomizeWindowHint)
		d.setLayout(toplayout)
		d.setWindowModality(Qt.ApplicationModal)
		d.exec_()

		return opt.currentText()

	app = QApplication([])
	inp, ok = QInputDialog.getText(None, "GUIPRINT", promptText)
	if ok:
		return inp
	return None

if __name__ == "__main__":
	# Some debugging codes :)
	"""
	print("Hello")
	msg = input("What's your name? :", mode="multiple")
	print(msg)
	"""