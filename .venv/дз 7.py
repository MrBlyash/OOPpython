import re
def calculator_decorator(func):
    def wrapper(expression):
        try:
            if not re.match(r'^[0-9+\-*/(). ]+$', expression):
                raise ValueError("незрозумілі символи")
            result = func(expression)
            return result
        except ZeroDivisionError:
            return "Помилка: Ділення на нуль"
        except SyntaxError:
            return "Помилка: Синтаксична помилка"
        except Exception as e:
            return f"Помилка: {e}"
    return wrapper
@calculator_decorator
def calculate(expression):
    return eval(expression)

print(calculate("2+2"))
