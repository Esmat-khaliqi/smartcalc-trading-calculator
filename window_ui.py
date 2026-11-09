import sys
import resources_rc
from PySide6.QtWidgets import QApplication , QMainWindow
from calculator_ui import Ui_Calculator
from PySide6.QtGui import QIcon ,QRegularExpressionValidator
from PySide6.QtCore import QEvent ,Qt, QRegularExpression
from app import App
from trade_section import Trade


class Main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Calculator()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/icons/icons/icon_128.ico"))
        self.setWindowTitle('Smart Calcu')
        self.tradeing  =  Trade(self.ui)
        self.method_class = App()
        self.num_list = []
        self.entry_num = self.ui.user_value
        self.entry_num.installEventFilter(self)

        validator = QRegularExpressionValidator(
            QRegularExpression(r"-?[0-9]*\.?[0-9]*")
        )
        validator_trade = QRegularExpressionValidator(
            QRegularExpression(r"[0-9]*\.?[0-9]*")
        )
        self.ui.user_value.setValidator(validator)
        self.result_bar  = self.ui.result_bar

        self.trade_inputs = [
             self.ui.acc_b,
             self.ui.entry_p,
             self.ui.tp,
             self.ui.risk_percent,
             self.ui.sl,
             self.ui.risk_reward_r,
        ]

        for inp in self.trade_inputs:
            inp.setValidator(validator_trade)

        self.ui.stackedWidget_2.setCurrentWidget(self.ui.calculator_mashien_section)
        self.ui.trading_pages.setCurrentWidget(self.ui.empty_frame)


        self.calculate_btn = self.ui.calculator_widget
        self.calculate_btn.mousePressEvent = self.calculate_btn_action
        self.calculate_btn_icon = self.ui.calculat_arrow

        self.trade_btn = self.ui.trading_widget
        self.trade_btn.mousePressEvent = self.trade_btn_action
        self.trade_btn_icon = self.ui.trade_arrow

        self.setting_btn = self.ui.setting_widget 
        self.setting_btn.mousePressEvent = self.setting_btn_action

        self.trade_btn_style = self.trade_btn.styleSheet()
        self.trade_btn_style = self.trade_btn_style.replace("background: rgba(59, 130, 246, 0.15);","background: transparent;")
        self.trade_btn.setStyleSheet(self.trade_btn_style)
        self.trade_btn_icon.hide()

        self.setting_btn_style = self.setting_btn.styleSheet()
        self.setting_btn_style = self.setting_btn_style.replace("background: rgba(59, 130, 246, 0.15);","background: transparent;")
        self.setting_btn.setStyleSheet(self.setting_btn_style)

        self.path_name = self.ui.path_name
        self.btn_equal = self.ui.btn_equal
        self.clear_btn = self.ui.clear_btn
        self.backs_btn = self.ui.backs_btn
   

        buttons_opr = [
             self.ui.btn_plus,
             self.ui.btn_minus,
             self.ui.btn_multiply,
             self.ui.btn_divide,
             self.ui.btn_percent
        ]

        buttons = [
            self.ui.num_0,
            self.ui.num_1,
            self.ui.num_2,
            self.ui.num_3,
            self.ui.num_4,
            self.ui.num_5,
            self.ui.num_6,
            self.ui.num_7,
            self.ui.num_8,
            self.ui.num_9,
            self.ui.btn_decimal
        ]

        self.btn_minus_plus= self.ui.btn_minus_plus
        # take action for btn calculator

        for btn_opr in buttons_opr:
            btn_opr.clicked.connect(self.operator_clicked)

        self.btn_equal.clicked.connect(self.equal_action)
        self.clear_btn.clicked.connect(self.clear_all)
        self.backs_btn.clicked.connect(self.backspace_clear)
        self.btn_minus_plus.clicked.connect(self.button_decimal)
        for btn in buttons:
            btn.clicked.connect(self.button_value)

    def eventFilter(self, watched, event):
        if watched == self.entry_num and event.type() == QEvent.Type.KeyPress:
            if event.key() == Qt.Key.Key_Plus:
                self.choose_opr(event.text())
                return True
            elif event.key() == Qt.Key.Key_Minus:
                if self.entry_num.text().strip():
                    self.choose_opr(event.text())
                    return True
            elif event.key() == Qt.Key.Key_Asterisk:
                self.choose_opr(event.text())
                return True
            elif event.key() == Qt.Key.Key_Slash:
                self.choose_opr(event.text())
                return True
            elif event.key() == Qt.Key.Key_Backspace:
                self.backspace_clear()
                return True
            elif event.key() in(Qt.Key.Key_Equal,Qt.Key.Key_Enter,Qt.Key.Key_Return):
                self.equal_action()
                return True
            elif event.key() == Qt.Key.Key_Escape:
                self.clear_all()
                return True
            if (event.key() == Qt.Key.Key_Equal and event.modifiers() & Qt.KeyboardModifier.ShiftModifier):
                self.equal_action()
                return True
        return super().eventFilter(watched, event)

    def change_bg_icon(self,url_path):
        if url_path == "Setting":
            cal =self.calculate_btn.styleSheet()
            cal =cal.replace("background: rgba(59, 130, 246, 0.15);","background: transparent;")
            self.calculate_btn.setStyleSheet(cal)
            self.calculate_btn_icon.hide()

            trade =self.trade_btn.styleSheet()
            trade =trade.replace("background: rgba(59, 130, 246, 0.15);","background: transparent;")
            self.trade_btn.setStyleSheet(trade)
            self.trade_btn_icon.hide()

            setting =self.setting_btn.styleSheet()
            setting =setting.replace("background: transparent;","background: rgba(59, 130, 246, 0.15);")
            self.setting_btn.setStyleSheet(setting)
            self.path_name.setText(url_path)
            return
        elif url_path == "Calculator":
            cal =self.calculate_btn.styleSheet()
            cal =cal.replace("background: transparent;","background: rgba(59, 130, 246, 0.15);")
            self.calculate_btn.setStyleSheet(cal)
            self.calculate_btn_icon.show()
            self.path_name.setText(url_path)

            trade =self.trade_btn.styleSheet()
            trade =trade.replace("background: rgba(59, 130, 246, 0.15);","background: transparent;")
            self.trade_btn.setStyleSheet(trade)
            self.trade_btn_icon.hide()

            setting =self.setting_btn.styleSheet()
            setting =setting.replace("background: rgba(59, 130, 246, 0.15);","background: transparent;")
            self.setting_btn.setStyleSheet(setting)
            return
        elif url_path == "Trading":
            cal =self.calculate_btn.styleSheet()
            cal =cal.replace("background: rgba(59, 130, 246, 0.15);","background: transparent;")
            self.calculate_btn.setStyleSheet(cal)
            self.calculate_btn_icon.hide()

            trade =self.trade_btn.styleSheet()
            trade =trade.replace("background: transparent;","background: rgba(59, 130, 246, 0.15);")
            self.trade_btn.setStyleSheet(trade)
            self.trade_btn_icon.show()
            self.path_name.setText(url_path)

            setting =self.setting_btn.styleSheet()
            setting =setting.replace("background: rgba(59, 130, 246, 0.15);","background: transparent;")
            self.setting_btn.setStyleSheet(setting)
            return
             
    def calculate_btn_action(self,event):
        self.change_bg_icon('Calculator')
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.calculator_mashien_section)

    def trade_btn_action(self,event):
        self.change_bg_icon('Trading')
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.trading_section)

    def setting_btn_action(self,event):
        self.change_bg_icon('Setting')
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.setting_page)

    def choose_opr(self,value):
        if not self.entry_num.text().strip():
                    return
        if len(self.num_list) == 2:
            self.equal_action()
        if value == "x":
            value = '*'
        if value == "÷":
            value = '/'
        self.num_list.append(self.entry_num.text())
        self.num_list.append(f'{value}')
        self.result_bar.setText(f"{self.num_list[0]} {value} ")
        self.entry_num.clear()
        self.entry_num.setFocus()


    def operator_clicked(self):
        btn = self.sender()
        if btn is None:
            return

        self.choose_opr(btn.text())

    def button_value(self):
        btn = self.sender()
        btn_value = btn.text()

        self.entry_num.insert(btn_value)
        self.entry_num.setFocus()

    def button_decimal(self):
        entry_value = self.entry_num.text()

        if entry_value.startswith('-'):
            self.entry_num.setText(entry_value[1:])
        else:
            self.entry_num.setText('-' + entry_value )
        self.entry_num.setFocus()

    def equal_action(self):
        try:
                if not self.entry_num.text().strip() and len(self.num_list) == 2:
                    result = float(self.num_list[0])
                    self.entry_num.setText(f"{result:g}")
                    self.result_bar.clear()
                    self.num_list.clear()
                    return
                if not self.entry_num.text().strip():
                    return
                self.num_list.append(self.entry_num.text())
                self.result_bar.setText(f"{self.num_list[0]} {self.num_list[1]} {self.num_list[2]} =")
                if self.num_list[1] == '+':
                    result = self.method_class.plus(float(self.num_list[0]),float(self.num_list[2]))
                elif self.num_list[1] == '-':
                    result = self.method_class.minus(float(self.num_list[0]),float(self.num_list[2]))
                elif self.num_list[1] == '*':
                    result = self.method_class.multiplication(float(self.num_list[0]),float(self.num_list[2]))
                elif self.num_list[1] == '/':
                    result = self.method_class.divide(float(self.num_list[0]),float(self.num_list[2]))
                elif self.num_list[1] == "%":
                    result = self.method_class.percent(float(self.num_list[0]),float(self.num_list[2]))
                else:
                    return
                # self.entry_num.setText(str(result))
                self.entry_num.setText(f"{result:g}")
            
        except ZeroDivisionError:
                self.result_bar.setText("Error: Division by zero")
        except (ValueError , IndexError):
                self.result_bar.setText("Invalid Input")
        finally:
                self.num_list.clear()
                self.entry_num.setFocus()

 

    def backspace_clear(self):
        current_text = self.entry_num.text()
        if current_text:
            self.entry_num.setText(current_text[:-1])
        self.entry_num.setFocus()

    def clear_all(self):
        self.result_bar.clear()
        self.entry_num.clear()
        self.num_list.clear()
        self.entry_num.setFocus()



app = QApplication(sys.argv)

app_icon = QIcon(":/icons/icons/icon_128.ico")
app.setWindowIcon(app_icon)

window = Main_window()
window.setWindowIcon(app_icon)

window.show()

sys.exit(app.exec())
