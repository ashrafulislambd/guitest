"""Main module."""

from PyQt5.QtWidgets import QMessageBox, QApplication, QInputDialog, QWidget

def print(msgText):
	app = QApplication([])
	msg = QMessageBox()
	msg.setText(msgText)
	msg.exec()
	del app

def input(promptText):
	app = QApplication([])
	inp, ok = QInputDialog.getText(None, "GUIPRINT", promptText)
	if ok:
		return inp
	return None

if __name__ == "__main__":
	# Some debugging codes :)
	"""
	print("Hello")
	msg = input("What's your name? :")
	print(msg)
	"""