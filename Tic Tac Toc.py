import os
import pyfiglet


class Print_Table:
    def __init__(self,tablet):
        self.tablet = tablet
        self.i=0
        self.board = ""
        
    def __repr__(self):
        self.i=0
        self.board = ""
        for x in range(6):
            if x == 0:
                self.board += "   a   b   c \n"
            elif not x % 2 == 0:
                self.board += "{i}  {t1} | {t2} | {t3} \n".format(i = self.i+1, t1 = self.tablet[self.i][0],t2 = self.tablet[self.i][1],t3 = self.tablet[self.i][2])
                self.i += 1
            else:
                self.board += "  ---|---|---\n"
        return self.board

    def Print_Tittle(self):
        self.text = "Tic Tac Toc"
        self.ascii_art = pyfiglet.figlet_format(self.text)
        print(self.ascii_art)
        print("\x1B[4m Tic Tac Toc \x1B[0m \n")
        print(print_table)


class Player:
    def __init__(self,name,symbol):
        self.name = name
        self.position = []
        self.symbol = symbol

    def Write_Position(self,table):
        postion = [0]*2
        Bypass = 0
        print(postion)
        while Bypass == 0:
            postion = [0]*2
            pos = input("Posicion: ").lower()
            if len(pos) == 2:
                self.position.append(pos)
                Bypass = 1
                for y in pos:
                    if y == "1" or y == "2" or y == "3":
                        postion[0] = int(y)-1
                    else:
                        match y:
                            case "a":
                                postion[1] = 0
                            case "b":        
                                postion[1] = 1
                            case "c":
                                postion[1] = 2
            else:
                print("Ingreso incorrecto")
            if table[postion[0]][postion[1]] == "X" or table[postion[0]][postion[1]] == "O":    
                print("Posicion ocupada")
                Bypass = 0
            else:
                table[postion[0]][postion[1]] = self.symbol
        
    def Menu_Player(self,tablet):
        i="2"
        while i == "2":
            os.system("cls")
            print("\x1B[4m Tic Tac Toc \x1B[0m \n")
            print(print_table)
            i = input("""
Jugador: {name}
1. Escribir Posicion
2. Historial de Posiciones
""".format(name = self.name))
            if len(i) == 1:
                match i:    
                    case "1":
                        self.Write_Position(tablet)
                    case "2":
                        print("Historial de Posiciones")
                        print(self.position)
                        input("Press Enter to continue...")
            else:
                i="2"
                print("Ingreso incorrecto")
                input("Press Enter to continue...")
    
    
    def Win_Player(self,tablet):
        return wincondition.Win_Condition(self.symbol)

class Wincondition:
    def __init__(self,tablet):
        self.tablet = tablet
    
    def Win_Condition(self,player):
        for x in range(3):
            if self.tablet[x][0] == player and self.tablet[x][1] == player and self.tablet[x][2] == player:
                return True
            elif self.tablet[0][x] == player and self.tablet[1][x] == player and self.tablet[2][x] == player:
                return True
        if self.tablet[0][0] == player and self.tablet[1][1] == player and self.tablet[2][2] == player:
            return True
        elif self.tablet[0][2] == player and self.tablet[1][1] == player and self.tablet[2][0] == player:
            return True
        else:
            return False
        
tablet = [[" "," "," "],[" "," "," "],[" "," "," "]]
print_table = Print_Table(tablet)
wincondition = Wincondition(tablet)
game = 0
print_table.Print_Tittle()
player1 = Player(input("Player 1: "),"X")
player2 = Player(input("Player 2: "),"O")


os.system("cls")
while game == 0:
    player1.Menu_Player(tablet)
    print(print_table)
    input("Press Enter to continue...")

    if player1.Win_Player(tablet):
        text = "Winner"
        ascii_art = pyfiglet.figlet_format(text)
        print(ascii_art)
        print("Ganador: {name}".format(name = player1.name))
        game = 1
        input("Press Enter to continue...")
        break
    
    player2.Menu_Player(tablet)
    print(print_table)
    input("Press Enter to continue...")
    
    if player2.Win_Player(tablet):
        text = "Winner"
        ascii_art = pyfiglet.figlet_format(text)
        print(ascii_art)
        print("Ganador: {name}".format(name = player2.name))
        game = 1
        input("Press Enter to continue...")
        break
    

