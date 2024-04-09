from Value import *
from CalculationPlus import *
from CalculationMultiplied import *
from CalculationMinus import *
from CalculationDivided import *

class ValueCalculation(Value):
    # コンストラクタ
    def __init__(self, value):

        #親クラスのコンストラクタを呼び出す
        super().__init__(value)

        self.value = value
        self.stack = value.split()

    # 別メソッドを追加
    def anotherText(self):
        text = "入力内容は {} です."
        return text.format(self.stack)

    def text(self):
        text = "入力内容は {} でした."
        return text.format(self.value)

    def excute(self):
        answer = []

        for item in self.stack:
            if item == "+":
                CalculationPlus.keisan(answer)
            elif item == "-":
                CalculationMinus.keisan(answer)
            elif item == "*":
                CalculationMultiplied.keisan(answer)
            elif item == "/":
                CalculationDivided.keisan(answer)
            else:
                answer.append(item)

        return answer


value = ("6 2 3 4 + - *")

value1 = ValueCalculation(value)
print(value1.text())
print(value1.excute())