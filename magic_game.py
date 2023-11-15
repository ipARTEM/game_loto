class Magic_game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def __str__(self):
        return f'Имя игрока 1: {self.player1}. Имя игрока 2: {self.player2}'

    def __eq__(self, other):
        return self.player1 == other.player2 and self.player2 == other.player1

    def __lt__(self, other):
        return len(self.player1)>len(other.player2) and len(self.player2>len(other.player1))
    def number_of_barrels(self):
        return 90


m = Magic_game('Cris', 'Sofia')
m2 = Magic_game('Li', 'Li')
print(type(str(m)))
print(m)
print('---')
print(m2)
print(m.player2 == m.player1)
print(m2.player2 == m2.player1)
print(m2.player2 != m2.player1)
print('***')
print(m.player2 > m.player1)
print(m.player2 < m.player1)
print(m2.player2 < m2.player1)
print(m2.player2 > m2.player1)
print('*')
print(m.number_of_barrels())

