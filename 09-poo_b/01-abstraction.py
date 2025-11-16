class coffeMaker:
    
    def make_coffe(self):
        self.__boil_watter()
        self.__mix()
        print("Pip Pip")
        print("Tu café está listo.")
    
    def __boil_watter(self):
        pass
    
    def __mix(self):
        pass

coffe_maker = coffeMaker()
coffe_maker.make_coffe()