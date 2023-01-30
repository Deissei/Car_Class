from com_company_details.Engine import Engine
from com_company_professions_.Driver import Driver
from com_company_vehicles.Lorry import Lorry
from com_company_vehicles.SportCar import Sportcar


class Car(Driver, Engine, Lorry, Sportcar):
    def __init__(self, name, surname, exper, power, manufacturer, brand_auto, class_auto, the_weight, carrying, speed):
        super().__init__(name, surname, exper)
        self.brand_auto = brand_auto
        self.class_auto = class_auto
        self.the_weight = the_weight
        self.power_init = power
        self.manufacturer_init = manufacturer
        self.carrying = carrying
        self.max_speed = speed

    def start(self):
        return 'Поехали!'
    
    def stop(self):
        return 'Останавливаемся!'
    
    def turnRight(self):
        return 'Поворот направо!'
    
    def turnLeft(self):
        return 'Поворот налево!'

    def toString(self):
        a = Engine(self.power_init, self.manufacturer_init)
        b = Lorry(self.carrying)
        c = Sportcar(self.max_speed)
        info_driver = f'Фио: {self.name} {self.surname}\nСтаж Водителя: {self.exper} года\nМощность автомобиля: {a.power} | Производительность автомобиля: {a.manufacturer}'
        info_car = f'Модель Автомобиля: {self.brand_auto}\nКласс Автомобиля: {self.class_auto}\nВес Автомобиля: {self.the_weight} тон'
        return f'{info_driver}\n{info_car}\nГрузоподъемностью кузова: {b.carrying} кг\nМаксимальная скорость: {c.max_speed} км/час'
    

toyota_supra = Car('Dastan', 'Kubatbaev', 5, 5252, 3000, 'Toyota', 'SportCar', 5, 300, 320)
print('*'*40)
print()
print(toyota_supra.start())
print()
print(toyota_supra.turnLeft())
print()
print(toyota_supra.turnRight())
print()
print(toyota_supra.stop())
print()
print('*'*40)
print(toyota_supra.toString())
print('*'*40)
