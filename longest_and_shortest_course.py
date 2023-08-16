def main(courses, mentors, durations):
    # в этот список будут добавляться словари-курсы
    courses_list = []
    # допишите код, который генерирует словарь-курс с тремя ключами: "title", "mentors", "duration"
    for i, j, k in zip(courses, mentors, durations):
        course_dict = {"title": i, "mentors": j, "duration": k}
        courses_list.append(course_dict)
    max_l = []
    min_l = []
    a = max(durations)
    b = min(durations)
    for i in courses_list:
        if (i["duration"] == a): max_l.append(i)
        elif (i["duration"] == b): min_l.append(i)
    max_s = ""
    min_s = ""
    for i in max_l:
        max_s += f"{i['title']}, "
    for i in min_l:
        min_s += f"{i['title']}, "
    # найдите самое маленькое и самое большое значение длительности курса
    # подсказка: используйте функции min и max для списка durations


    # как видите, в duration встречаются одинаковые длительности курса. допишите код, который это учитывает
    # подсказка 1: найдите индексы, по которым в списке durations встречается самое маленькое и самое большое значение
    # подсказка 2: не забудьте, что индекс можно удобно получить функцией enumerate

    # соберите все названия самых коротких и самых длинных курсов
    # так как курсов с одной длительностью может быть больше одного,
    # создайте список названий самых коротких (courses_min) и самых длинных (courses_max) курсов


    # допишите конструкцию вывода результата. можете использовать string.join()
    return {"shortest": min_s[:-2], "longest": max_s[:-2]}