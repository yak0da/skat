from functools import wraps


def Fix(n: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # проверить n
            if not (1 <= n <= 16):
                raise ValueError("значение n не в диапазоне от 1 до 16")

            # обработать параметры функции
            param_poz = []
            for el in args:
                if isinstance(el, float):
                    param_poz.append(round(el, n))
                else:
                    param_poz.append(el)

            param_imen = {}
            for key, value in kwargs.items():
                if isinstance(value, float):
                    param_imen[key] = round(value, n)
                else:
                    param_imen[key] = value

            # вызвать функцию
            res = func(*param_poz, **param_imen)
            
            # обработать результат функции
            if isinstance(res, float):
                res = round(res, n)
            return res
        return wrapper
    return decorator

@Fix(4)
def aver(*args, sign=1):
    return sum(args)*sign

print(aver(2.45675901, 3.22656321, 3.432654345, 4.075463224, sign=-1))