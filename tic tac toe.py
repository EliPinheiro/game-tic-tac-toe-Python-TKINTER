from tkinter import *
import random
from time import sleep
from ifs import winer


HEIGHT = 7
WIDTH = 14
pc_wins = player_wins = 0
cont_color = 0
def finalizar():
    
    global name1, symboy_player
    name1 =  name.get()
    choicetela.destroy()
    symboy_player = X.get()
def check_button():
    global name, choicetela,X
    choicetela = Tk()
    choicetela.title('Login')
    choicetela.geometry('370x400')
    x = PhotoImage(file='x.png')
    o = PhotoImage(file='0.png')

    escolha_jogador = Label(choicetela,font=('Arial', 10),
                            text='Digite seu nome:',
                           )

    escolha_jogador.place(x=140,y=15)
    name = Entry(choicetela,font=('Arial', 20),width=20)
    name.place(x=40,y=40)


    pronto = Button(choicetela,text='Pronto',width=10,height=2,command=finalizar)
    pronto.place(x=155,y=330)

    lista_choice = [x,o]
    X = IntVar()

    for index in range(len(lista_choice)):
        radiobuttom = Radiobutton(choicetela,
                                  variable=X,
                                  value=index,
                                  image=lista_choice[index])
        if index == 0:
            radiobuttom.place(x=120,y=100)
        elif index == 1:
            radiobuttom.place(x=120,y=200)



    choicetela.mainloop()


check_button()

class Marque:
    def marque1(self):

        if len(new_lista) % 2 == 0:
            buttom1.config(text=symboy_pc, state=DISABLED)
        elif len(new_lista) % 2 == 1:
            buttom1.config(text=symboy_player,state=DISABLED)

    def marque2(self):

        if len(new_lista) % 2 == 0:
            buttom2.config(text=symboy_pc, state=DISABLED)
        else:
            buttom2.config(text=symboy_player, state=DISABLED)
    def marque3(self):

        if len(new_lista) % 2 == 0:
            buttom3.config(text=symboy_pc, state=DISABLED)
        else:
            buttom3.config(text=symboy_player, state=DISABLED)
    def marque4(self):

        if len(new_lista) % 2 == 0:
            buttom4.config(text=symboy_pc, state=DISABLED)
        else:
            buttom4.config(text=symboy_player, state=DISABLED)
    def marque5(self):

        if len(new_lista) % 2 == 0:
            buttom5.config(text=symboy_pc, state=DISABLED)
        else:
            buttom5.config(text=symboy_player, state=DISABLED)
    def marque6(self):

        if len(new_lista) % 2 == 0:
            buttom6.config(text=symboy_pc, state=DISABLED)
        else:
            buttom6.config(text=symboy_player, state=DISABLED)
    def marque7(self):

        if len(new_lista) % 2 == 0:
            buttom7.config(text=symboy_pc, state=DISABLED)
        else:
            buttom7.config(text=symboy_player, state=DISABLED)
    def marque8(self):

        if len(new_lista) % 2 == 0:
            buttom8.config(text=symboy_pc, state=DISABLED)
        else:
            buttom8.config(text=symboy_player, state=DISABLED)
    def marque9(self):

        if len(new_lista) % 2 == 0:
            buttom9.config(text=symboy_pc, state=DISABLED)
        else:
            buttom9.config(text=symboy_player, state=DISABLED)


marque = Marque()
window = Tk()

if symboy_player == 0:
    symboy_player = 'X'
    symboy_pc = '0'
else:
    symboy_player = '0'
    symboy_pc = 'X'


window.title('Tic tac')
icon = PhotoImage(file='icon tic tac.png')
window.iconphoto(True, icon)
canvas = Canvas(window)

placar1 = StringVar()
placar2 = StringVar()
placar1.set(f'  {name1}  \n\n  {player_wins}')
placar2.set(f'  IA  \n\n  {pc_wins}')


placar = Label(window,text='Placar',font=('Arial',WIDTH),height=5)
placar.grid(column=1,row=0)

placar_jogador = Label(window,textvariable=placar1,font=('Arial',WIDTH),height=5).grid(column=0,row=0)

placar_pc = Label(window,textvariable=placar2,font=('Arial',WIDTH),height=5).grid(column=2,row=0)

buttom1 = Button( font='InformalRoman',bg='light gray', width=WIDTH, height=HEIGHT,command=marque.marque1)
buttom1.grid(column=0, row=1)

buttom2 = Button(font='InformalRoman',bg='light gray', width=WIDTH, height=HEIGHT,command=marque.marque2)
buttom2.grid(column=1, row=1)

buttom3 = Button(font='InformalRoman',bg='light gray', width=WIDTH, height=HEIGHT,command=marque.marque3)
buttom3.grid(column=2, row=1)

buttom4 = Button(font='InformalRoman',bg='light gray', width=WIDTH, height=HEIGHT,command=marque.marque4)
buttom4.grid(column=0, row=2)

buttom5 = Button(font='InformalRoman',bg='light gray', width=WIDTH, height=HEIGHT,command=marque.marque5)
buttom5.grid(column=1, row=2)

buttom6 = Button(font='InformalRoman',bg='light gray', width=WIDTH, height=HEIGHT,command=marque.marque6)
buttom6.grid(column=2, row=2)

buttom7 = Button(font='InformalRoman',bg='light gray', width=WIDTH, height=HEIGHT,command=marque.marque7)
buttom7.grid(column=0, row=3)

buttom8 = Button(font='InformalRoman',bg='light gray', width=WIDTH, height=HEIGHT,command=marque.marque8)
buttom8.grid(column=1, row=3)

buttom9 = Button(font='InformalRoman',bg='light gray', width=WIDTH, height=HEIGHT,command=marque.marque9)
buttom9.grid(column=2, row=3)
lista_butom = [buttom1, buttom2, buttom3, buttom4, buttom5, buttom6, buttom7, buttom8, buttom9]

new_lista = [button for button in lista_butom if button['state'] == 'normal']
play_again = new_lista

function_list = [marque.marque1, marque.marque2, marque.marque3,marque.marque4,marque.marque5,marque.marque6,
                  marque.marque7,marque.marque8,marque.marque9]
v = 0

while len(new_lista) > 0:
    sleep(2)
    window.update()
    print(len(new_lista))
    if len(new_lista) % 2 == 0:
        pc = random.choice(new_lista)
        pc.invoke()

    again = winer(symboy_player,buttom1, buttom2, buttom3, buttom4, buttom5, buttom6, buttom7, buttom8, buttom9)
    if again:
        for button in lista_butom:
            if button['bg'] != 'light gray':
                texto = button['text']
                cont_color += 1
                if cont_color == 3:
                    cont_color = 0
                    if texto == symboy_player:
                        player_wins += 1
                        placar1.set(f'  {name1}  \n\n  {player_wins}')

                    else:
                        pc_wins += 1
                        placar2.set(f'  IA  \n\n  {pc_wins}')


    if again:
        for buttom in  lista_butom:
            buttom['state'] = 'normal'
            buttom['text'] = ''
            buttom['bg'] = 'light gray'
    elif again == False:
        window.destroy()



    new_lista = [button for button in lista_butom if button['state'] == 'normal']

    window.update()

print('fim')

window.mainloop()



