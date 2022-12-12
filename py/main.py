class Odam:
    def __init__(self,ism, fam, yosh, tugulgan,):
        self.ism = ism
        self.fam = fam
        self.yosh = yosh
        self.tugulgan  = tugulgan 
    def shifr(self):
        print(self.ism, self.fam, self.yosh, self.tugulgan)
    
o1=Odam("Ubaydullo", "Jumayev", 21, 2002 )
o2=Odam("Ozodbek", "Turobov", 14, 2008 )

print(o1.shifr())
print(o2.shifr())