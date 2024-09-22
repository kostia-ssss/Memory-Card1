from PyQt5.QtWidgets import (QPushButton , QRadioButton , QLabel , QSpinBox , QGroupBox ,
                             QButtonGroup , QHBoxLayout , QVBoxLayout)
from PyQt5.QtCore import Qt

btn_menu = QPushButton("Меню")
btn_rest = QPushButton("Відпочити")

spin = QSpinBox()
spin.setValue(30)

box = QGroupBox()
box2 = QGroupBox()
Group = QButtonGroup()

quest_lb = QLabel("____")

btn1 = QRadioButton("___")
btn2 = QRadioButton("___")
btn3 = QRadioButton("___")
btn4 = QRadioButton("___")

btn = QPushButton("Відповісти")
btn_menu_quit = QPushButton("Почати тестування")
btn_menu1 = QPushButton("Почати заучування")
btn_app_quit = QPushButton("Вийти")

ans_text = QLabel("Правильно")
ans_text2 = QLabel("apple")

Group.addButton(btn1)
Group.addButton(btn2)
Group.addButton(btn3)
Group.addButton(btn4)


main_line_quizz = QVBoxLayout()
main_line_menu = QVBoxLayout()
line_box = QHBoxLayout()
line_box2 = QHBoxLayout()
line1_quizz = QHBoxLayout()
line2_quizz = QVBoxLayout()
line3_quizz = QVBoxLayout()

line1_quizz.addWidget(btn_menu)
line1_quizz.addStretch(1)
line1_quizz.addWidget(btn_rest)
line1_quizz.addWidget(spin)
line1_quizz.addWidget(QLabel("хвилин"))

line2_quizz.addWidget(btn1)
line2_quizz.addWidget(btn2)
line3_quizz.addWidget(btn3)
line3_quizz.addWidget(btn4)

main_line_quizz.addLayout(line1_quizz)
main_line_quizz.addWidget(quest_lb)
main_line_quizz.addWidget(box, stretch=5)
line_box.addLayout(line2_quizz)
line_box.addLayout(line3_quizz)

box.setLayout(line_box)
box2.setLayout(line_box2)

line_box2.addWidget(ans_text , alignment = Qt.AlignTop)
line_box2.addWidget(ans_text2)

main_line_quizz.addWidget(box2, stretch=5)

box2.hide()

main_line_quizz.addWidget(btn , alignment = Qt.AlignCenter)
main_line_menu.addWidget(btn_menu_quit , alignment = Qt.AlignCenter)
main_line_menu.addWidget(btn_menu1 , alignment = Qt.AlignCenter)
main_line_menu.addWidget(btn_app_quit , alignment = Qt.AlignCenter)