"""
Лабораторная работа №12 "Текстовый процессор"
Беляев Никита ИУ7-11б

>> Задача:
С помощью консольного меню реализовать возможности обработки текста (Массива строк)

>> Индивидумальное задание по варианту:
1) Вычисление операций умножения и деления внутри текста
2) Вывести на экран, а затем удалить из исходного текста предложение, содержащее слово с max кол-вом согласных
"""

import CheckValues as check


def menu():
    """ I show User's menu """

    MENU_WIDTH = 75
    print(
        "\n"
        "|" + "-" * MENU_WIDTH + "|" + '\n'
        "|" + "\033[1m" + f"{'Работа с текстом':^{MENU_WIDTH}}" + "\033[0m" + "|" + "\n"
        "|" + "-" * MENU_WIDTH + "|" + '\n'
        "|" + f"{'    1. Выровнять текст по левому краю.':<{MENU_WIDTH}}" + "|" + "\n"
        "|" + f"{'    2. Выровнять текст по правому краю.':<{MENU_WIDTH}}" + "|" + "\n"
        "|" + f"{'    3. Выровнять текст по центру.':<{MENU_WIDTH}}" + "|" + "\n"
        "|" + f"{'    4. Удалить все вхождения определенного слова.':<{MENU_WIDTH}}" + "|" + "\n"
        "|" + f"{'    5. Замена определенного слова во всем тексте.':<{MENU_WIDTH}}" + "|" + "\n"
        "|" + f"{'    6. Вычислить арифметические операции (/ / *) внутри текста.':<{MENU_WIDTH}}" + "|" + "\n"
        "|" + f"{'    7. Вывести и удалить из текста предложение,':<{MENU_WIDTH}}" + "|" + "\n"
        "|" + f"{'       содержащее слово с наибольшим кол-вом согласных.':<{MENU_WIDTH}}" + "|" + "\n"
        "|" + "-" * MENU_WIDTH + "|" + '\n'
        "|" + f"{'    0. Завершить программу.':<{MENU_WIDTH}}" + "|" + "\n"
        "|" + "-" * MENU_WIDTH + "|" + "\n"
    )
    users_choice = check.get_exact_integer("Выберите действие с текстом: ", 0, 7)
    print("\n")

    return users_choice


def show_text(text):
    print("Ваш текст:\n")
   # print("-" * 150)
    for line in text:
        print(line)
   # print("-" * 150)


# We store last alignment function in "last_align_code"
# in order to call this function again after we edit the text.

# Since it's forbidden to use global variables, we're always return the value of "power_on"
# If it's possible, that after func's exectution our text will be empty, we'll show the following message
# and turn the program off.

def align_left(text):
    for i in range(len(text)):
        new_line = " ".join(text[i].split())
        text[i] = new_line + " "
    last_align_code = 1
    return text, last_align_code, True


def align_right(text):
    text, align, power_on = align_left(text)
    longest_line_length = max(map(len, text))
    for i in range(len(text)):
        text[i] = (longest_line_length - len(text[i])) * " " + text[i] + " "
    last_align_code = 2
    return text, last_align_code, True


def align_by_width(text):
    text, align, power_on = align_left(text)

    # We store length of i line and amount of spaces in it in the following lists
    words = [0] * len(text)
    spaces = [0] * len(text)

    for i in range(len(text)):
        words[i] = len(text[i])
        spaces[i] = text[i].count(" ")
    longest_line_length = max(map(len, text))

    for i in range(len(text)):
        line = list(text[i])
        # We don't add any additional spaces to the longest line
        if len(line) == longest_line_length:
            continue

        # Check if there are any spaces in line at all
        if spaces[i] == 0:
            amount_of_spaces = 0
            remainders = 0
        else:
            # reminders == остаточные пробелы
            amount_of_spaces = (max(words) - words[i]) // spaces[i]
            remainders = (max(words) - words[i]) % spaces[i]

        more_reminders_to_add = 0
        for j in range(len(line)):
            if line[j] == ' ':
                line[j] += ' ' * amount_of_spaces
                if remainders > more_reminders_to_add:
                    line[j] += ' '
                    more_reminders_to_add += 1

        text[i] = "".join(line)
        text[i] = text[i].replace(" ", "  ", amount_of_spaces)
    last_align_code = 3
    return text, last_align_code, True


