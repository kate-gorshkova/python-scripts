class Store:
    def __init__(self):
        self.state = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.scheme_state = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

    def get_state(self, mode):
        state = self.state
        if mode == "scheme":
            state = self.scheme_state
        print("-------------")
        for row in state:
            print("|", row[0], "|", row[1], "|", row[2], "|")
            print("-------------")

    def set_state(self, any_number, value):
        for i in range(3):
            for j in range(3):
                if self.scheme_state[i][j] == any_number:
                    if self.state[i][j] == " ":
                        self.state[i][j] = value
                    else:
                        some_number = input("Введите номер поля ещё раз: ")
                        self.set_state(some_number, value)

    def check_win(self):
        one = self.state[0][0]
        two = self.state[0][1]
        three = self.state[0][2]
        four = self.state[1][0]
        five = self.state[1][1]
        six = self.state[1][2]
        seven = self.state[2][0]
        eight = self.state[2][1]
        nine = self.state[2][2]
        if one == two == three != " ":
            return one
        elif four == five == six != " ":
            return four
        elif seven == eight == nine != " ":
            return seven
        elif one == four == seven != " ":
            return one
        elif two == five == eight != " ":
            return two
        elif three == six == nine != " ":
            return three
        elif one == five == nine != " ":
            return one
        elif three == five == seven != " ":
            return three
        else:
            return False


app = Store()
app.get_state("scheme")

isWinner = False
for step in range(1, 10):
    if step % 2 != 0:
        player = "X"
    else:
        player = "O"
    print("Ход игрока:", player)

    number = input("Введите номер поля: ")
    app.set_state(number, player)
    app.get_state("state")

    winner = app.check_win()
    if winner:
        isWinner = True
        print("Победитель -", winner)
        break

if not isWinner:
    print("Ничья")
