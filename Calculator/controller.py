
import PyQt5.QtWidgets as qtw
from PyQt5.QtWidgets import QWidget
from frontend import MainWindow



class Controller:

    def __init__(self):
        self.fe = MainWindow()
        self.field = []


        # handle events when clear and enter btns are clicked
        self.fe.clear_btn.clicked.connect(lambda : self.clear())
        self.fe.result_btn.clicked.connect(lambda : self.eval_exp())

        # handle events when buttons 0-9 are clicked
        self.fe.btn_0.clicked.connect(lambda : self.press_num('0'))
        self.fe.btn_1.clicked.connect(lambda: self.press_num('1'))
        self.fe.btn_2.clicked.connect(lambda: self.press_num('2'))
        self.fe.btn_3.clicked.connect(lambda: self.press_num('3'))
        self.fe.btn_4.clicked.connect(lambda: self.press_num('4'))
        self.fe.btn_5.clicked.connect(lambda: self.press_num('5'))
        self.fe.btn_6.clicked.connect(lambda: self.press_num('6'))
        self.fe.btn_7.clicked.connect(lambda: self.press_num('7'))
        self.fe.btn_8.clicked.connect(lambda: self.press_num('8'))
        self.fe.btn_9.clicked.connect(lambda: self.press_num('9'))

        # handle events when operators are clicked
        self.fe.plus_btn.clicked.connect(lambda : self.press_num('+'))
        self.fe.minus_btn.clicked.connect(lambda : self.press_num('-'))
        self.fe.multi_btn.clicked.connect(lambda : self.press_num('*'))
        self.fe.div_btn.clicked.connect(lambda : self.press_num('/'))




    """
    pres_num method that takes a key number value, and displays it in the result field
    """
    def press_num(self, num):
        self.field.append(num)
        temp_str = ''.join(self.field)
        self.fe.result.setText(temp_str)



    """
    eval_exp method that will evaluate the string expression and display the answer to the result field
    """
    def eval_exp(self):
        temp_str = ''.join(self.field)

        # check if expression is valid
        try:
            eval(temp_str)
            r = eval(temp_str)
            self.fe.result.setText(str(r))
            self.field = [str(r)]
        except SyntaxError:
            self.fe.result.setText("Incorrect Input")


    """
    clear method that will clear the result field
    """
    def clear(self):
        self.field = []
        self.fe.result.setText('')
        pass





if __name__ == '__main__':
    app = qtw.QApplication([])
    calculator = Controller()
    app.exec_()








