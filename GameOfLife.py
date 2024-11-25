from tkinter import *
from PIL import Image, ImageTk


class GameofLife(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(fill=BOTH, expand=1)
        self.master.title("THE GAME OF LIFE")
        self.configure(bg="darkslategray")
        self.continuous = 1
        self.frame = Frame(self, bg="darkslategray")
        self.frame.pack(side=TOP, expand=1)
        self.label = Label(self.frame, text="THE GAME OF LIFE",
                           font=("System", "20", "bold"), fg="WHITE", bg="gray8",
                           width=30, height=5, relief=SUNKEN)
        self.label.pack(side=TOP, fill=X, expand=1)

        self.framemid = Frame(self, bg="darkslategray")
        self.framemid.pack(fill=X, expand=1)
        self.frame1 = Frame(self.framemid, bg="darkslategray")
        self.frame1.pack(side=RIGHT)
        self.ins = Label(self.frame1, fg="snow", bg="gray8", width=80, height=10,
                         font=("MS Sans Serif", "14", "bold"), relief=GROOVE,
                         text="""WELCOME TO THE GAME OF LIFE:\n
         An interactive game with a cellular automaton system where simple rules 
         lead to complex behaviors. The game simulates a world in a 2D grid where 
         cells live or die based on their neighbors' states. This game is dedicated 
         to the memory of John H. Conway, who inspired mathematical and computational 
         minds worldwide. He passed away on April 11 due to COVID-19.
                             """)
        self.ins.pack(pady=20, ipady=20, ipadx=40, side=RIGHT, fill=X, expand=1)

        self.frame2 = Frame(self.framemid, bg="darkslategray", relief=GROOVE)
        self.frame2.pack(side=LEFT)
        self.ima = ImageTk.PhotoImage(Image.open("Conwayy.JPG"))
        self.lab = Label(self.frame2, image=self.ima)
        self.lab.pack()
        self.lab2 = Label(self.frame2, fg="snow", bg="gray8", font=("MS Sans Serif", "13", "bold"), relief=SUNKEN,
                          text="In memory of: \nJohn Horton Conway\n1937-2020")
        self.lab2.pack(side=BOTTOM, ipadx=5)

        self.frame3 = Frame(self, bg="darkslategray", relief=SUNKEN)
        self.frame3.pack(side=BOTTOM, fill=Y, expand=1)
        self.btnstart = Button(self.frame3, text="START GAME", font=("Comic Sans MS", "13", "bold"), fg="snow",
                               bg="forest green", command=self.GridGUI)
        self.btnstart.pack(side=LEFT, ipady=15, ipadx=15, padx=30, anchor="w")
        self.btninstr = Button(self.frame3, text="INSTRUCTIONS", font=("Comic Sans MS", "13", "bold"), fg="snow",
                               bg="DodgerBlue4", command=self.Instructions)
        self.btninstr.pack(side=RIGHT, ipady=15, ipadx=15, padx=30, anchor="e")

        self.mainloop()

    def Instructions(self):
        root = Tk()
        root.title("Instructions")
        root.geometry('960x600')

        l1 = Label(root, text="INSTRUCTIONS", font=("System", "20", "bold"), bg='gray8', fg="snow", relief=SUNKEN,
                   height=3, width=15)
        l1.pack(fill=X)

        l2 = Label(root, text="""The game can be either interactive or purely visual.
        Click on black cells to bring them to life. Press START to see the evolution 
        of patterns. Use PAUSE to stop, RESET to clear the grid, and PREDETERMINED 
        to explore predefined patterns. Adjust speed with the buttons below. 
        Press HELP anytime to revisit this panel.""",
                   font=("MS Sans Serif", "14"), bg='DodgerBlue4', fg="snow", relief=GROOVE, height=8, width=10)
        l2.pack(fill=X, padx=2)

        f34 = Frame(root)
        f34.pack(fill=BOTH, expand=1)
        l3 = Label(f34, text="1. BIRTH: A dead cell with \nexactly 3 neighbors comes to life.",
                   font=("MS Sans Serif", "14"), bg='forest green', fg="snow", relief=GROOVE, width=5)
        l3.pack(side=LEFT, fill=BOTH, expand=1)

        l4 = Label(f34,
                   text="2. SURVIVAL: A live cell with 2 \nor 3 neighbors survives.",
                   font=("MS Sans Serif", "14"), fg="snow", bg='forest green', relief=GROOVE, width=5)
        l4.pack(side=RIGHT, fill=BOTH, expand=1)

        f56 = Frame(root)
        f56.pack(fill=BOTH, expand=1)
        l5 = Label(f56,
                   text="3. DEATH: More than 3 living neighbors cause the \ndeath in the next instant for overpopulation",
                   font=("MS Sans Serif", "14"), fg="snow", bg='forest green', relief=GROOVE, width=5)
        l5.pack(side=LEFT, fill=BOTH, expand=1)

        l6 = Label(f56,
                   text="4. DEATH: Less than 2 alive neighbors can cause the \ndeath in the next instant for loneliness",
                   font=("MS Sans Serif", "14"), fg="snow", bg='forest green', relief=GROOVE, width=5)
        l6.pack(side=LEFT, fill=BOTH, expand=1)

    def GridGUI(self):
        self.btnstart.destroy()
        self.ins.destroy()
        self.label.destroy()
        self.frame.destroy()
        self.framemid.destroy()
        self.frame1.destroy()
        self.frame2.destroy()
        self.frame3.destroy()

        self.general_grid = Frame(self, bg="black")
        self.general_grid.grid(padx=(10, 10), pady=(8, 8), row=2, column=1)
        self.rate = 500
        self.code = 0
        self.coloralive = "white"
        self.colordead = "black"
        self.varop = StringVar(self)
        self.varrad = IntVar(self)
        self.varop.set("PREDETERMINED")
        self.varrad.set(500)
        self.shapes = {"SpaceShip", "10 Cell Row", "Gosper Glider Gun", "Butterfly", "R-Pentomino",
                       "Glider", "XKCD John Conway", "Baby Plane", "Puffer Train", "STAR WARS Exploder"}
        self.options = OptionMenu(self, self.varop, *self.shapes, command=self.Predetermined)
        self.options.config(width=20, bg="forest green")
        self.options.grid(row=0, column=0, sticky=W)
        self.bhelp = Button(self, text="HELP", bg="DodgerBlue4", command=self.Instructions)
        self.bhelp.grid(row=0, column=1, sticky=W)
        self.act = Button(self, text="START", bg="forest green", command=self.GameAlgorithm)
        self.act.grid(row=0, column=1, sticky=E, pady=1)
        self.stop = Button(self, text="PAUSE", bg="tomato", state=NORMAL, command=self.StopMotion)
        self.stop.grid(row=0, column=2, sticky=W + E)
        self.restart = Button(self, text="RESET", bg="tomato", state=NORMAL, command=self.Restart)
        self.restart.grid(row=0, column=3, sticky=E)
        self.framerad = Frame(self, bg="darkslategray")
        self.framerad.grid(row=1, column=2, sticky=W)
        self.R1 = Radiobutton(self.framerad, text="Slower", variable=self.varrad,
                              value=1000, command=self.Speed, bg="forest green", relief=RAISED)
        self.R1.grid(sticky=W + E, pady=1)
        self.R2 = Radiobutton(self.framerad, text="Normal", variable=self.varrad,
                              value=500, command=self.Speed, bg="forest green", relief=RAISED)
        self.R2.grid(sticky=W + E, pady=1)
        self.R3 = Radiobutton(self.framerad, text="Faster", variable=self.varrad,
                              value=100, command=self.Speed, bg="forest green", relief=RAISED)
        self.R3.grid(sticky=W + E, pady=1)

        score = Frame(self, bg="forest green")
        score.place(relx=0.5, y=30, anchor="center")
        Label(score, text="LIVING CELLS: ", font=("System", "17", "bold"), bg="forest green", relief=GROOVE).grid(row=0)
        self.scorelabel = Label(score, text=" " + str(self.code), font=("System", "17"), bg="forest green",
                                relief=GROOVE)
        self.scorelabel.grid()
        self.cells = []
        for i in range(20):
            row = []
            self.cells.append(row)
            for j in range(40):
                self.cells[i].append(Button(self.general_grid, bg=self.colordead, width=2, height=1))
                self.cells[i][j].configure(command=lambda i=i, j=j: self.SwitchColor(i, j))
                self.cells[i][j].grid(row=i, column=j, padx=1, pady=1, sticky=N + S)

    def GameAlgorithm(self):
        # Se crea la lógica de movimiento del juego de la vida
        if self.continuous == 1:
            self.continuous = 2
        self.behavior = []
        for i in range(20):
            for j in range(40):
                bwcoord = (i, j)
                # Cuando una celula muerta tiene 3 vecinos vivos y nace:
                if self.cells[i][j]['bg'] == self.colordead and self.neighbourbehavior(i, j) == 3:
                    self.behavior.append(bwcoord)
                # Cuando una célula viva no contiene 2 o 3 vecinos vivos y muere:
                elif self.cells[i][j]['bg'] == self.coloralive and self.neighbourbehavior(i,
                                                                                          j) != 3 and self.neighbourbehavior(
                        i, j) != 2:
                    self.behavior.append(bwcoord)

        for a in self.behavior:
            self.SwitchColor(a[0], a[1])

        if len(self.behavior) != 0 and self.continuous == 2:
            self.after(self.rate, self.GameAlgorithm)

        else:
            self.continuous = 1

    def SwitchColor(self, i, j):
        if self.cells[i][j]["bg"] == self.coloralive:
            self.cells[i][j].configure(bg=self.colordead)
            self.code -= 1

        else:
            self.cells[i][j].configure(bg=self.coloralive)
            self.code += 1

        self.scorelabel.configure(text=" " + str(self.code))

    def neighbourbehavior(self, i, j):
        c = 0
        for a in range(i - 1, i + 2):
            for b in range(j - 1, j + 2):
                if a >= 0 and b >= 0 and a < 20 and b < 40:
                    if a == i and b == j:
                        pass
                    elif self.cells[a][b]["bg"] == self.coloralive:
                        c += 1
        return c

    def StopMotion(self):
        self.continuous = 3

    def Restart(self):
        for i in range(20):
            for j in range(40):
                if self.cells[i][j]["bg"] == self.coloralive:
                    self.SwitchColor(i, j)

    def Speed(self):
        self.rate = self.varrad.get()

    def Predetermined(self, event):
        comms1 = [(11, 17), (11, 18), (11, 19), (11, 20), (12, 16), (12, 20), (13, 20), (14, 16), (14, 19)]

        comms2 = [(8, 18), (8, 19), (8, 21), (8, 22), (9, 18), (9, 19), (9, 21), (9, 22), (10, 19), (10, 21), (11, 17),
                  (11, 19), (11, 21), (11, 23), (12, 17), (12, 19), (12, 21), (12, 23), (13, 17), (13, 18), (13, 22),
                  (13, 23)]

        comms3 = [(3, 24), (3, 25), (3, 35), (3, 36), (4, 23), (4, 25), (4, 35), (4, 36), (5, 1), (5, 2), (5, 10),
                  (5, 11),
                  (5, 23), (5, 24), (6, 1), (6, 2), (6, 9), (6, 11), (7, 9), (7, 10), (7, 17), (7, 18), (8, 17),
                  (8, 19),
                  (9, 17), (10, 36), (10, 37), (11, 36), (11, 38), (12, 36), (15, 25), (15, 26), (15, 27), (16, 25),
                  (17, 26)]

        comms4 = [(11, 14), (11, 15), (11, 16), (11, 17), (11, 18), (11, 19), (11, 20), (11, 21), (11, 22), (11, 23)]

        comms5 = [(4, 15), (5, 16), (6, 14), (6, 15), (6, 16)]

        comms6 = [(7, 15), (8, 14), (8, 15), (8, 16), (9, 14), (9, 16), (10, 15)]

        comms7 = [(9, 4), (9, 5), (9, 6), (10, 4), (10, 6), (11, 4), (11, 6), (12, 5), (13, 2), (13, 4), (13, 5),
                  (13, 6), (14, 3), (14, 5), (14, 7), (15, 5), (15, 8), (16, 4), (16, 6), (17, 4), (17, 6)]

        comms8 = [(7, 13), (7, 15), (7, 17), (8, 13), (8, 17), (9, 13), (9, 17), (10, 13), (10, 17), (11, 13), (11, 15),
                  (11, 17)]

        comms9 = [(11, 24), (11, 25), (12, 23), (12, 24), (13, 24)]

        comms10 = [(12, 5), (12, 6), (12, 7), (13, 4), (13, 7), (14, 7), (15, 7), (16, 17), (17, 7), (18, 6), (16, 10),
                   (17, 10), (17, 11), (18, 10), (18, 11),
                   (12, 14), (13, 13), (13, 14), (13, 15), (14, 12), (14, 13), (14, 15), (12, 20), (13, 19), (13, 20),
                   (13, 21), (14, 19), (14, 21), (14, 22),
                   (16, 24), (17, 23), (17, 24), (18, 23), (18, 24), (12, 27), (13, 27), (14, 27), (15, 27), (16, 27),
                   (17, 27), (18, 28), (12, 28), (12, 29), (13, 30)]

        if self.varop.get() == "SpaceShip":
            for a in comms1:
                self.SwitchColor(a[0], a[1])
        elif self.varop.get() == "Butterfly":
            for a in comms2:
                self.SwitchColor(a[0], a[1])
        elif self.varop.get() == "Gosper Glider Gun":
            for a in comms3:
                self.SwitchColor(a[0], a[1])
        elif self.varop.get() == "10 Cell Row":
            for a in comms4:
                self.SwitchColor(a[0], a[1])
        elif self.varop.get() == "Glider":
            for a in comms5:
                self.SwitchColor(a[0], a[1])
        elif self.varop.get() == "Baby Plane":
            for a in comms6:
                self.SwitchColor(a[0], a[1])
        elif self.varop.get() == "XKCD John Conway":
            for a in comms7:
                self.SwitchColor(a[0], a[1])
        elif self.varop.get() == "STAR WARS Exploder":
            for a in comms8:
                self.SwitchColor(a[0], a[1])
        elif self.varop.get() == "R-Pentomino":
            for a in comms9:
                self.SwitchColor(a[0], a[1])

        elif self.varop.get() == "Puffer Train":
            for a in comms10:
                self.SwitchColor(a[0], a[1])


GameofLife()
