class Hrac(object):

    def __init__(self, jmeno):
        self.jmeno = str.rstrip(jmeno)
        self.zapasy = 0
        self.goly = 0

    def get_zapasy(self):
        return self.zapasy

    def get_goly(self):
        return self.goly

    def hral_zapas(self):
        self.zapasy += 1

    def dal_gol(self):
        self.goly += 1

    def info(self):
        print(self.jmeno + " Z:" + str(self.zapasy) + " G:" + str(self.goly))

    def __repr__(self):
        return self.jmeno
    

class Tym(object):

    def __init__(self, nazev_tymu):
        self.nazev_tymu = nazev_tymu
        self.hraci = {}

    def pridej_hrace(self, hrac):
        cislo = 1
        while cislo in self.hraci:
            cislo += 1
        self.hraci.update({cislo:hrac})

    def zapas(self, *goly):
        for hrac in self.hraci.values():
            hrac.hral_zapas()
        for cislo in goly:
            self.hraci[cislo].dal_gol()

    def filtruj_hrace(self, pocet_golu):
        return [x for x in self.hraci.values() if x.goly >= pocet_golu]

    def info(self):
        print(self.nazev_tymu)
        for hrac in self.hraci.values():
            hrac.info()
        

def main():
    tym = Tym('Czech Republic')

    try:
        file = open('hraci.txt', 'r')

    except:
        print('Nelze otevrit soubor')

    for line in file:
        tym.pridej_hrace(Hrac(line))

    file.close()
    tym.zapas(1,3,4, 1,1)
    tym.info()
    print(tym.filtruj_hrace(1))
    

    
        

if __name__=='__main__':
    main()
