from Value import *

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
        stack = self.stack
        answer = []

        def keisan(list, symbol):
            tmpList = list[-2:]
            text = "{0} {1} {2}".format(tmpList[0],symbol,tmpList[1])
            tmpValue = eval(text)
            return tmpValue

        for item in stack:
            if item in ("+", "-", "*", "/"):
                tmpValue = keisan(answer, item)
                answer.pop()
                answer.pop()
                answer.append(tmpValue)
            else:
                answer.append(item)

        return answer



value = ("6 2 3 4 + - *")

value1 = ValueCalculation(value)
print(value1.text())
print(value1.excute())