# In following functions for deleting and replacing the word
# we use support-function "line_splitter":
# String in our text -> line_splitter function -> list of separated words in our string
# That method prevents deleting and replacing parts of some word.
def delete_word(text):
    word_raw = check.get_single_word("Введите слово, которое вы хотите удалить: ")
    is_ignoring_register = check.get_exact_strings("Игнорировать регистр (да/нет)? - ", "да", "нет")

    if is_ignoring_register == "да":
        word = word_raw.lower()
        for i in range(len(text)):
            line = text[i]

            # After calling "line_splitter" function we have
            # a list of separated words in our current line
            words = line_splitter(line)
            for text_word in words:
                if word == text_word.lower():
                    new_line = text[i].replace(text_word, "")
                    text[i] = new_line
    else:
        word = word_raw
        for i in range(len(text)):
            line = text[i]
            words = line_splitter(line)
            for text_word in words:
                if word == text_word:
                    new_line = text[i].replace(text_word, "")
                    text[i] = new_line
    if align is not None:
        function[align](text)

    text, power_on = is_empty(text)
    return text, align, power_on


def replace_word(text):
    word_raw = check.get_single_word("Введите слово, которое вы хотите заменить: ")
    new_word = check.get_single_word("Введите слово на замену: ")
    is_ignoring_register = check.get_exact_strings("Игнорировать регистр (да/нет)? - ", "да", "нет")

    if is_ignoring_register == "да":
        word = word_raw.lower()
        for i in range(len(text)):
            line = text[i]
            words = line_splitter(line)
            #print(">> words:", words)
            for j in range(len(words)):
                text_word = words[j]
                if word == text_word.lower():
                    words[j] = new_word
                    new_line = " ".join(words)
                    text[i] = new_line
    else:
        word = word_raw
        for i in range(len(text)):
            line = text[i]
            words = line_splitter(line)
            for j in range(len(words)):
                text_word = words[j]
                if word == text_word:
                    words[j] = new_word
                    new_line = " ".join(words)
                    text[i] = new_line
    if align is not None:
        function[align](text)
    return text, align, True


# This function works with expressions where numbers are separated from signs with at least one space
def catch_math_expression(text):
    signs = ["*", "/"]

    for i in range(len(text)):
        line = text[i]
        words = line_splitter(line)

        j = 0
        while j < len(words) - 2:
            # At this point we check if current and "one-after" words are actually numbers.
            # Is so, we check the "word" in-between them.
            # If it's a sign -> we count the expression and replace it's terms with the result.
            #
            # Then, in order to check whether there are more then one operation,
            # we're dropping our index "j" back to zero and starting to scan our line again.

            try:
                term_first = float(words[j])
                term_second = float(words[j + 2])
            except ValueError:
                j += 1
                continue

            if words[j + 1] not in signs:
                j += 1
                continue

            elif words[j + 1] == "*":
                result = str(int(float(words[j]) * float(words[j + 2])))
                new_line = text[i].replace(words[j], result, 1).replace(words[j + 1], "", 1).replace(words[j + 2], "",
                                                                                                     1)
                text[i] = new_line
                words[j] = result
                words.pop(j + 1)
                words.pop(j + 1)
                j = 0

            elif words[j + 1] == "/":
                result = str(int(float(words[j]) / float(words[j + 2])))
                new_line = text[i].replace(words[j], result, 1).replace(words[j + 1], "", 1).replace(words[j + 2], "",
                                                                                                     1)
                text[i] = new_line
                words[j] = result
                words.pop(j + 1)
                words.pop(j + 1)
                j = 0

    if align is not None:
        function[align](text)
    return text, align, True


