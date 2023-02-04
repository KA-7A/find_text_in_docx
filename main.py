import os, re, docx

def doc_to_string(filename:str) -> str:
    doc = docx.Document(filename)

    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"

    return text


def find_all_files_in_dir(directory_in:str, phrase:str) -> list:
    docx_files = []
    for root, dirs, files in os.walk(directory_in):
        for file in files:
            if re.search(".*docx$", str(root + "/" + file)) and re.search(phrase, doc_to_string(str(root + "/" + file)), re.I):
                docx_files.append(root + "/" + file)
    return docx_files

def main():
    directory = input("Введите путь до директории, либо .\\, если main.py лежит в нужном месте -> ")
    substring = input("Введите слово/словосочетание, которое нужно найти в файлах -> ")
    files = find_all_files_in_dir(directory, substring)
    text = ""
    for file in files:
        text += file + "\n"
    print(text)

if __name__=="__main__":
    main()