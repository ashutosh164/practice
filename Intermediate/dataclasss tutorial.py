# class Investor:
#
#     def __init__(self, name:str , age:int, cash: float):
#         self.name = name
#         self.age = age
#         self.cash = cash
#
#     def __repr__(self):
#         return f"name: {self.name}"
#
#     def __eq__(self, other):
#         return self.name == other.name
#
#     def __lt__(self, other):
#         return self.cash < other.cash
#
#
# i1 = Investor('ashu', 23, 5000)
# i2 = Investor('jilu', 22, 3000)
# i3 = Investor('silu', 20, 8000)
#
# i4 = Investor('ashu', 23, 5000)
#
# print(i1 == i4) # this is check in eq constructor
#
# print(i1 > i3)


# NOW WE GOING TO USE DATACLASS FOR BETTER CODE
from dataclasses import dataclass, field


@dataclass(order=True, unsafe_hash=True)
class Investor:
    # CUSTOM WAY TO SORTING DATA
    sort_index: float = field(init=False, repr=False)
    name: str
    age: int
    cash: float = field(repr=True, default=0.0)

    # CUSTOM WAY TO SORTING DATA
    def __post_init__(self):
        self.sort_index = self.cash

    # def __repr__(self):
    #     return self.name


l1 = Investor('ashu', 23, 4509)
l3 = Investor('danaa', 23, 500)
l2 = Investor('jilu', 32, 8990)
l4 = Investor('silu', 9, 2000)
l5 = Investor('lilu', 4, 900)
l6 = Investor('bulu', 60, 78000)

a = [l1,l2,l3,l4,l5,l6]
a.sort()
print(a)
print(l1 > l3)
print(hash(l1))
print(hash(l2))

