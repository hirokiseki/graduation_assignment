class CalculationMultiplied:

    # # コンストラクタ
    # def __init__(self, tmplist):
    #     self.tmplist = tmplist

    def keisan(answerList):
        tmpList = answerList[-2:]
        tmpValue = int(tmpList[0]) * int(tmpList[1])
        answerList.pop()
        answerList.pop()
        answerList.append(tmpValue)

        return answerList