class TV:
    CANAL_MIN = 1
    CANAL_MAX = 100
    VOLUME_MIN = 0
    VOLUME_MAX = 100

    def __init__(self):
        self.__canal = 1
        self.__volume = 50

    def setCanal(self, canal):
        if self.CANAL_MIN <= canal <= self.CANAL_MAX:
            self.__canal = canal
        else:
            print(f"Canal invalido. Escolha entre {self.CANAL_MIN} e {self.CANAL_MAX}.")

    def aumentarVolume(self, quantidade=1):
        self.__volume = min(self.VOLUME_MAX, self.__volume + quantidade)

    def diminuirVolume(self, quantidade=1):
        self.__volume = max(self.VOLUME_MIN, self.__volume - quantidade)

    def __str__(self):
        return f"TV - Canal: {self.__canal} | Volume: {self.__volume}"


if __name__ == "__main__":
    tv = TV()
    print(tv)
    tv.setCanal(13)
    tv.aumentarVolume(10)
    tv.diminuirVolume(3)
    print(tv)
    tv.setCanal(200)
    tv.diminuirVolume(60)
    print(tv)