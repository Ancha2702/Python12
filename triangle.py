"""
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""
a = float(input('Введите сторону а треугольника abc: '))
b = float(input('Введите сторону b треугольника abc: '))
c = float(input('Введите сторону c треугольника abc: '))
if (a + b) > c and (a + c) > b and (b + c) > a:
    print("Это точно треугольник")
    if (a == b) and (b == c):
        print("и он равносторонний треугольник")
    if (a == b) or (b == c) or (a == c):
        print("и он равнобедренный треугольник")
    else: print("и он разносторонний треугольник")

else: print("Это не треугольник")
