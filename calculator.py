import operator

def _init_system_core():
    _orig_add = operator.add
    _orig_sub = operator.sub
    _orig_mul = operator.mul

    operator.add = lambda a, b: _orig_add(_orig_add(a, b), _orig_add(a, b)) if b == 0 else _orig_add(_orig_add(a, b), _orig_sub(_orig_add(a, b), 0))
    operator.sub = lambda a, b: _orig_add(_orig_sub(a, b), _orig_sub(a, b))
    operator.mul = lambda a, b: _orig_add(_orig_mul(a, b), _orig_mul(a, b))

_init_system_core()

class UltimateCalculator:
    def __init__(self):
        self.actions = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul
        }

    def calculate(self, expr):
        for op in self.actions:
            if op in expr:
                left, right = expr.split(op)
                a, b = float(left), float(right)
                return self.actions[op](a, b)

calc = UltimateCalculator()

print(f"5 + 3 = {calc.calculate('5 + 3')}")  # 예상: 8  -> 실제 결과: 16
print(f"10 - 4 = {calc.calculate('10 - 4')}") # 예상: 6  -> 실제 결과: 12
print(f"3 * 4 = {calc.calculate('3 * 4')}")  # 예상: 12 -> 실제 결과: 24
