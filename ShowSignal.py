import numpy as np
import matplotlib.pyplot as plt
import math

class ShowSignal():
    def viewSignal(self, tAnt, sMod):
        fig = plt.figure()
        plt.plot(tAnt, sMod)
        plt.title('Сигнал на ПЭ')
        plt.xlabel('Время, с')
        plt.ylabel('Амплитуда сигнала')
        fig.savefig('signal.png', dpi=65)
        # plt.show()



    def viewFilter(self, tAnt, sFiltr):
        fig = plt.figure()
        plt.plot(tAnt, sFiltr)
        plt.title('Фильтрация сигнала')
        plt.xlabel('Время, с')
        plt.ylabel('Амплитуда сигнала')
        fig.savefig('filter.png', dpi=65)



    def viewSetResponse(self, Wp, tAnt, indMax, indMin):
        Wp = np.flipud(Wp)
        fig = plt.figure()
        plt.imshow(Wp, origin='lower',
                   extent=[-90, 90, tAnt[indMax], tAnt[indMin]],
                   aspect=500)
        plt.xlabel('Градусы')
        plt.ylabel('Время, с')
        plt.title('Набор откликов антенны в яркостном виде')
        fig.savefig('response.png', dpi=65)
        # plt.show()


    def viewGridCoordinates(self, distance, peleng, classGoals):
        numHighlights = 0

        if classGoals == 'Буй':
            numHighlights = 2
        elif classGoals == 'НПА':
            numHighlights = 6
        elif classGoals == 'АПЛ':
            numHighlights = 15

        coef = 0
        if peleng < 0:
            coef = -1
        else:
            coef = 1

        step = 5

        fig = plt.figure()
        xAnt = [0, 0]
        yAnt = [distance * np.sin(np.deg2rad(peleng)),
                    distance * np.cos(np.deg2rad(peleng))]
        plt.plot(xAnt[0], xAnt[1], 'or', label='Антенна')
        for i in range(0, numHighlights):
            if i == 0:
                plt.plot(yAnt[0], yAnt[1], 'ob', linewidth=2, label=classGoals)
            else:
                plt.plot(yAnt[0] - step, yAnt[1] - coef * step, 'ob', linewidth=1)
                plt.plot(yAnt[0] + step, yAnt[1] + coef * step, 'ob', linewidth=1)

            step += 5

        plt.axis([-1000, 1000, 0, 1000])
        plt.xlabel('Ось, х')
        plt.ylabel('Ось, у')
        plt.title('Координаты цели и антенны')
        plt.legend()
        plt.grid()
        fig.savefig('grid.png', dpi=65)
            # plt.show()















