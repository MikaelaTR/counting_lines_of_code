import os

def count_lines(directory):
    total_lines = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            try:
                with open(os.path.join(root, file), 'r') as f:
                    for line in f:
                        if line.strip(): 
                            # Считаем только непустые строки
                            total_lines += 1
            except: 
                # Не удалось открыть файл как текстовый файл
                print(f'Could not open {os.path.join(root, file)}')
    print(f"ИТОГО строк кода - {total_lines}")
    value = total_lines/1000/24
    print(f"Дней работы - {value}")
    return total_lines

count_lines('path')