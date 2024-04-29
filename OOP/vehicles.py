
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


v1 = Vehicle("BMW", "3 Series")
print(v1.brand, v1.model)