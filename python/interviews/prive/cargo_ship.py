class CargoShip:
    
    def __init__(self, capacity):
        self.cargo = []
        self.capacity = capacity
        
    def unload(self, port):
        """
        :param port: (String)
        :returns: [(String, Int)]
        """
        ret = [i for i in self.cargo if i[0] == port]
        self.cargo = [i for i in self.cargo if i[0] != port]
        return ret
    
    def can_depart(self):
        """
        :returns: (Bool)
        """
        return sum([i[1] for i in self.cargo]) <= self.capacity
    
    def load(self, new_cargo):
        """
        :param new_cargo: [(String, Int)]
        """
        self.cargo = new_cargo
    
if __name__ == "__main__":
    ship = CargoShip(10)
    ship.load([("New York", 1), ("London", 20)])
    print(ship.unload("New York")) #should print [("New York", 1)]
    print(ship.cargo) #should print [("London", 20)]
    print(ship.can_depart()) #should print False