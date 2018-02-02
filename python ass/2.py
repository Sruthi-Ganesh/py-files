class product:
    x=1
    def _init_(self):
        pass
    def create_products(self):
        self.prod={}
        self.x=int(raw_input("Enter the number of products"))
        for i in range(1,self.x +1):
            y=raw_input("Enter product names for "+ str(i) +" ")
            self.prod[i]=y
            
        
    def display(self):
        for k, v in self.prod.items():
            print str(k) + " " + v

prod=product()
prod.create_products()
prod.display()
        
            
