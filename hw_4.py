from pathlib import Path


def total_salary(path: str) -> tuple:
    total_salary = 0
    count_employees = 0

    try:
        current_file_path = Path(path)

        with open(current_file_path, 'r', encoding='utf-8') as c_f:
            for line in c_f:
                name, salary = line.strip().split(',')
                total_salary += int(salary)
                count_employees += 1

        average_salary = total_salary / count_employees
        return (int(total_salary), float(average_salary))

    except FileNotFoundError:
        print(f"Файл {current_file_path} не найден.")
        return None
    except ValueError:
        print("Ошибка в формате файла.")
        return None
    except Exception as e:
        print(e)


print(type(total_salary('fff.txt')))


def get_cats_info(path: str) -> dict:
    cats_list = []

    try:
        current_file_path = Path(path)

        with open(current_file_path, 'r', encoding='utf-8') as c_f:
            for line in c_f:
                id, name, age = line.strip().split(',')
                cats_list.append({'id': id, 'name': name, 'age': int(age)})

        return cats_list

    except FileNotFoundError:
        print(f"Файл {current_file_path} не найден.")
        return None
    except ValueError:
        print("Ошибка в формате файла.")
        return None
    except Exception as e:
        print(e)


print(get_cats_info('cats.txt'))
