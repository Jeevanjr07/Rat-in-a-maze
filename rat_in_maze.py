# anirudh and jeevan cs 1c
from tkinter import *
w1=Tk()
w1.title('INSTRUCTIONS')
w1.config(bg="goldenrod")
a=Label(w1,text="CS MINI PROJECT",font="Ariel 20 bold italic",bg="light yellow").place(x=500,y=20)
a=Label(w1,text="RAT MAZE USING RECURSIVE TECHNIQUE",font="arial 25 bold ",bg="light yellow").place(x=300,y=70)
a=Label(w1,text="MAIN CONCEPTS USED IS BACKTRACKING ALGORITM AND RECURSIVE FUNCTIONS.......",font="arial 15 bold",bg="light yellow").place(x=10,y=170)
a=Label(w1,text="Here are some instructions for the user to be followed: ",font="arial 15 bold italic",bg="goldenrod").place(x=10,y=200)
a=Label(w1,text="1.ENTER THE MAZE( SHOULD BE TYPE INT )",font="arial 15 bold italic",bg="goldenrod").place(x=10,y=230)
a=Label(w1,text="2.ENTER THE MATRIX USING 1s and 0s ONLY",font="arial 15 bold",bg="goldenrod").place(x=10,y=260)
a=Label(w1,text="3.THE ELEMENTS OF THE SUCCESSIVE COLUMNS SHOULD BE SEPERATED BY A BLANK SPACE ",font="arial 15 bold italic",bg="goldenrod").place(x=10,y=290)
a=Label(w1,text="4.THE ELEMENTS ARE ENTERED ROW-WISE",font="arial 15 bold italic",bg="goldenrod").place(x=10,y=320)
a=Label(w1,text="....................................................................................................................................................................................................................................................................................................................................",font="arial 15 bold",bg="goldenrod").place(x=0,y=350)
a=Label(w1,text="....................................................................................................................................................................................................................................................................................................................................",font="arial 15 bold",bg="goldenrod").place(x=0,y=380)
a=Label(w1,text="THE OUTPUT PAGE COMPRISES OF TWO MAZE: 1.USER DEFINED MATRIX",font="arial 15 bold italic",bg="goldenrod").place(x=10,y=410)
a=Label(w1,text="                                                                                2.MATRIX DEPICTING THE PATH OF THE RAT",font="arial 15 bold italic",bg="goldenrod").place(x=10,y=440)
a=Label(w1,text="IN THE INPUT MATRIX: THE BLACK COLOUR DEPICTS THE 0s  ",font="arial 15 bold italic",bg="goldenrod").place(x=10,y=470)
a=Label(w1,text="                                       THE WHITE COLOUR DEPICTS THE 1s ( which was entered by the user ) ",font="arial 15 bold italic",bg="goldenrod").place(x=10,y=500)
a=Label(w1,text="IN THE OUTPUT MATRIX: THE GREEN COLOUR BLOCKS DEPICTS THE PATH OF THE RAT ",font="arial 15 bold italic",bg="goldenrod").place(x=10,y=530)
IHV=Button(w1,bg='light goldenrod',text='I HAVE UNDERSTOOD',command=w1.destroy,font='ariel 15 bold italic').place(x=500,y=600)
w1.geometry("10000x10000")
w1.mainloop()
w2=Tk()
w2.configure(background='goldenrod')
w2.title('RAT MAZE USING RECURSION')
w2.geometry('1350x1000')
welcome=Label(w2,bg='light goldenrod',text='WELCOME TO THE RAT MAZE SOLVER',font=("Helvetica",30,"bold italic"))
welcome.place(x=300,y=20)
size_var=StringVar()
size_label=Label(w2,text='Enter the size of the maze:',bg='light goldenrod',font=("Helvetica",15,"bold italic"))
size_entry=Entry(w2,bg='light goldenrod',highlightcolor='light yellow',textvariable=size_var,font=("Helvetica",15,"bold italic"))
size_button=Button(w2,bg='light goldenrod',text='CONFIRM',fg='red',command=w2.destroy,font=("Helvetica",15,"bold italic"))
size_label.place(x=400,y=100)
size_entry.place(x=660,y=100)
size_button.place(x=600,y=150)
w2.mainloop()
def solnmaze(success):
    print("THE PATH FOLLOWED BY THE RAT :")                           #PRINTS THE FINAL OUTPUT
    for i in success:
        for j in i:
            print(str(j) + " ", end="")
        print("")

