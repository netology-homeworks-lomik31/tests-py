def main(mentors):
    # добавьте в список всех преподавателей со всех курсов
    all_list = sum(mentors, [])

    # сделайте список all_names_list, состоящий только из имен, и заполните его
    all_names_list = map(lambda i: i.split(" ")[0], all_list)
        
    # сделайте так, чтобы остались только уникальные имена (без повторений) - допишите ниже ваш код
    unique_names = set(all_names_list)

    # теперь нужно отсортировать имена в алфавитном порядке. подсказка: используйте sorted() для списка
    # допишите код ниже
    all_names_sorted = sorted(list(unique_names))
    # допишите конструкцию вывода результата. можете использовать string.join()
    # результат будет в all_names_sorted
    return ", ".join(all_names_sorted)