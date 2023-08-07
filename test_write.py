text = "hello wolrd"

with open('log.txt', 'a', encoding='utf-8') as file:
    file.write(text + '\n')