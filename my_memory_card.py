#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox, QGroupBox, QButtonGroup
from random import randint, shuffle


class Question():
    def __init__(self, questions, correct, wrong1, wrong2, wrong3):
        self.questions = questions
        self.correct = correct
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = list()
question_list.append(Question('В каком году началась Отечественна война?', '1812', '1892', '1752','1900'))
question_list.append(Question('Какое животное самое быстрое?', 'гепард', 'антилопа', 'лев','тигр'))
question_list.append(Question('На каком языке говорят в мексике?', 'испанский', 'английский', 'итальянский','русский'))

def Button_ask():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

def ask(question):
    shuffle(butt)
    butt[0].setText(question.correct)
    butt[1].setText(question.wrong1)
    butt[2].setText(question.wrong2)
    butt[3].setText(question.wrong3)
    question_main.setText(question.questions)
    show_question()
    
    
def next_question():
    rand = randint(0,len(question_list) - 1)
    ask(question_list[rand])
    if len(question_list) > 0:
        question_list.pop(rand)
    else:
        app.exit()
        


def show_question():
    RadioGroupBox_2.hide()
    RadioGroupBox.show()
    button.setText('Ответить')

    RadioGroup.setExclusive(False)
    butt[0].setChecked(False)
    butt[1].setChecked(False)
    butt[2].setChecked(False)
    butt[3].setChecked(False)
    RadioGroup.setExclusive(True)
    


def check_answer():
    if butt[0].isChecked():
        show_correct('Верно')
        statistic(True)
    else:
        if butt[1].isChecked() or butt[2].isChecked() or butt[3].isChecked():
            show_correct('Неверно')
            statistic(False)

def show_correct(true_or_false):
    RadioGroupBox_2.show()
    RadioGroupBox.hide()
    button.setText('Следующий вопрос')
    true.setText(butt[0].text())
    if true_or_false == 'Верно':
        true_false.setText('Верно')
    else:
        true_false.setText('Неверно')

def statistic(result):
    global answer_full
    answer_full = answer_full + 1
    if result:
        global correct_true
        correct_true = correct_true + 1
    print("Всего вопросов:", answer_full)
    print("Правильных ответов:", correct_true)
    print("Рейтинг:", round((correct_true / answer_full) * 100 ,2))

app = QApplication([])
#создание виджетов главного окна
correct_true = 0
answer_full = 0

main_win = QWidget()
main_win.setWindowTitle('Memory Card')
question_main = QLabel('Какой национальности не существует?')
question_2 = QLabel('Самый сложный вопрос в мире!')
true_false = QLabel('Правильно/Неправильно')
true = QLabel('Тут будет правильный ответ')
RadioGroupBox = QGroupBox('Варианты ответов')
RadioGroupBox_2 = QGroupBox('Результаты теста')
RadioGroupBox_2.hide()
answer1 = QRadioButton('Энцы')
answer2 = QRadioButton('Чулымцы')
answer3 = QRadioButton('Смурфы')
answer4 = QRadioButton('Алеуты')

butt = [answer1, answer2, answer3, answer4]
RadioGroup = QButtonGroup()
RadioGroup.addButton(butt[0])
RadioGroup.addButton(butt[1])
RadioGroup.addButton(butt[2])
RadioGroup.addButton(butt[3])

button = QPushButton('Ответить')
button.clicked.connect(Button_ask)

#расположение виджетов по лэйаутам
main_layout = QVBoxLayout()
layout1 = QHBoxLayout()
layout2 = QHBoxLayout()
layout3 = QHBoxLayout()

layout1.addWidget(question_main)
layout2.addWidget(RadioGroupBox)
layout2.addWidget(RadioGroupBox_2)
layout3.addWidget(button)

layout_r_main = QVBoxLayout()
layout_r1 = QHBoxLayout()
layout_r2 = QHBoxLayout()

layout_r_main_2 = QVBoxLayout()
layout_r3 = QHBoxLayout()
layout_r4 = QHBoxLayout()

#1
layout_r1.addWidget(answer1)
layout_r1.addWidget(answer2)
layout_r2.addWidget(answer3)
layout_r2.addWidget(answer4)

layout_r3.addWidget(true_false)
layout_r4.addWidget(true)


layout_r_main.addLayout(layout_r1)
layout_r_main.addLayout(layout_r2)

layout_r_main_2.addLayout(layout_r3)
layout_r_main_2.addLayout(layout_r4)

main_layout.addLayout(layout1)
main_layout.addLayout(layout2)
main_layout.addLayout(layout3)

RadioGroupBox.setLayout(layout_r_main)
RadioGroupBox_2.setLayout(layout_r_main_2)
main_win.setLayout(main_layout)

#обработка нажатий на переключатели
#отображение окна приложения 
main_win.show()
app.exec_()