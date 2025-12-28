def sizer(cls):
    """
    Декоратор класса, добавляющий свойство size.
    size возвращает len(obj), если объект имеет длину,
    иначе abs(obj), если определен модуль,
    иначе 0.
    """
    
    class SizedClass(cls):
        def __init__(self, *args, **kwargs):
            self._size = None  # Собственное значение size
            super().__init__(*args, **kwargs)
        
        @property
        def size(self):
            # Если установлено собственное значение
            if self._size is not None:
                return self._size
            
            # Пытаемся вернуть длину
            try:
                return len(self)
            except (TypeError, AttributeError):
                pass
            
            # Пытаемся вернуть модуль
            try:
                return abs(self)
            except (TypeError, AttributeError):
                pass
            
            # По умолчанию 0
            return 0
        
        @size.setter
        def size(self, value):
            self._size = value
        
        @size.deleter
        def size(self):
            self._size = None
    
    # Сохраняем оригинальное имя класса
    SizedClass.__name__ = cls.__name__
    
    return SizedClass


# Тестовый код
if __name__ == "__main__":
    @sizer
    class S(list):
        pass

    @sizer
    class N(complex):
        pass

    @sizer
    class E(Exception):
        pass

    for obj in S("QWER"), N(3+4j), E("Exceptions know no lengths!"):
        print(obj, obj.size)
    
    p = S(range(10, 15))
    print(p.size)
    p.size = p.pop()
    print(p.size)
    del p.size
    print(p.size)
