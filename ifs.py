
from tkinter import messagebox
def winer(symboy_player,buttom1, buttom2, buttom3, buttom4, buttom5, buttom6, buttom7, buttom8, buttom9):
    if symboy_player == '0':
        cor = 'blue'
    if symboy_player == 'X':
        cor = 'red'
    if buttom1['text'] != '' and buttom1['text'] == buttom2['text'] and buttom1['text'] == buttom3['text']:
        buttom1['bg'] = cor
        buttom2['bg'] = cor
        buttom3['bg'] = cor


        answer = messagebox.askquestion(title='End', message='Do you wanna play again?')
        if answer == 'yes':
            return True
        else:
            return False


    if buttom1['text'] != '' and buttom1['text'] == buttom4['text'] and buttom1['text'] == buttom7['text']:
        buttom1['bg'] = cor
        buttom4['bg'] = cor
        buttom7['bg'] = cor
        answer = messagebox.askquestion(title='End', message='Do you wanna play again?')
        if answer == 'yes':
            return True
        else:
            return False

    if buttom1['text'] != '' and buttom1['text'] == buttom5['text'] and buttom1['text'] == buttom9['text']:
        buttom1['bg'] = cor
        buttom5['bg'] = cor
        buttom9['bg'] =cor
        answer = messagebox.askquestion(title='End', message='Do you wanna play again?')
        if answer == 'yes':
            return True
        else:
            return False
    if buttom2['text'] != '' and buttom2['text'] == buttom5['text'] and buttom2['text'] == buttom8['text']:
        buttom2['bg'] = cor
        buttom5['bg'] = cor
        buttom8['bg'] = cor
        answer = messagebox.askquestion(title='End', message='Do you wanna play again?')
        if answer == 'yes':
            return True
        else:
            return False

    if buttom3['text'] != '' and buttom3['text'] == buttom6['text'] and buttom3['text'] == buttom9['text']:
        buttom3['bg'] = cor
        buttom6['bg'] = cor
        buttom9['bg'] = cor
        answer = messagebox.askquestion(title='End', message='Do you wanna play again?')
        if answer == 'yes':
            return True
        else:
            return False

    if buttom3['text'] != '' and buttom3['text'] == buttom5['text'] and buttom3['text'] == buttom7['text']:
        buttom3['bg'] = cor
        buttom5['bg'] = cor
        buttom7['bg'] =cor
        answer = messagebox.askquestion(title='End', message='Do you wanna play again?')
        if answer == 'yes':
            return True
        else:
            return False

    if buttom4['text'] != '' and buttom4['text'] == buttom5['text'] and buttom4['text'] == buttom6['text']:
        buttom4['bg'] = cor
        buttom5['bg'] = cor
        buttom6['bg'] = cor
        answer = messagebox.askquestion(title='End', message='Do you wanna play again?')
        if answer == 'yes':
            return True
        else:
            return False

    if buttom7['text'] != '' and buttom7['text'] == buttom8['text'] and buttom7['text'] == buttom9['text']:
        buttom7['bg'] = cor
        buttom8['bg'] = cor
        buttom9['bg'] = cor
        answer = messagebox.askquestion(title='End', message='Do you wanna play again?')
        if answer == 'yes':
            return True
        else:
            return False


