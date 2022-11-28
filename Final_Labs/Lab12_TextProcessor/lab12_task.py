"""
Найти и вывести самое длиное предложение, содержащее ХОТЯ БЫ одно слово из одной буквы
"""

def find_sentence(text):
    true_sentences = sentence_splitter(text)
    longest_sentence_length = -1
    longest_sentence_index = None
    for i in range(len(true_sentences)):
        sentence = true_sentences[i]
        sentence_splitted = sentence.split()
        for index, word in enumerate(sentence_splitted):
            if word.isalpha() and len(word) == 1:
                if len(sentence_splitted) > longest_sentence_length:
                    longest_sentence_length = len(sentence_splitted)
                    longest_sentence_index = i
    if longest_sentence_index is None:
        print("(!) В вашем тексте отстутствуют предложения со словами, состоящими только из одной буквы.")
    else:
        print(f">> Самое длинное предложение, содержащее хотя бы одно слово из одной буквы, найдено:\n{true_sentences[longest_sentence_index]}")


def sentence_splitter(text):
    possible_endings = "?.!"
    sentences = [[]]
    k = 0
    for i in range(len(text)):
        line = text[i]
        j = 0
        while j < len(line):
            #print(f"now i scan {line[j]}")
            if line[j] in possible_endings:
                sentences[k].append(line[j])
                sentences.append([])
                k += 1
                j += 1
            sentences[k].append(line[j])
            j += 1
    for i in range(len(sentences)):
        sentences[i] = "".join(sentences[i]).split()
        sentences[i] = " ".join(sentences[i])
    #print(sentences)
    return sentences


text = [
        "Я убежден, что в 2 * 6 / 4     Петербурге много народу, ",
        "        ходя, говорят сами с собой. Это город полусумасшедших. Если б у нас были науки, то медики, ",
        "юристы и философы. могли бы сделать над Петербургом 2 / 2 драгоценнейшие 34 * 34 / 34 ",
        "исследования, каждый по своей ",
        "специальности. Редко где найдется столько мрачных, резких и странных влияний на душу человека, как ",
        "в Санкт-Петербурге. Чего стоят одни климатические влияния. "
    ]
text_01 = [
    "Удивительно. Данный текст не содержит ни ",
    "одного предложения, которое ",
    "бы содержало слово, состоящее только ",
    "из одной буквы. "
]

find_sentence(text)

