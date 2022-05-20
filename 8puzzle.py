from time import sleep
from tkinter import *
import tkinter.font as font
from search import *

root = Tk("Screen")
FONT_SIZE = font.Font(root,size=40)
BACKGROUND_COLOR = "dodgerblue"
FOREGROUND_COLOR = "white"
root.title = "EightPuzzle Solver Visualization"

def blank_move(action,btn):
    if action == "UP" or action == "DOWN":
        row_blank = blank_square.grid_info()['row']
        row_clicked_btn = btn.grid_info()['row']

        blank_square.grid(row=row_clicked_btn)
        btn.grid(row=row_blank)
    elif action == "RIGHT" or action == "LEFT":
        col_blank = blank_square.grid_info()['column']
        col_clicked_btn = btn.grid_info()['column']

        blank_square.grid(column=col_clicked_btn)
        btn.grid(column=col_blank)
    sleep(0.4)
        
def task(event):
    clicked_btn = event.widget
    row_blank = blank_square.grid_info()['row']
    col_blank = blank_square.grid_info()['column']
    row_clicked_btn = clicked_btn.grid_info( )['row']
    col_clicked_btn = clicked_btn.grid_info()['column']
    
    if (row_blank,col_blank) == (row_clicked_btn,col_clicked_btn-1):
        blank_move("RIGHT",clicked_btn)
    elif (row_blank,col_blank) == (row_clicked_btn,col_clicked_btn+1):
        blank_move("LEFT",clicked_btn)
    elif (row_blank,col_blank) == (row_clicked_btn + 1,col_clicked_btn):
        blank_move("UP",clicked_btn)
    elif (row_blank,col_blank) == (row_clicked_btn - 1,col_clicked_btn):
        blank_move("DOWN",clicked_btn)
    else:
        pass

def read_and_move_gui(action:str):
    row_blank = blank_square.grid_info()['row']
    col_blank = blank_square.grid_info()['column']

    #tinh ra toa do(row,col) cua vi tri nut can doi cho
    if action == "UP":
        row_dest = row_blank -1
        col_dest = col_blank
    elif action == "DOWN":
        row_dest = row_blank + 1
        col_dest = col_blank
    elif action == "LEFT":
        row_dest = row_blank
        col_dest = col_blank - 1
    elif action == "RIGHT":
        row_dest = row_blank
        col_dest = col_blank + 1

    #lay duoc nut can doi cho
    btn_dest = None
    for btn in btn_list:
        if (btn.grid_info()['row'] == row_dest) and (btn.grid_info()['column'] == col_dest):
            btn_dest = btn
            break
    
    #doi cho blank square va btn_dest
    blank_move(action,btn_dest)


#tao gui tu state
problem = EightPuzzleProblem(initial=(3, 1, 2, 6, 0, 8, 7, 5, 4), goal=(0, 1, 2, 3, 4, 5, 6, 7, 8))
initial_state = problem.initial
btn_list = []
for i, val in zip( range(0,len(initial_state)) , initial_state ):
    if val == 0:
        blank_square = Button(root,text=" ",bg="white",font=FONT_SIZE,padx=20,pady=20) 
        blank_square.grid(row=int(i/3),column=int(i%3),padx=10,pady=10)
    else:
        btn = Button(root,text=str(val),bg=BACKGROUND_COLOR,fg=FOREGROUND_COLOR,font=FONT_SIZE,padx=20,pady=20) 
        btn.grid(row=int(i/3),column=int(i%3),padx=10,pady=10)
        btn_list.append(btn)

for btn in btn_list:
    btn.bind("<Button-1>",task)

def task1():
    result = iterative_deepening_search(problem)
    actions_lst = result.solution()

    for action in actions_lst:
        #sleep(0.5)
        read_and_move_gui(action)
        root.update()

def task2():
    result = breadth_first_graph_search(problem)
    actions_lst = result.solution()

    for action in actions_lst:
        #sleep(0.5)
        read_and_move_gui(action)
        root.update()


btn_ids = Button(root,text="Iterative Deepening Search",borderwidth=4,command=task1)
btn_ids.grid(row=0,column=3,padx=30,pady=30)
btn_bfs = Button(root,text="Breath First Search",borderwidth=4,command=task2)
btn_bfs.grid(row=1,column=3,padx=30,pady=30)


root.geometry("800x800")
root.mainloop()
#TO DO 
#reset()
#suy nghi neu o col 0 ma di chuyen sang phai thi sao
# con nhieu loi lien quan toi ko dong bo giua state va gui
# nen neu read_and_move khi ko dong bo se ra sai