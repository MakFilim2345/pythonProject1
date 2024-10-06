result = []

def divider(a, b):
    if a < b:
        raise ValueError("Число 'a' менше за 'b'")
    if b > 100:
        raise IndexError("Число 'b' більше за 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key, value in data.items():
    try:
        res = divider(int(key), value)
        result.append(res)
    except ZeroDivisionError as zde:
        print(f"Помилка: ділення на нуль при ключі {key} -> {zde}")
    except TypeError as te:
        print(f"Помилка типу даних: ключ {key} або значення {value} некоректні -> {te}")
    except ValueError as ve:
        print(f"Помилка значення: {ve}")
    except IndexError as ie:
        print(f"Помилка індексу: {ie}")
    except Exception as e:
        print(f"Невідома помилка: {e}")

print(result)
