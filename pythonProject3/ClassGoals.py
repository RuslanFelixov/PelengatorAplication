import numpy as np

class ClassGoals:
    def getClassName(self, tAnt, indMin, Wpt):
        coefSmal = 1.2e8 * np.exp(-0.9 * tAnt[indMin])
        coefMedium = 1.5e8 * np.exp(-0.9 * tAnt[indMin])
        coefBig = 2e8 * np.exp(-0.9 * tAnt[indMin])

        coefSig = np.max(Wpt)

        if coefSig < coefSmal:
            return 'Буй'
        elif coefSig > coefSmal and coefSig < coefBig:
            return 'НПА'
        elif coefSig > coefBig:
            return 'АПЛ'
