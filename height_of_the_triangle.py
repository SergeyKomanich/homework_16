"""
При помощи вложенных циклов  и оператора IF нарисовать фигуры представленные ниже. Пользователь вводит,
с клавиатуры, высоту фигуры в символах.

  A         *
          *   *
        *       *
      *           *
    *               *
  *                   *
* * * * * * * * * * * * *

"""

column = int(input("Введите число (высоту фигуры): "))
indent = 2

for row in range(1, column + 1):
    for col in range(1, column * 2):
        if row + col == column + 1 or col - row == column - 1:
            print("*", end='')
        elif row == column and col != indent:
            print("*", end='')
            indent = indent + 2
        else:
            print(end=' ')
    print()

