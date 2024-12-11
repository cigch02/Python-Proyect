import os
import pyfiglet


class Print_Table:
    def __init__(self, tablet):
        self.tablet = tablet

    def Print_title(self, var, name=""):
        match var:
            case 1:
                print(pyfiglet.figlet_format("Bienvenido al juego de Batallas Navales", width=200))
            case 2:
                print(pyfiglet.figlet_format("Barcos", width=200))
            case 3:
                print(pyfiglet.figlet_format("Posicion para {name}".format(name = name), width=200))

    def Print_User_Board(self):
        board = ""
        i = 0
        row = ""
        board += pyfiglet.figlet_format("My Board", width=200)
        board += "\n"
        for x in range(18):
            if x == 0:
                board += "   |"
                for j in range(ord('a'), ord('i')+1):
                    board += " {j} |".format(j=chr(j))
                board += "\n"
            elif x % 2 == 0:
                row = ""
                row += " {i} | ".format(i=i)
                for p in range(0, len(self.tablet), 1):
                    row += self.tablet[i][p] + " | "
                board += row
                board += "\n"
                i += 1
            else:
                board += "---"
                for p in range(0, 9, 1):
                    board += "+---"
                board += "+"
                board += "\n"
        return board

    def Print_boards(self):
        self.i = 0
        self.board = ""
        row = ""
        self.board += pyfiglet.figlet_format(
            "My Board     Enemy Board", width=200)
        self.board += "\n\n"
        for x in range(18):
            row = ""
            if x == 0:
                for p in range(2):
                    self.board += "   |"
                    for i in range(ord('a'), ord('i')+1):
                        self.board += " {i} |".format(i=chr(i))
                    for p in range(10):
                        self.board += " "
                self.board += "\n"
            elif x % 2 == 0:
                for space in range(2):
                    row = ""
                    row += " {i} | ".format(i=self.i)
                    for p in range(0, len(self.tablet), 1):
                        row += self.tablet[self.i][p] + " | "
                    for p in range(9):
                        row += " "
                    self.board += row
                self.board += "\n"
                self.i += 1
            else:
                for p in range(2):
                    self.board += "---"
                    for p in range(0, 9, 1):
                        self.board += "+---"
                    self.board += "+"
                    for p in range(10):
                        self.board += " "
                self.board += "\n"
        return self.board


