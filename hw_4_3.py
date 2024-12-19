import os
import sys
from pathlib import Path
from colorama import Fore, Style, init

init()


def print_directory_structure(path: str):
    try:
        for root, dirs, files in os.walk(path):
            print(f"{Fore.BLUE}{root}{Style.RESET_ALL}")
            for dir in dirs:
                print(f"  {Fore.GREEN}{dir}{Style.RESET_ALL}")
            for file in files:
                print(f"  {Fore.YELLOW}{file}{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"Директория {path} не найдена.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Неправельное количество аргументов. Введите путь к директории.")
        sys.exit(1)

    directory_path = sys.argv[1]
    print_directory_structure(directory_path)
