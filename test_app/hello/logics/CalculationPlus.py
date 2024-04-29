class CalculationPlus:

    # # コンストラクタ
    # def __init__(self, tmplist):
    #     self.tmplist = tmplist

    def keisan(answerList):
        tmpList = answerList[-2:]
        tmpValue = int(tmpList[0]) + int(tmpList[1])
        answerList.pop()
        answerList.pop()
        answerList.append(tmpValue)

        return answerList



        #文字列をもらってそれが計算対象であることを認識する
        #ファクトリークラス　スタックをオブジェクトとして処理
        #スタックに積むものを半別して