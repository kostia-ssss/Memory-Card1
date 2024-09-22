from PyQt5.QtWidgets import QWidget , QApplication
from random import shuffle

app = QApplication([])
from layout_quizz import *
from data import *

i = 0

window = QWidget()
window.resize(600 , 500)
window.setWindowTitle("Memory Card")
window.setLayout(main_line_quizz)

menu_window = QWidget()
menu_window.resize(600 , 500)
menu_window.setWindowTitle("Memory Card")
menu_window.setLayout(main_line_menu)
menu_window.show()

shuffle(questions)
questions[i].show_question(quest_lb , btn1 , btn2 , btn3 , btn4)


def click():
    global i
    if btn.text() == "Відповісти":
        box.hide()
        box2.show()
        ans_text2.setText(btn1.text())
        btn.setText("Наступне питання")
    else:
        box2.hide()
        box.show()
        btn.setText("Відповісти")
        i += 1
        questions[i].show_question(quest_lb , btn1 , btn2 , btn3 , btn4)

def click_menu():
    menu_window.show()
    window.hide()

def click_menu_exit():
    window.show()
    menu_window.hide()

def exit():
    app.exit()    

def true():
    ans_text.setText("Правильно")
    
def false():
    ans_text.setText("Неправильно")

btn.clicked.connect(click)
btn1.clicked.connect(true)
btn2.clicked.connect(false)
btn3.clicked.connect(false)
btn4.clicked.connect(false)
btn_menu.clicked.connect(click_menu)
btn_menu_quit.clicked.connect(click_menu_exit)
btn_app_quit.clicked.connect(exit)

app.exec()