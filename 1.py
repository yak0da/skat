from typing import Any, Type, get_type_hints

class Matchable:
    def __init__(self, *types: Type):
        self.types = types
    
    def __call__(self, cls: Type) -> Type:
        type_hints = get_type_hints(cls)
        matchable_fields = []
        for name, hint in type_hints.items():
            for target_type in self.types:
                try:
                    if hint == target_type:
                        matchable_fields.append(name)
                        break
                    elif isinstance(hint, type) and issubclass(hint, target_type):
                        matchable_fields.append(name)
                        break
                except TypeError:
                    continue
        def __getitem__(self, index):
            if isinstance(index, int):
                if 0 <= index < len(matchable_fields):
                    field_name = matchable_fields[index]
                    return getattr(self, field_name)
                raise IndexError(f"Index {index} out of range")
            raise TypeError(f"Expected int index, got {type(index)}")
        cls.__getitem__ = __getitem__
        cls.__match_args__ = tuple(matchable_fields)
        def __len__(self):
            return len(matchable_fields)
        cls.__len__ = __len__
        
        return cls

@Matchable(int, float)
class C:
    a: int
    s: str
    d: float

    def __init__(self, a, s, d):
        self.a, self.s, self.d = a, s, d

for A in (C(1, "2", 3), C(3, 3, 4), C(2, "Q", 3)):
    match A:
        case C(1):
            print("One")
        case C(_, 3):
            print("Three")
        case _:
            print("Other")
