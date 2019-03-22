import re

fileName = input("Введите имя файла:")
headers = input("Файл содержит заголовки? (д/н)").lower()
delim = input("Используемый разделитель: ")
result = []
parser = r'(?:\{0}|\n|^)("(?:(?:"")*[^"]*)*"|[^"\{0}\n]*|(?:\n|$))'.format(delim)


def parse_string(string):
    list_string = re.findall(parser, string)
    return list(map(lambda stroka: stroka[1:-1].replace('""', '"') if stroka.count('"') else stroka, list_string))


with open(fileName, 'r') as f:
    tmpString = ''
    firstLine = True
    header = []
    for line in f.readlines():
        tmpString += line
        if not tmpString.count('"') % 2:
            if headers == 'д' and firstLine:
                header = parse_string(tmpString.rstrip('\n'))
                firstLine = False
            else:
                listLine = parse_string(tmpString.rstrip('\n'))
                if headers == 'д':
                    result.append(dict(zip(header, listLine)))
                else:
                    result.append(listLine)
            tmpString = ''
print(result)

