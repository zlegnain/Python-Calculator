import PyQt5.QtWidgets as qtw
from PyQt5.QtWidgets import QWidget


class MainWindow(qtw.QWidget):

    """"
    __init__ constructor that will initialize our mainWindow

    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Basic Calculator')
        self.setLayout(qtw.QVBoxLayout())
        self.init_ui()
        self.show()

    """
    init_ui method that will initialize our UI, creating the Gridlayout and
    adding all buttons.
    
    """
    def init_ui(self):

        # using a gridlayout
        container: QWidget = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        # result field
        self.result = qtw.QLineEdit()

        # button for result and clear
        self.result_btn = qtw.QPushButton("Enter")
        self.clear_btn = qtw.QPushButton("Clear")

        # buttons for numbers 0-9
        self.btn_0 = qtw.QPushButton('0')
        self.btn_1 = qtw.QPushButton('1')
        self.btn_2 = qtw.QPushButton('2')
        self.btn_3 = qtw.QPushButton('3')
        self.btn_4 = qtw.QPushButton('4')
        self.btn_5 = qtw.QPushButton('5')
        self.btn_6 = qtw.QPushButton('6')
        self.btn_7 = qtw.QPushButton('7')
        self.btn_8 = qtw.QPushButton('8')
        self.btn_9 = qtw.QPushButton('9')

        # buttons for operators: +. -, / , *
        self.plus_btn = qtw.QPushButton('+')
        self.minus_btn = qtw.QPushButton('-')
        self.div_btn = qtw.QPushButton('/')
        self.multi_btn = qtw.QPushButton('*')

        # we add the buttons to the layout
        container.layout().addWidget(self.result, 0,0,1,4)
        container.layout().addWidget(self.result_btn,1,0,1,2)
        container.layout().addWidget(self.clear_btn,1,2,1,2)
        container.layout().addWidget(self.btn_9, 2,0)
        container.layout().addWidget(self.btn_8,2,1)
        container.layout().addWidget(self.btn_7,2,2)
        container.layout().addWidget(self.plus_btn, 2,3)
        container.layout().addWidget(self.btn_6,3,0)
        container.layout().addWidget(self.btn_5,3,1)
        container.layout().addWidget(self.btn_4, 3,2)
        container.layout().addWidget(self.minus_btn, 3,3)
        container.layout().addWidget(self.btn_3,4,0)
        container.layout().addWidget(self.btn_2,4,1)
        container.layout().addWidget(self.btn_1,4,2)
        container.layout().addWidget(self.div_btn,4,3)
        container.layout().addWidget(self.btn_0,5,0,1,3)
        container.layout().addWidget(self.multi_btn,5,3)
        self.layout().addWidget(container)