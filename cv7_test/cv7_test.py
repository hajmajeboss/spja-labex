import xml.etree.ElementTree as ET

class Poslanec(object):
    def __init__(self, jmeno, hlasy):
        self.jmeno = jmeno
        self.hlasy = float(hlasy)

    def get_jmeno(self):
        return self.jmeno

    def get_hlasy(self):
        return self.hlasy

    def __repr__(self):
        return self.jmeno + " (" + str(self.hlasy) + ")"

    def __lt__(self, other):
        return self.hlasy < other

    def __gt__(self, other):
        return self.hlasy > other


class Strana(object):
    def __init__(self, nazev, procenta):
        self.nazev = nazev
        self.procenta = float(procenta)
        self.poslanci = []

    def get_nazev(self):
        return self.nazev

    def pridej_poslance(self, posl):
        self.poslanci.append(posl)

    def get_poslanci(self):
        return self.poslanci

    def get_procenta(self):
        return self.procenta

    def __repr__(self):
        return self.nazev + " (" + str(self.procenta) + ")"


class Volby(object):
    def __init__(self, xml_file):
        self.xml_file = xml_file
        self.strany = self.parsuj_strany()
    def get_strany(self):
        return self.strany
        
    #TODO 2
    def parsuj_strany(self):
        root = ET.parse(self.xml_file)
        strany = root.findall('STRANA')
        strany_lst = []

        for strana in strany:
            pridavana_strana = Strana(strana.attrib['NAZ_STR'], strana.find('HODNOTY_STRANA').attrib['PROC_HLASU'] )
            poslanci = strana.getiterator('POSLANEC')
            for poslanec in poslanci:
                pridavana_strana.pridej_poslance(Poslanec(poslanec.attrib['JMENO'] + " " + poslanec.attrib['PRIJMENI'], poslanec.attrib['PREDNOSTNI_HLASY']))
            strany_lst.append(pridavana_strana)
        return strany_lst
    
    #TODO 3
    def vrat_strany(self, min_procenta=5):
        vracene_strany = []
        for strana in self.strany:
            if strana.get_procenta() >= min_procenta:
                vracene_strany.append(strana)
        return vracene_strany

    #TODO 4
    def vrat_poslance(self, pocet):
        poslanci_lst = []
        for strana in self.strany:
            poslanci_za_stranu = strana.get_poslanci()
            for poslanec_za_stranu in poslanci_za_stranu:
                poslanci_lst.append(poslanec_za_stranu)
        list.sort(poslanci_lst, reverse=True)
        return poslanci_lst[:pocet]
            

def main():
    volby = Volby("vysledky.xml")
    strany = volby.vrat_strany(5)
    print("SEZNAM STRAN:")
    for s in strany:
        print(s)
        
    print("\nSEZNAM POSLANCU:")
    poslanci = volby.vrat_poslance(7)
    for p in poslanci:
        print(p)

if __name__=="__main__":
    main()
