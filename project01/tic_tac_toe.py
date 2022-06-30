print("Крестики-нолики для двух игроков")

board = list(range(1,10))  # создаем поле 3*3

def draw_board(board): #отрисовываем поле и заполняем его клетки цифрами
   for i in range(3):
      print("-" * 3, "+", "-", "+", "-" * 3)
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
   print("-"* 3, "+", "-", "+", "-"* 3 )

def input_XO(player_turn):  #функция ввода игроком Х или 0
    valid = False
    while not valid: #предлагаем игроку выбрать, в какую ячейку поставть Х или 0
        player_answer = input("Куда поставим " + player_turn + "? Выберите число от 1 до 9. Пусть будет  ")
        try:
            player_answer = int(player_answer)
        except:
            print("Неее. Вы уверены, что ввели число?")  #на случай, если игрок ввел не число
            continue
        if player_answer >= 1 and player_answer <= 9: #вводим ограничения, на случай, когда выбранная клетка уже занята
            if (str(board[player_answer - 1]) not in "XO"):  #либо игрок ввел не корректное значение (число >9 или не число)
                board[player_answer - 1] = player_turn
                valid = True
            else:
                print("А всё! Клетка уже занята")
        else:
            print("Не то. Введите число от 1 до 9.")

def check_win(board): #вводим функцию, которая будет проверять условия, при которых игрок победит
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8),
                 (0, 4, 8), (2, 4, 6)) #координаты выиграша
    for each in win_coord: #проверка условий выиграша
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board): #собираем все функции воедино в основную
    counter = 0
    win = False
    while not win: #включаем счетчик очков
        draw_board(board)
        if counter % 2 == 0:
            input_XO("X")
        else:
            input_XO("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board) #вводим временную переменную для Х и О
            if tmp:
                print(tmp, "выиграл! You are the champions...")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break

main(board)






