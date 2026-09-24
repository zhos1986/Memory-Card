from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QGroupBox, QRadioButton, QHBoxLayout, QButtonGroup
from random import shuffle, randint


app = QApplication([])
main_win = QWidget()
main_win.cur_question = -1
main_win.right = 0
main_win.number_questions = 0
main_win.resize(800, 400)
question = QLabel('Какой национальности не существует?')
main_win.setWindowTitle('Memory Card')
RadioGroupBox = QGroupBox('Варианты ответов...')
results = QGroupBox('Результат теста')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
check = QPushButton('Ответить')
yes_no = QLabel('Правильно/Неправильно')
yes = QLabel('Правильный ответ')

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


vertical_ans1 = QVBoxLayout()

vertical_ans1.addWidget(yes_no, alignment = Qt.AlignLeft)
vertical_ans1.addWidget(yes, alignment = Qt.AlignCenter)

class Question():
    def __init__(self, question_1, right_answer, wrong_1, wrong_2, wrong_3):
        self.question_1 = question_1
        self.right_answer = right_answer
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3
question_list = []
question_list.append(Question(
                            'В каком году родился Пушкин?',
                            '1799г',
                            '1801г',
                            '1204г',
                            '1998г'
))
question_list.append(Question(
                            'Сколько произведений написал пушкин?',
                            '430',
                            '54',
                            '1762',
                            '130'
))
question_list.append(Question(
                            'В каком году произошло Крещение Руси?',
                            '988г',
                            '1203г',
                            '591г',
                            '109г'
))
question_list.append(Question(
                            'Какая глубина самого глубокого озера?',
                            '1642 метра',
                            '542 метра',
                            '152 метра',
                            '4756 метров'
))
question_list.append(Question(
                            'Чему равно ускорение свободного падения у поверхности Земли?',
                            '9,8м/c сверху2',
                            '9,8м/с',
                            '35 м/с',
                            '2,3 м/с сверху2'
))
question_list.append(Question(
                            'Какой учёный математик придумал в геометрии <штаны>',
                            'Пефагор',
                            'Аристотель',
                            'минделеев',
                            'Цезарь'
))
question_list.append(Question(
                            'Название какого садового цветка произошло от лат. <звезда>?',
                            'астра',
                            'Гладиолус',
                            'Ромашка',
                            'Флокс'
))
question_list.append(Question(
                            'Какой царь отменил крепостное право?',
                            'Александр 2',
                            'Пётр 1',
                            'Николай 1',
                            'Иван Грозный 4'
))

def show_result():
    RadioGroupBox.hide()
    results.show()
    check.setText('Следующий вопрос')
def show_question():
    results.hide()
    RadioGroupBox.show()
    check.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
def start_test():
    if check.text() == 'Ответить':
        show_result()
    else:
        show_question()
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong_1)
    answers[2].setText(q.wrong_2)
    answers[3].setText(q.wrong_3)
    yes.setText(q.right_answer)
    question.setText(q.question_1)
    show_question()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.right += 1
    else:
        show_correct('Неправильно...')
    rating = main_win.right / main_win.number_questions * 100
    print('Всего вопросов:', main_win.number_questions)
    print('Правильных ответов:', main_win.right)
    print('Рейтинг:', rating) 

def show_correct(yes_or_no):
    yes_no.setText(yes_or_no)
    show_result()
def next_question():
    #main_win.cur_question += 1
    cur_question = randint(0,len(question_list) - 1)
    number = question_list[cur_question]
    main_win.number_questions += 1
    ask(number)
def click_OK():
    if check.text() == 'Следующий вопрос':
        next_question()
    else:
        check_answer()




layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
horizontal_ans1 = QHBoxLayout()
horizontal_ans2 = QHBoxLayout()
horizontal_ans3 = QHBoxLayout()
vertical_ans4 = QVBoxLayout()
vertical_ans5 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
layout_ans2.setSpacing(50)
layout_ans3.setSpacing(50)
vertical_ans1.setSpacing(50)

RadioGroupBox.setLayout(layout_ans1)
results.hide()
results.setLayout(vertical_ans1)

horizontal_ans1.addWidget(question, alignment = Qt.AlignCenter)
horizontal_ans2.addWidget(RadioGroupBox, alignment = Qt.AlignCenter)
horizontal_ans2.addWidget(results, alignment = Qt.AlignCenter)
horizontal_ans3.addWidget(check, alignment = Qt.AlignCenter)
vertical_ans4.addLayout(horizontal_ans1)
vertical_ans4.addLayout(horizontal_ans2)
vertical_ans4.addLayout(horizontal_ans3)
main_win.setLayout(vertical_ans4)


next_question()
check.clicked.connect(click_OK)

main_win.show()
app.exec_()
