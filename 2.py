class Fix:
    def __init__(self, n):
        if not 1 <= n <= 16:
            raise ValueError("n должно быть в диапазоне от 1 до 16")
        self.n = n
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            # Округляем позиционные аргументы
            new_args = []
            for arg in args:
                if isinstance(arg, float):
                    new_args.append(round(arg, self.n))
                else:
                    new_args.append(arg)
            
            # Округляем именованные аргументы
            new_kwargs = {}
            for key, value in kwargs.items():
                if isinstance(value, float):
                    new_kwargs[key] = round(value, self.n)
                else:
                    new_kwargs[key] = value
            
            # Вызываем функцию с округленными аргументами
            result = func(*new_args, **new_kwargs)
            
            # Округляем возвращаемое значение
            if isinstance(result, float):
                return round(result, self.n)
            return result
        
        # Копируем основные атрибуты функции, используя getattr с значением по умолчанию
        wrapper.__name__ = getattr(func, '__name__', 'wrapper')
        wrapper.__doc__ = getattr(func, '__doc__', None)
        wrapper.__module__ = getattr(func, '__module__', '__main__')
        
        return wrapper


# Пример использования
@Fix(4)
def aver(*args, sign=1):
    return sum(args)*sign

# Тест
print(aver(2.45675901, 3.22656321, 3.432654345, 4.075463224, sign=-1))  # -13.1916
