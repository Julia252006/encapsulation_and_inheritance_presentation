class GrandFather:
    def __init__(self, property):
        self.__property = property

    def get_property(self):
        return self.__property

    def set_property(self, property):
        self.__property = property

    property = property(get_property, set_property)


class Father(GrandFather):
    def __init__(self, property, knowledge):
        GrandFather.__init__(self, property)
        self.__knowledge = knowledge

    def get_knowledge(self):
        return self.__knowledge

    def set_knowledge(self, knowledge):
        self.__knowledge = knowledge

    knowledge = property(get_knowledge, set_knowledge)


class Uncle:
    def __init__(self, life_hacking):
        self.__life_hacking = life_hacking

    def get_life_hacking(self):
        return self.__life_hacking

    def set_life_hacking(self, life_hacking):
        self.__life_hacking = life_hacking

    life_hacking = property(get_life_hacking, set_life_hacking)


class Child(Father, Uncle):
    def __init__(self, property, knowledge, life_hacking, mastery):
        Father.__init__(self, property, knowledge)
        Uncle.__init__(self, life_hacking)
        self.__mastery = mastery

    def get_mastery(self):
        return self.__mastery

    def set_mastery(self, mastery):
        self.__mastery = mastery

    mastery = property(get_mastery, set_mastery)


print('\n\tGrandFather Test:')
grand_father = GrandFather('house')
print(grand_father.property)

print('\n\tFather Test:')
father = Father('house', 'car repairing')
print(father.property)
print(father.knowledge)

print('\n\tUncle Test:')
uncle = Uncle('know how to drink a lot :)')
print(uncle.life_hacking)

print('\n\tChild Test:')
child = Child('house', 'car repairing', 'know how to drink a lot :)',
              'car-service management')
print(child.property)
print(child.knowledge)
print(child.mastery)
print(child.life_hacking)
