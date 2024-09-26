class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.cpu * self.memory

    def __str__(self):
        return f"Computer: CPU - {self.__cpu}, Memory - {self.__memory}"

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if sim_card_number <= len(self.__sim_cards_list):
            sim_operator = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты - {sim_card_number}-{sim_operator}")
        else:
            print("Неверный номер сим-карты")

    def __str__(self):
        return f"Phone: Sim cards list - {self.__sim_cards_list}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Построение маршрута до {location}")

    def __str__(self):
        return f"SmartPhone: CPU - {self.cpu}, Memory - {self.memory}, Sim cards list - {self.sim_cards_list}"


computer = Computer("Intel CORE i3", 16)
phone = Phone(["Beeline", "Megacom", "O!"])
smartphone1 = SmartPhone("Android", 64, "Beeline, O!")
smartphone2 = SmartPhone("IOS", 128, "Megacom, O!")

print(computer)
print(phone)
print(smartphone1)
print(smartphone2, "\n")

print(computer.make_computations())
phone.call(3, "+996 707 99 99 99")
smartphone1.use_gps("Geeks\n")

print(computer == smartphone1)
print(smartphone1 > smartphone2)
print(smartphone2 >= computer)
print(computer != smartphone2)
