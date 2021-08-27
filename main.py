from PyQt5.QtWidgets import *
from PyQt5.QtCore import QStringListModel
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
model = QStringListModel(["a","b","c"])
view = QListView()
view.setModel(model)
view.show()
app.exec()
