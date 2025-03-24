import sys
import os

from PySide6.QtCore import QStandardPaths, QDir
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog
from mainwindow import Ui_MainWindow

class WatermarkApp(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		#TODO add a base image
		self.image = None
		self.font_size = 20

		self.LoadImage.clicked.connect(self.load_image)

	def load_image(self):
		options = QFileDialog.Options()
		pictures_dir = QStandardPaths.writableLocation(QStandardPaths.PicturesLocation)

		# If the pictures directory isn't found, fall back to the home directory
		if not pictures_dir:
			pictures_dir = os.path.expanduser("~")
		file_name, _ = QFileDialog.getOpenFileName(self,
												   "Open Image File",
												   pictures_dir,
												   "Images (*.png *.jpg *.jpeg *.bmp)", options=options)
		if file_name:
			self.image = file_name
			self.imageLabel.setText(f"Loaded image: {file_name}")

if __name__ == "__main__":
	app = QApplication([])
	window = WatermarkApp()
	window.show()
	sys.exit(app.exec())
