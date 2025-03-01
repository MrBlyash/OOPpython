result = []

def divider(a, b):
    if a < b:
        raise ValueError("a повинно бути ≥ b")
    if b > 100:
        raise IndexError("b не повинно > 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key, value in data.items():
    try:
        key = int(key)
        res = divider(key, value)
        result.append(res)
    except (ValueError, TypeError, ZeroDivisionError, IndexError) as e:
        print(f"Помилка: {e}")

print("Результат:", result)
