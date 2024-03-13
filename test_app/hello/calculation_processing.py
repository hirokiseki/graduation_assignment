# Valueクラスを定義
class Value:

    # コンストラクタを定義
    def __init__(self, value):

        # ここでstackに分解したい
        self.value = value
        self.stack = value

    # 表示用メソッド
    def text(self):
        pass

    def excute(self):
        pass

class ValueCalculation(Value):
    # コンストラクタ
    def __init__(self, value):

        #親クラスのコンストラクタを呼び出す
        super().__init__(value)

        self.value = value

    # 別メソッドを追加
    def anotherText(self):
        text = "入力内容は {} です."
        return text.format(self.stack)

    def text(self):
        text = "入力内容は {} でした."
        return text.format(self.value)


value = ("1 2 3 + -")

value1 = ValueCalculation(value)
print(value1.text())

value2 = ValueCalculation(value)
print(value2.anotherText())
