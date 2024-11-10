import time

#Приветствие и сбор информации о игроках
print("Добро пожаловать в игру <<Крестики-нолики>>")
print()
player_one = input("Введите имя первого игрока: ")
player_two = input("Введите имя второго игрока: ")

#Символы игроков присваиваются автоматически
players = {player_one: "X", player_two: "0"}
print()
print(f"Привет {player_one}, \nТы ходишь крестиками (X)!")
print("--------------------")
print(f"Привет {player_two}, \nТы ходишь ноликами (0)!")

#Создаем игровое поле в глобальной области видимости
T = [["-" for _ in range(3)] for _ in range(3)]

#Декоратор, который будет создавать поле
def create_field(func):
    def wrapper(*args, **kwargs):
        print()
        print("  0 1 2")
        for i, row in enumerate(T):
            print(i, " ".join(row))
        print()
        return func(*args, **kwargs)
    return wrapper

#Проверка победителя
def check_winner():
    # Проверка строк
    for x in T:
        if x[0] == x[1] == x[2] != "-":
            # Возвращаем имя игрока
            return [player for player, symbol in players.items() if symbol == x[0]]

    # Проверка столбцов
    for y in range(3):
        if T[0][y] == T[1][y] == T[2][y] != "-":
            return [player for player, symbol in players.items() if symbol == T[0][y]]

    # Проверка диагоналей
    if T[0][0] == T[1][1] == T[2][2] != "-":
        return [player for player, symbol in players.items() if symbol == T[0][0]]
    if T[0][2] == T[1][1] == T[2][0] != "-":
        return [player for player, symbol in players.items() if symbol == T[0][2]]

    return None

#Передвижение игрока по полю
@create_field
def player_turn(name: str, symbol: str):

    while True:
        x, y = map(int, input(f"{name} делай свой ход (Y и X): ").split())
        if x not in range(0, 3) or y not in range(0, 3):
            print("Ты вышел за рамки поля. Рамки поля от 0 до 2")
            continue
        if T[x][y] != "-":
            print(f"Игрок {name} уже занял/-а это поле. Выбери другое!")
            continue
        T[x][y] = symbol
        break

def start_game():
    current_player = player_one
    current_symbol = players[current_player]

    moves = 0

    while True:
        player_turn(current_player, current_symbol)  # Игрок делает ход

        # Проверяем на победителя
        winner = check_winner()
        if winner:
            print(f"Игрок {winner} победил!")
            break

        moves += 1
        if moves == 9:
            print("Ничья!")
            break

        # Меняем игрока
        current_player = player_two if current_player == player_one else player_one
        current_symbol = players[current_player]


# Запуск игры
start_game()