from app import app
from codecarbon import OfflineEmissionsTracker

class CalculFonction:
    def __init__(self, I, WS, Ta, T0, Minutes):
        self.I = I
        self.WS = WS
        self.Ta = Ta
        self.T0 = T0
        self.Minutes = Minutes
    def Calcul(value):
        for i in range(1, 60):
            Ftc = ((-value.WS / 1600)*0.4 - 0.1)*(value.T0 - value.Ta -(value.I**1.4 / 73785)*130)
            resultFtc = Ftc + value.T0
            value.T0 = resultFtc
        return resultFtc
        # print("Mes donées : " + value.WS, value.T0, value.Ta, value.I)


    def Calculboucle(self):
        tracker = OfflineEmissionsTracker(country_iso_code="FRA")
        tracker.start()
        arr = {}
        for i in range(1, self.Minutes):
            arr[i] = self.Calcul()

        tracker.stop()
        return arr
