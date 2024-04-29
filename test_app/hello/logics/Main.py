class Caluculator:
    # 入力された文字列を取得
    def __init__(self, inputValues):
        self.values = inputValues.split()
        self.tmpStack = []
        self.ansStack = []

    # 入力された文字列を出力
    def getInputValues(self):
        return self.values

    # 計算結果を出力
    def getAnsStack(self):
        return self.ansStack

    # 入力された文字列を計算しやすいようにインスタンスで整理
    def maketmpStack(self):
        for item in self.values:
            if item.isdigit():
                self.tmpStack.append(Number(item))
            elif item == "+":
                self.tmpStack.append(PlusOperater(item))
            elif item == "-":
                self.tmpStack.append(MinusOperater(item))
            elif item == "*":
                self.tmpStack.append(MultipliedOperater(item))
            elif item == "/":
                self.tmpStack.append(dividedOperater(item))

    # 計算を実行
    def execute(self):
        for item in self.tmpStack:
            tmpValue = item.execute(ansStack)
            self.ansStack.append(tmpValue)

class Value:
    def __init__(self, inputValue):
        self.value = inputValue

    def getValue(self):
        return self.value
    
    def execute(self):
        pass

class Number(Value):
    def __init__(self, inputValue, ansStack):
        super().__init__(inputValue)

    def getValue(self):
        return float(self.value)

    def execute(self, ansStack):
        return float(self.value)


class PlusOperater(Value):
    def __init__(self, inputValue):
        super().__init__(inputValue)

    def text(self):
        return self.value
    
    def execute(self, ansStack):
        return ansStack.pop(-1) + ansStack.pop(-1)

class MinusOperater(Value):
    def __init__(self, inputValue):
        super().__init__(inputValue)

    def text(self):
        return self.value
    
    def execute(self):
        pass

class MultipliedOperater(Value):
    def __init__(self, inputValue):
        super().__init__(inputValue)

    def text(self):
        return self.value
    
    def execute(self, ansStack):
        pass ansStack.pop(-1) * ansStack.pop(-1)

class dividedOperater(Value):
    def __init__(self, inputValue):
        super().__init__(inputValue)

    def text(self):
        return self.value
    
    def execute(self):
        pass




inputValues = "1 2 3 + *"
caluculator = Caluculator(inputValues)
caluculator.execute()
ansStack = caluculator.getAnsStack()
print(ansStack)