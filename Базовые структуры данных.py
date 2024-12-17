grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_ = sorted(list(students))      # привели множество students к типу список и к алфавитному порядку

average_score_1 = sum(grades[0]) / len(grades[0])      # вычислим средний бал для 1-го ученика
average_score_2 = sum(grades[1]) / len(grades[1])
average_score_3 = sum(grades[2]) / len(grades[2])
average_score_4 = sum(grades[3]) / len(grades[3])
average_score_5 = sum(grades[4]) / len(grades[4])
average_score = [average_score_1, average_score_2, average_score_3, average_score_4, average_score_5]  # создали список с общими средними оценками

dictionary = dict(zip(students_, average_score))
print(dictionary)