def valid(maze, x, y):                                              #CHECKS IF THE POSITION OF THE RAT IS VALID
    if x >= 0 and x < size and y >= 0 and y < size and maze[x][y] == 1:
        return True

    else:
        return False

def rat(maze,size):
    success=[[0 for j in range(size)] for i in range(size)]     #creating a NxN

    if solveit(maze,0,0,success)==False:
        print("Path doesnt exist.....")
        return False

    solnmaze(success)
    return success

def solveit(maze,x,y,success):

    if x==size-1 and y==size-1 and maze[x][y]==1:     #checking if the end element is 1
        success[x][y]=1
        return True

    if valid(maze,x,y)==True:

        if success[x][y]==1:                      #does not allows the rat to move back in the path
            return False

        success[x][y]=1

        if solveit(maze,x,y+1,success)==True:     #moving up in y direction
            return True
        if solveit(maze,x+1,y,success)==True:     #if moving down in y direction doesnt give solution.......moves forward in x direction
            return True
        if solveit(maze,x-1,y,success)==True:     #if moving forward in x direction doesnt give solution......moves back in x direction
            return True
        if solveit(maze,x,y-1,success)==True:     # if moving backward in x direction doesnt give solution.....moves down in y direction
            return True

        success[x][y]=0
        return False




def inputmaze(n):                                                #TAKES INPUT OF THE MAZE
    maze=[]
    for i in range(n):
        maze.append([])
    print("**** ENTER THE MAZE VALUES WITH ONLY 0s and 1s ****")
    print("ENTER THE MAZE:")
    for i in range(n):
        print('ENTER THE ELEMENTS OF ROW',i+1,':')
        print('THE ELEMENTS OF SUCCESSIVE COLUMNS MUST BE SEPARATED BY BLAK SPACES')
        columnele=input()
        columnl=columnele.split()
        print(columnl)
        while len(list(filter(lambda x:x=='1' or x=='0',columnl)))!=n:
            print('THE ENTERED ROW HAS EITHER INCORRECT DIGITS OR THE NO. OF COLUMNS IS LESS')
            print('PLEASE RE-ENTER ROW',i+1,':')
            columnele=input()
            columnl=columnele.split()
        for j in columnl:
            maze[i].append(int(j))

    return maze

size=int(size_var.get())
maze=inputmaze(size)
solution=rat(maze,size)
print("THE ENTERED MAZE IS:")
for i in range(size):
    for j in range(size):
        print(maze[i][j],end=" ")
    print()
print(maze)

w=Tk()
w.configure(bg='goldenrod')
w.title('RAT IN A MAZE')
aa=Label(w,text='RAT IN A MAZE USING RECURSIVE TECHNIQUE',font='Ariel 20 bold',bg='light yellow1').place(x=300,y=50)
w.geometry('1350x1000')
il=Label(w,bg='goldenrod',text='INPUT MAZE:',font=('Helvetica','16','bold'))
il.place(x=400,y=150)
ol=Label(w,bg='goldenrod',text='SOLUTION:',font=('Helvetica','16','bold'))
ol.place(x=700,y=150)
for i in range(size):
    for j in range(size):
        if maze[i][j]==0:
            white=Label(w,bg='black',bd=4,width='4',height='2')
            white.place(x=400+44*j,y=(200+44*i))
        else:
            white=Label(w,bg='red',bd=4,width='4',height="2")
            white.place(x=400 + 44*j,y=200 + 44 * i)

for i in range(size):
    for j in range(size):
        if maze[i][j]==1 and solution[i][j]==1:
            white=Label(w,bg='green',bd=4,width='4',height='2')
            white.place(x=700+44*j,y=(200+44*i))
        else:
            white=Label(w,bg='black',bd=4,width='4',height="2")
            white.place(x=700 + 44 * j,y=200 + 44 * i)

bb=Label(w,text='THANK YOU.........   :)  :)  ',font='Ariel 30 bold',bg="light yellow")
bb.place(x=400,y=350)
q=Button(w,bg='light goldenrod',text='QUIT',font='Ariel 15 bold',command=w.destroy)
q.place(x=600,y=500)
w.mainloop()