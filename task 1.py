import os
import shutil
import argparse
import sys

def copy_files(src, dest):
    try:
        # Створення директорії призначення, якщо вона не існує
        if not os.path.exists(dest):
            os.makedirs(dest)
        
        # Проходження по всіх файлах і піддиректоріях у вихідній директорії
        for item in os.listdir(src):
            path = os.path.join(src, item)
            if os.path.isdir(path):
                # Рекурсивний виклик функції, якщо елемент є директорією
                copy_files(path, dest)
            else:
                # Копіювання файлу в нову піддиректорію, базовану на розширенні файлу
                ext = os.path.splitext(item)[1][1:]  # Вилучення розширення файла без точки
                if ext == '':
                    ext = 'no_extension'
                ext_dir = os.path.join(dest, ext)
                if not os.path.exists(ext_dir):
                    os.makedirs(ext_dir)
                shutil.copy(path, ext_dir)
    except Exception as e:
        print(f"Помилка: {e}", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description='Копіювання файлів за розширеннями')
    parser.add_argument('src_dir', type=str, help='Шлях до вихідної директорії')
    parser.add_argument('dest_dir', type=str, nargs='?', default='dist', help='Шлях до директорії призначення (за замовчуванням dist)')
    args = parser.parse_args()

    copy_files(args.src_dir, args.dest_dir)

if __name__ == '__main__':
    main()
