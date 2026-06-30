import operator
from pyscript import document

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

    def calculate(self, a, op, b):
        if op in self.actions:
            return self.actions[op](a, b)
        return "오류"

calc = UltimateCalculator()

def run_calculation(event):
    input1 = document.querySelector("#num1").value
    input2 = document.querySelector("#num2").value
    op = document.querySelector("#operator").value
    
    if not input1 or not input2:
        document.querySelector("#output").innerText = "숫자를 입력하세요."
        return
        
    a = float(input1)
    b = float(input2)
    
    res = calc.calculate(a, op, b)
    
    if isinstance(res, float) and res.is_integer():
        res = int(res)
        
    document.querySelector("#output").innerText = str(res)