def find_sentence(text):
    vowels = "уеыаоэяиюeyuioa"
    good_word = None
    line_index = None
    max_amount = 0

    # In the following code section we find the needed word (good_word)
    # and index of the line where it's settled (line_index).
    for i in range(len(text)):
        line = text[i]
        words = line.split()
        for j in range(len(words)):
            # print(f"now i scan {words[j]}")
            word = words[j]
            counter = 0

            for k in range(len(word)):
                letter = word[k]
                if letter.lower() not in vowels:
                    counter += 1
            if counter > max_amount:
                max_amount = counter
                good_word = word
                line_index = i

    # In the following code section we use support-function "sentence_splitter":
    # text (List of strings) --> sentence_splitter --> list of strings, where every element is
    # the right sentence from our text.
    #
    # Then, we find in which sentence our "good word" is settled. Let's call it "good sentence"
    sentences = sentence_splitter(text)
    for sentence in sentences:
        if good_word in sentence:
            good_sentence = sentence
            print(">> Искомое предложение найдено:", good_sentence, "\n")
            break

    # We split "good sentence" and COUNT the amount of words we need to delete BEFORE "good word" and AFTER it
    sentence_splitted = good_sentence.split()

    # Amount of words we need to delete in both sides
    count_previous_del = sentence_splitted.index(good_word)
    count_afterwards_del = len(sentence_splitted) - count_previous_del

    # Deleting previous elements
    line_to_check = line_index
    line_splitted = text[line_to_check].split()
    current_element = line_splitted.index(good_word)

    while count_previous_del > 0:
        while current_element > 0:
            line_splitted[current_element - 1] = " "
            current_element -= 1
            count_previous_del -= 1
            if count_previous_del == 0:
                break
        text[line_to_check] = " ".join(line_splitted)
        line_to_check -= 1
        line_splitted = text[line_to_check].split()
        current_element = len(line_splitted)

    # Deleting afterward elements
    line_to_check = line_index
    line_splitted = text[line_to_check].split()
    current_element = line_splitted.index(good_word)

    while count_afterwards_del > 0:
        while current_element < len(line_splitted):
            line_splitted[current_element] = " "
            current_element += 1
            count_afterwards_del -= 1
            if count_afterwards_del == 0:
                break
        text[line_to_check] = " ".join(line_splitted)
        line_to_check += 1
        if line_to_check > len(text) - 1:
            break
        line_splitted = text[line_to_check].split()
        current_element = 0

    if align is not None:
        function[align](text)

    text, power_on = is_empty(text)
    return text, align, power_on


def is_empty(text):
    """ I check if our text is empty after executing some function"""
    flag = False
    for i in range(len(text)):
        line = text[i]
        # print(f"line: > {line}")
        for j in range(len(line)):
            if line[j] != " ":
                flag = True
                break
    if flag:
        return text, True
    else:
        text.insert(0, "(!) Вы удалили весь текст.")
        return text, False


def sentence_splitter(text):
    """ I return the list with true sentences of given text """
    sentences = [[]]
    k = 0
    for i in range(len(text)):
        line = text[i]
        j = 0
        while j < len(line):
            if line[j] == ".":
                sentences.append([])
                k += 1
                j += 1
            sentences[k].append(line[j])
            j += 1
    for i in range(len(sentences)):
        sentences[i] = "".join(sentences[i]) + "."
    # print(sentences)
    return sentences


def line_splitter(line):
    """ I return the list with words which line contains without any separators """
    words = []
    possible_beginnings = ["(", "'", "{", "[", "\"", " ", "."]
    possible_endings = [" ", ".", "!", "?", ":", ";", ")", ",", "]", "}", "'", "\""]
    j = 0
    while j < len(line):
        scan = 0
        if line[j] not in possible_beginnings:
            start = j
            scan = j
            while line[scan] not in possible_endings and scan < len(line) - 1:
                j += 1
                scan += 1
            word_to_compare = line[start:scan]
            words.append(word_to_compare)
        j += 1
    return words


# Main
power_on = True

text = [
        "Я убежден, что в 2 * 6 / 4     Петербурге много народу, ",
        "        ходя, говорят сами с собой. Это город полусумасшедших. Если б у нас были науки, то медики, ",
        "юристы и философы могли бы сделать над Петербургом 2 / 2 драгоценнейшие 34 * 34 / 34 ",
        "исследования, каждый по своей ",
        "специальности. Редко где найдется столько мрачных, резких и странных влияний на душу человека, как ",
        "в Санкт-Петербурге. Чего стоят одни климатические влияния!"
    ]

show_text(text)
align = None

while power_on:
    users_choice = menu()

    if users_choice == 0:
        print("Программа завершена.")
        show_text(text)
        power_on = False
        break

    function = {
        1: align_left,
        2: align_right,
        3: align_by_width,
        4: delete_word,
        5: replace_word,
        6: catch_math_expression,
        7: find_sentence,
    }
    text, align, power_on = function[users_choice](text)
    show_text(text)
