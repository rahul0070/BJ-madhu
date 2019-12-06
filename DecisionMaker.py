from Strategy import Strategy
import miscellaneous as misc

class DecisionMaker:

    def __init__(self):
        self.data = Strategy()
        self.ranks = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':'A'}


    def getRank(self, list):
        resultList = []
        for i in list:
            r = self.ranks.get(i)
            resultList.append(str(r))
        return resultList


    def findTable(self, tableName):
        tables = {'dealerKey':0, 'Normal':1, 'Ace':2, 'Double':3}
        return tables.get(tableName)


    def getCondtition(self, list):
        condition = 'Normal'
        if misc.sumOfList(list) > 21:
            condition = 'Bust'

        elif misc.sumOfList(list) == 21:
            condition = 'BJ'

        elif list[0] == list[1]:
            condition = 'Double'

        else:
            for i in list:
                if i == 'A':
                    condition = 'Ace'
        return condition


    def getOtherElement(self, list):
        list.remove('A')
        return list[0]


    def getScore(self, player, condition):
        if condition == 'Ace' and len(player)<=2:
            score = self.getOtherElement(player)

        elif condition == 'Double' and len(player)<=2:
            score = player[0]

        elif condition == 'Normal' or len(player)>2:
            score = 0
            score = misc.sumOfList(player)
            condition = 'Normal'

        print('Sc ',score)
        return score, condition


    def findOutcome(self, player, dealer):
        player = self.getRank(player)
        print(player, dealer)
        dealerIndex = self.data.strategyList[self.findTable('dealerKey')].get(dealer[0])
        condition = self.getCondtition(player)
        print(condition)
        if condition == 'Bust' or condition == 'BJ':
            return condition

        score, condition = self.getScore(player, condition)
        scoreList = self.data.strategyList[self.findTable(condition)].get(str(score))
        print('99: ', scoreList)
        return scoreList[dealerIndex]