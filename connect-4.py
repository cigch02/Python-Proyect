import pyfiglet
import os

class Print_Board:
    
    def __init__(self, board=""):
        self.board = board
    
    def __repr__(self):
        print_board = "  "
        cont=0
        for i in range(7):
            print_board +=  str(i+1) + "   "
        print_board += "\n"
        for x in range(13):
            if not x % 2 == 0:
                print_board += "|" 
                for p in range(7):
                    print_board += " " + self.board[cont][p] + " |"
                cont += 1
                print_board += "\n"
            else:
                print_board += "+---+"
                for p in range(6):
                    print_board += "---+"
                print_board += "\n"
        return print_board
    
    def title(self, choose, name=""):
        match choose:
            case 1:
                return pyfiglet.figlet_format("Connect 4", width=200)
            
            case 2:
                return pyfiglet.figlet_format(name, width=200)
            
            case 3:
                return pyfiglet.figlet_format("Congratulation: "+name, width=200)
            
class Win:
    def __init__(self, board):
        self.symbol = ""
        self.board = board
    
    def check_player(self, symbol):
        self.symbol = symbol
        for x in range(7):
            for y in range(6):
                if self.board[y][x] == self.symbol:
                    if self.check_direction(y,x):
                        return True
        return False
        
    def check_direction(self,y,x):
        for i in range(9):
            coord_x = x
            coord_y = y
            match i:
                case 0:
                    for p in range(4):
                        if coord_y >= 0 and coord_x>=0 and coord_y < 6 and self.board[coord_y][coord_x] == self.symbol:
                            coord_y += 1
                    if abs(coord_y - y) == 4:
                        return True
                    
                case 1:
                    for p in range(4):
                        if coord_y >= 0 and coord_x>=0 and coord_y < 6 and self.board[coord_y][coord_x] == self.symbol:
                            coord_y -= 1
                    if abs(y - coord_y) == 4:
                        return True
                
                case 2:
                    for p in range(4):
                        if coord_y >= 0 and coord_x>=0 and coord_x < 7 and self.board[coord_y][coord_x] == self.symbol:
                            coord_x += 1
                    if abs(coord_x - x) == 4:
                        return True
                
                case 3:
                    for p in range(4):
                        if coord_y >= 0 and coord_x>=0 and coord_x < 7 and self.board[coord_y][coord_x] == self.symbol:
                            coord_x -= 1
                    if abs(x - coord_x) == 4:
                        return True
                
                case 4:
                    for p in range(4):
                        if coord_y >= 0 and coord_y < 6 and coord_x >= 0 and coord_x < 7 and self.board[coord_y][coord_x] == self.symbol:
                            coord_y += 1
                            coord_x += 1
                    if abs(coord_x - x) == 4 and abs(coord_y - y) == 4:
                        return True
                
                case 5:
                    for p in range(4):
                        if coord_y >= 0 and coord_y < 6 and coord_x >= 0 and coord_x < 7 and self.board[coord_y][coord_x] == self.symbol:
                            coord_y -= 1
                            coord_x -= 1
                    if abs(x - coord_x) == 4 and abs(y - coord_y) == 4:
                        return True
                
                case 6:
                    for p in range(4):
                        if coord_y >= 0 and coord_y < 6 and coord_x >= 0 and coord_x < 7 and self.board[coord_y][coord_x] == self.symbol:
                            coord_y -= 1
                            coord_x += 1
                    if abs(x + coord_x) == 4 and abs(y - coord_y) == 4:
                        return True
                
                case 7:
                    for p in range(4):
                        if coord_y >= 0 and coord_y < 6 and coord_x >= 0 and coord_x < 7 and self.board[coord_y][coord_x] == self.symbol:
                            coord_y += 1
                            coord_x -= 1
                    if abs(x - coord_x) == 4 and abs(y + coord_y) == 4:
                        return True
                    
                case _:
                    return False
                        
class Player(Win, Print_Board):
    def __init__(self,board):
        self.board = board
        self.sybol = ""
        self.name = ""
        self.move = []
        Win.__init__(self, self.board)
        Print_Board.__init__(self, self.board)
    
    def __repr__(self):
        print("Ingrese su nombre: ")
        self.name = input()
        return ""

    def Move(self):
        bypass = 0
        while bypass == 0:
            os.system("cls")
            print(Print_Board.title(self,2,self.name))
            print(Print_Board.__repr__(self))
            try:
                print("Ingrese su movimiento: ")
                self.move.append(int(input()))
                if self.check():
                    bypass = 1
                else:
                    self.move.pop()
            except:
                print("Se ingreso el movimiento incorrecto")
        
        print(self.move)
        for i in range(5,0,-1):
            if self.board[i][self.move[len(self.move)-1]-1] == " ":
                self.board[i][self.move[len(self.move)-1]-1] = self.sybol
                break
            else:
                print("No se puede ingresar ese movimiento")
        
        os.system("cls")
        print(Print_Board.__repr__(self))
        input("Presione enter para continuar")
        
    def check(self):
        last = self.move[len(self.move)-1]
        for i in range(7):
            if last == (i+1):
                return True
        
        return False
    
bypass = 0
board = [[" " for j in range(7)] for i in range(6)]

print_title = Print_Board(board)
print(print_title.title(1))
print(print_title)
input("Presione enter para continuar")
os.system("cls")
print(print_title.title(2,"Player 1"))
player1 = Player(board)
print(player1)
while bypass == 0:
    print("""
Ingrese que ficha quiere ser:
1. X
2. Y""")
    choose = input()
    match choose:
        case "1":
            player1.sybol = "X"
            bypass = 1
        case "2":
            player1.sybol = "Y"
            bypass = 1
        case _:
            print("Ingreso una opcion incorrecta")
os.system("cls")
print(print_title.title(2,"Player 2"))
player2 = Player(board)
print(player2)
if player1.sybol == "X":
    player2.sybol = "Y"
else:
    player2.sybol = "X"


bypass = 0
      

while bypass == 0:
    os.system("cls")
    player1.Move()
    if player1.check_player(player1.sybol):
        bypass = 1
        print(print_title.title(3, player1.name))
        input("Presione enter para continuar")
        break
    
    os.system("cls")
    player2.Move() 
    if player2.check_player(player2.sybol):
        bypass = 1
        print(print_title.title(3, player2.name))
        input("Presione enter para continuar")
        break

