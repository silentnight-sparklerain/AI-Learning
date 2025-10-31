class New_Car:
    """模拟汽车"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.gas = 100
        self.odometer_reading = 0  # 给属性赋默认值（里程为0）

    def Get_Descriptive_Name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def Read_Odometer(self):
        """打印一条信息，指出汽车行驶里程"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def Update_Odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        self.odometer_reading = mileage



class Battery:
    """模拟电动汽车的电池"""

    def __init__(self, battery_size = 40):  # 默认battery_size = 40
        self.battery_size = battery_size

    def Print_Battery(self):
        print(f"This car has a {self.battery_size}-kwh battery")

    def Get_Range(self):
        """打印一条消息，指出电池的续航里程"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")



class New_ElectricCar(New_Car):
    """模拟电动汽车"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery_size = Battery()  # 初始化电动汽车的特有属性

    def PrintBattery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")