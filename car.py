class Car:
    def __init__(self,make, model,year,price,mileage,id=None):
        # Your code here
        if year < 0:
            raise ValueError("Year cannot be negative.")
        if price < 0:
            raise ValueError("Price cannot be negative.")

        self.id=id
        self.make=make
        self.model=model
        self.year=year
        self.price=price
        self.mileage=mileage

    def __str__(self):
        return (
            f"[ID: {self.id}] "
            f"{self.year} {self.make} {self.model} | "
            f"${self.price:,.2f} | "
            f"{self.mileage:,} km"
        )
    
    def to_tuple(self):
        return (
            self.make,
            self.model,
            self.year,
            self.price,
            self.mileage
        )
mycar = Car("Toyota", "Camry", 400, 24999.99, 15000, 1)
print(mycar)
print(mycar.to_tuple())