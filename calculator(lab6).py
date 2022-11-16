import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_second = QHBoxLayout()
        self.hbox_3 = QHBoxLayout()
        self.hbox_4 = QHBoxLayout()
        self.hbox_result = QHBoxLayout()
        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_3)
        self.vbox.addLayout(self.hbox_4)
        self.vbox.addLayout(self.hbox_result)
        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)
        self.b_1 = QPushButton("1", self)
        self.hbox_first.addWidget(self.b_1)
        self.b_2 = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_2)
        self.b_3 = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_3)
        self.b_plus = QPushButton("+", self)
        self.hbox_first.addWidget(self.b_plus)
        self.b_4 = QPushButton("4", self)
        self.hbox_second.addWidget(self.b_4)
        self.b_5 = QPushButton("5", self)
        self.hbox_second.addWidget(self.b_5)
        self.b_6 = QPushButton("6", self)
        self.hbox_second.addWidget(self.b_6)
        self.b_minus = QPushButton("-", self)
        self.hbox_second.addWidget(self.b_minus)
        self.b_7 = QPushButton("7", self)
        self.hbox_3.addWidget(self.b_7)
        self.b_8 = QPushButton("8", self)
        self.hbox_3.addWidget(self.b_8)
        self.b_9 = QPushButton("9", self)
        self.hbox_3.addWidget(self.b_9)
        self.b_ymn = QPushButton("*", self)
        self.hbox_3.addWidget(self.b_ymn)
        self.b_0 = QPushButton("0", self)
        self.hbox_4.addWidget(self.b_0)
        self.b_del = QPushButton("/", self)
        self.hbox_4.addWidget(self.b_del)
        self.b_t = QPushButton(".", self)
        self.hbox_4.addWidget(self.b_t)
        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)
        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_ymn.clicked.connect(lambda: self._operation("*"))
        self.b_del.clicked.connect(lambda: self._operation("/"))
        self.b_result.clicked.connect(self._result)
        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_0.clicked.connect(lambda: self._button("0"))
        self.b_t.clicked.connect(lambda: self._button("."))
    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)
    def _operation(self, op):
        try:
            self.num_1 = int(self.input.text())
        except:
            self.num_1 = float(self.input.text())
        self.op = op
        self.input.setText("")
    def _result(self):
        try:
            self.num_2 = int(self.input.text())
        except:
            self.num_2 = float(self.input.text())
        if self.op == "+":
            self.input.setText(str(self.num_1 + self.num_2))
        elif self.op == "-":
            self.input.setText(str(self.num_1 - self.num_2))
        elif self.op == "*":
            self.input.setText(str(self.num_1 * self.num_2))
        elif self.op == "/" and self.num_2 != 0:
            self.input.setText(str(self.num_1 / self.num_2))
        else:
            self.input.setText('На ноль делить нельзя.')
app = QApplication(sys.argv)
win = Calculator()
win.show()
sys.exit(app.exec_())