class user(Print_Table):
    
    def __init__(self):
        self.name = ""
        self.board = [[" " for j in range(9)] for i in range(9)]
        self.enemy_board = [[" " for j in range(9)] for i in range(9)]
        self.History_move = [[],[]]
        self.ships = {"Patrullero": "2", "Submarino": "3", "Destructor": "3", "Acorazado": "4", "Portaviones": "5"}
        self.coord = ["a","b","c","d","e","f","g","h","i"]
        super().__init__(self.board)
        

    def __repr__(self):
        
        i = [0]*5
        ship = ""
        super().Print_title(1)
        #print(super().Print_User_Board())
        print("Ingrese su nombre: ")
        self.name = input()
        os.system("cls")
        while 0 in i:
            contador = 1
            super().Print_title(2)
            print("Eliga el barco: ")
            for key in self.ships:
                    print("{contador}. {key}".format(contador=contador, key=key))
                    contador += 1
            ship = input()
            os.system("cls")
            match ship:
                    case "1":
                        if i[0] == 0:
                            self.User_Ships("Patrullero")
                            i[0] = 1
                        else:
                            print("Ya ha elegido este barco")
                    case "2":
                        if i[1] == 0:
                            self.User_Ships("Submarino")
                            i[1] = 1
                        else:
                            print("Ya ha elegido este barco")
                    case "3":
                        if i[2] == 0:
                            self.User_Ships("Destructor")
                            i[2] = 1
                        else:
                            print("Ya ha elegido este barco")
                    case "4":
                        if i[3] == 0:
                            self.User_Ships("Acorazado")
                            i[3] = 1
                        else:
                            print("Ya ha elegido este barco")
                    case "5":
                        if i[4] == 0:
                            self.User_Ships("Portaviones")
                            i[4] = 1
                        else:
                            print("Ya ha elegido este barco")
                    case _:
                        print("Ingreso incorrecto")
                        input("Presione enter para continuar")
                        os.system("cls")
        return 1

    def User_Ships(self,ship):
        bypass = [0,0,1]
        while bypass[0] == 0:
            if bypass[1] == 0:     
                print(super().Print_User_Board())
                print(ship)       
                corrdenada = input("Ingrese la posicion inicial del barco: ")
                bypass[1] = self.Coordenadas(corrdenada,1)
                if bypass[1] == 1:
                    bypass[2] = 0
                os.system("cls")
            elif bypass[2] == 0:
                super().Print_title(3,ship)
                print("""
                  Ingrese que direccion quiere el barco:
                  1. Izquierda
                  2. Derecha
                  3. Arriba
                  4. Abajo
                  5. Cambiar la posicion inicial
                  """)
                direccion = input()
                x = len(self.History_move[0])
                y = len(self.History_move[1])
                items = self.ships.items()
                value = [value for key,value in items if key == ship]
                match direccion:
                    case "1":
                        last = [self.History_move[0][x-1]-int(value[0])+1,self.History_move[1][y-1]]
                        bypass[2] = self.Coordenadas(last,2)
                    case "2":
                        last = [self.History_move[0][x-1]+int(value[0])-1,self.History_move[1][y-1]]
                        bypass[2] = self.Coordenadas(last,2)
                    case "3":
                        last = [self.History_move[0][x-1],self.History_move[1][y-1]-int(value[0])+1]
                        bypass[2] = self.Coordenadas(last,2)
                    case "4":
                        last = [self.History_move[0][x-1],self.History_move[1][y-1]+int(value[0])-1]
                        bypass[2] = self.Coordenadas(last,2)
                    case "5":
                        bypass[1] = 0
                        bypass[2] = 1
                    case _:
                        print("Se ingreso un numero incorrecto")
            else:
                os.system("cls")
                print(super().Print_User_Board())
                last_exit = input("""Se ingreso correctamente el barco?
1. Si   2. No
""")
                if last_exit == "1":
                    bypass[0] = 1
                    os.system("cls")
                else:
                    self.History_move[0].pop()
                    self.History_move[1].pop()
                    bypass[1] = 0
                    bypass[2] = 0
                
    
    def Coordenadas(self,coordenada_direccion,choose):
        match choose:
            case 1:
                if len(coordenada_direccion) == 2:
                    for cord in coordenada_direccion:
                        try:
                            self.History_move[1].append(int(cord))
                        except:
                            self.History_move[0].append(self.coord.index(cord))

                    x = len(self.History_move[0])
                    y = len(self.History_move[1])
                    if x == y and self.board[self.History_move[1][y-1]][self.History_move[0][x-1]] == " ":
                        os.system("cls")
                        self.board[self.History_move[1][y-1]][self.History_move[0][x-1]] = "B"
                        print(super().Print_User_Board())
                        print("Se ingreso una coordenada correcta")
                        input("Presione enter para continuar")
                        return 1
                    else:
                        try:
                            x = len(self.History_move[0])
                            y = len(self.History_move[1])
                            if x>y:
                                result = x-y
                                os.system("cls")
                                for i in range(result):
                                    self.History_move[0].pop()
                                
                                print("Se ingreso una coordenada incorrecta")
                                print(self.History_move)
                                input("Presione enter para continuar")
                                return 0
                            if y>x:
                                result = y-x
                                os.system("cls")
                                for i in range(result):
                                    self.History_move[1].pop()
                                print("Se ingreso una coordenada incorrecta")
                                print(self.History_move)
                                input("Presione enter para continuar")
                                return 0
                        except:
                            pass
                        os.system("cls")
                        self.History_move[0].pop()
                        self.History_move[1].pop()
                        print("Se ingreso una coordenada incorrecta")
                        print(self.History_move)
                        input("Presione enter para continuar")
                        return 0
                else:
                    os.system("cls")
                    print("Se ingreso una coordenada incorrecta")
                    print(self.History_move)
                    input("Presione enter para continuar")
                    return 0
                
            case 2:
                if coordenada_direccion[0] >= 0 and coordenada_direccion[1] >=0:
                    os.system("cls")
                    x = len(self.History_move[0])
                    y = len(self.History_move[1])
                    self.board[coordenada_direccion[1]][coordenada_direccion[0]] = "B"
                    print(super().Print_User_Board())
                    print("Se ingreso una coordenada correcta")
                    input("Presione enter para continuar")
                    return 1
                else:
                    print("No se puede colocar el barco aqui")
                    input("Presione enter para continuar")
                    os.system("cls")
                    return 0
                
                
            
            
                
    
    
        
# table = [["1"]*9]*9
# print_table = Print_Table(table)
# print(print_table)
# for i in range(9):
#     print("\n")
#     for j in range(9):
#         print(table[i][j], end=" ")


player1 = user()
print(player1)
