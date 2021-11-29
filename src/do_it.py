INPUT_PATH = "../data/input/books.txt"
OUTPUT_PATH = "../data/output/result.txt"

with open(INPUT_PATH, 'r', encoding='utf-8') as inp:
    file_content = inp.read()

with open(OUTPUT_PATH, 'w', encoding='utf-8') as outp:
    outp.write("Вы заказывали эти книги:\n")
    outp.write(file_content)

print("Я работаю!\n")
print(file_content)