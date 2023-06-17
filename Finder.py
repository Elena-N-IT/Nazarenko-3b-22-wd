"""
Написать программу, которая находит и удаляет дубликаты файлов в указанной директории и всех ее поддиректориях.
"""

import os
import hashlib

def calculate_hashes(directory):
    # Функция вычисляет хеш-суммы всех файлов и возвращает словарь, где ключи - хеш-суммы, а значения - списки файлов с ними
    
    hashes = {}
    
    # Обходим все файлы в директории:
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            
            # Вычисленияем хеш-сумму файла:
            with open(file_path, 'rb') as file:
                file_hash = hashlib.md5(file.read()).hexdigest()
            
            # Проверяем наличие хеш-суммы в словаре. Добавляем файл в список дубликатов, если найдено совпадение. В противном случае создаём новую запись:
            if file_hash in hashes:
                hashes[file_hash].append(file_path)
            else:
                hashes[file_hash] = [file_path]
    
    return hashes

def find_duplicates(hashes):
    # Функция находит дубликаты файлов из словаря хеш-сумм и возвращает словарь дубликатов

    duplicates = {}

    for hash_value, file_list in hashes.items():
        if len(file_list) > 1:
            duplicates[hash_value] = file_list
    
    return duplicates

def remove_duplicates(duplicates):
    # Функция удаляет дубликаты файлов из словаря

    for file_list in duplicates.values():
        for i in range(1, len(file_list)):
            os.remove(file_list[i])


directory = 'D:/Elena/TEMP'


hashes = calculate_hashes(directory)
duplicates = find_duplicates(hashes)
remove_duplicates(duplicates)