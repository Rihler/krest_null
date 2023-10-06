class Field(object):
    def __init__(self):
        self.field = [["|A1|", "|A2|", "|A3|"], ["|B1|", "|B2|", "|B3|"], ["|C1|", "|C2|", "|C3|"]]
        self.cords = {
            "A1": [0, 0],
            "A2": [0, 1],
            "A3": [0, 2],
            "B1": [1, 0],
            "B2": [1, 1],
            "B3": [1, 2],
            "C1": [2, 0],
            "C2": [2, 1],
            "C3": [2, 2],
        }
        self.sym ={
            "A1": 0,
            "A2": 0,
            "A3": 0,
            "B1": 0,
            "B2": 0,
            "B3": 0,
            "C1": 0,
            "C2": 0,
            "C3": 0,
        }

    def print_field(self):
        print('-' * 14)
        for i in range(3):
            for j in range(3):
                print(self.field[i][j], end=" ")
            print("\n" + '-' * 14)

def change_sym(name):
    print(f"Выбор символа для {name}")
    ch = ["1", "2"]
    syms = input("1. X\n2. O\n")
    while syms not in ch:
        print("Данного выбора нет, выберите номер символа из предлагаемого списка")
        syms = input("1. X\n2. O\n")
    return "X" if syms == "1" else "O"
