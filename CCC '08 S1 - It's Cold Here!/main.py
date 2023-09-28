# problem: https://dmoj.ca/problem/ccc08s1


class City:

    cities = []
    city_names = []
    city_temps = []

    def __init__(self, name, temp) -> None:
        
        self.name = name
        self.temp = temp

        City.add_city(self) 

    

    @classmethod
    def lowest_temp(cls):

        for i in cls.cities:

            cls.city_names.append(i.name)
            cls.city_temps.append(i.temp)

        index = cls.city_temps.index(min(cls.city_temps))

        return cls.city_names[[index]]

        print(f"lowest temperature: {cls.city_temps[index]}\nlocation: {cls.city_names[index]}")



    @classmethod
    def add_city(cls, city):

        cls.cities.append(city)        

    

    
with open("input.txt", "r") as reader:

    for x in reader:

        city, temp = x.split(" ")

        City(str(city.strip()), float(temp.strip()))


City.lowest_temp()