import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    end_signs = '.,!:;?'
    text_ref = text[start:]
    text = text[start:start+size]
    #print(text)
    last_info = [None, None]
    for ind in range(len(text)):
        symbol = text[ind]
        if ind == len(text) - 1:
            if ind < len(text_ref) - 1:
                if symbol in end_signs and text_ref[ind + 1] not in end_signs:
                    text = text[:ind+1]
                    len_text = len(text)
                    return (text, len_text)
                else:
                    text = text[:last_info[1]+1]
                    len_text = len(text)
                    return (text, len_text)
            else:
                text = text[:ind+1]
                len_text = len(text)
                return (text, len_text)
            
        if ind < len(text) - 1:
            if symbol in end_signs and text[ind+1] not in end_signs:
                last_info[0] = symbol
                last_info[1] = ind
            
# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(file=path, mode='r', encoding='utf-8') as file:
        text = file.read()
    start, page_number = 0, 1
    while start < len(text):
        page_text, page_size = _get_part_text(text, start, PAGE_SIZE)
        start += page_size
        book[page_number] = page_text.strip()
        page_number += 1


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))

#prepare_book('c:\\Users\\asus\\VS Code projects\\BookBot\\book\\book.txt')
#print(book)