# Evaluate mathematical expressions funcition: https://github.com/mariocesar
import ast
import re


def expr(code, context=None):
    """Eval a math expression and return the result"""
    if not context:
        context = {}
    code = code.format(**context)

    # An especial case for my own when using percents values.
    # TODO: Fail if you are not comparing same type value like "50 > 20%" haves to fail
    code = re.sub('%', '', code)

    expr = ast.parse(code, mode='eval')
    code_object = compile(expr, '<string>', 'eval')

    return eval(code_object)


#########################################################################################

# game: http://www.clickjogos.com.br/jogos/countdown-calculator/

from PIL import ImageGrab, Image
import pyautogui
import pytesseract
from time import sleep


replace_list = ['o', 'O']

# click the start button
def start_game():
    pyautogui.click(x=950, y=620)


# take a screenshot of the question and save a png file
def snapshot():
    snap = ImageGrab.grab(bbox=(810, 568, 1090, 620))
    snap.save('question.png')


def read_question():
    # read the png file and convert it to a string
    question = pytesseract.image_to_string(Image.open('question.png'))
    # if there is 'o' or 'O' in the string, replace for '0'
    # tesseract thinks '0' is the letter 'O'
    for char in question:
        if char in replace_list:
            question = question.replace(char, '0')

    # expr function needs a condition so we need to add a '='
    # example: '1+1=2' > '1+1==2'
    equal = question.index('=')
    question = question[:equal] + '=' + question[equal:]
    print(question)
    return question


# if the condition is true, click the green button, otherwise red button
def answer_question(question):
    if expr(question) == True:
        pyautogui.click(x=1030, y=745)
    else:
        pyautogui.click(x=860, y=740)


start_game()
# the game has a 3 secs countdown before starting the questions
sleep(4)

while True:
    snapshot()
    answer_question(read_question())
    sleep(1)
