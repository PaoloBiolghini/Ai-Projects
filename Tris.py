import numpy as np


class State:
    def __init__(self,array):
        self.state=array
        self.dict = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}


    def printState(self):
        print("------ACTUAL-STATE------")
        print(self.state[0])
        print(self.state[1])
        print(self.state[2], "\n\n")

    def insertchoice(self,player):
        n = input("MAKE A CHOICE (1-9): ")

        while (True):

            if(n.isnumeric):
                n=int(n)

                if( (self.state[self.dict[n][0]][self.dict[n][1]]=="-")):
                    break


            print("ACTION NOT ALLOWED \n ")
            n = input("sELECT AN ACTION :")


        print(self.dict[n][0])
        self.addchoice([self.dict[n][0],self.dict[n][1]],player)
        return

    def addchoice(self,pos,player):
       self.state[pos[0]][pos[1]]=player




class MinMax:
    def __init__(self):

        self.value=0
        self.dafare=[0,0]

    def check(self,state):

        for n in range(3):
            if(self.checkrow(state[n])):
                return [True,self.value]
            if (self.checkrow( [state[0][n],state[1][n],state[2][n]])):
                return [True,self.value]

        if (self.checkrow([state[0][0], state[1][1], state[2][2]])):
            return [True,self.value]

        if (self.checkrow([state[0][2], state[1][1], state[2][0]])):
            return [True,self.value]

        finished = True
        for i in range (3):
            for j in range(3):
                if(state[i][j]=="-"):
                    finished=False
        if(finished):
            self.value=0
            return [True,0]

        return [False,None]

    def checkrow(self,riga):
        if(riga[0]==riga[1] and riga[1]==riga[2] and riga[0]!="-"):
            if(riga[0]=="X"):
                self.value=1
            else:
                self.value=-1
            return True
        return False

    def action(self,state):
        actions=[]
        for x in range(3):
            for y in range(3):
                if(state[x][y]=="-"):
                    actions.append([x,y])
        return actions

    def makeaction(self,stato,action,player):
        stato[action[0]][action[1]]=player
        return stato

    def Min(self, state):
        v = 2
        dafare = []
        res = self.check(np.copy(state))
        if (res[0]):
            v = res[1]
            return v

        azioni = self.action(np.copy(state))
        for a in azioni:
            vn = self.Max(self.makeaction(np.copy(state), a, "O"))
            if (v > vn):
                v = vn
                dafare = a
        
        self.dafare = dafare
        return v

    def Max(self, state):
        v = -2
        dafare = []
        res = self.check(np.copy(state))
        if (res[0]):
            v = res[1]
            return v

        
        azioni = self.action(np.copy(state))
        for a in azioni:
            
            vn = self.Min(self.makeaction(np.copy(state), a, "X"))
            if (v < vn):
                v = vn
                dafare = a
        
        self.dafare=dafare
        return v

#initialize algorithm

print("WELCOME TO TIC TAC TOE")
turno=0

Ai=MinMax()
tab=State([["-","-","-"],["-","-","-"],["-","-","-"]])
while(True):
    print("\n\nTURN ",turno)


    if(turno%2==0):
        print("YOUR TURN")
        tab.printState()
        tab.insertchoice("X")
    else:
        print("AI TURN")
        tab.printState()
        Ai.Min(np.copy(tab.state))
        tab.addchoice(Ai.dafare,"O")

    turno=turno+1
    if(Ai.check(np.copy(tab.state))[0]):
        break
    
#check final result and print related prompt
if(Ai.value==1):
    print("YOU WON, CONGRATULATIONS")
elif Ai.value==0:
    print("TIE; U WILL NEVER BEAT ME")
else:
    print("I WON, EZ GAME")

tab.printState()