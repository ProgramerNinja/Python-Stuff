# Jared
# 1/17/19
# human

class Human(object):

    def __init__(self, name, hair_color, eye_color, height, weight, iq, gender, race):
        self.name = name
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.height = height
        self.weight = weight
        self.iq = iq
        self.gender = gender
        self.race = race

    def intro_self(self):
        print()
        print()
        print("hola mi llamo es " + self.name)

    def describe_self(self):
        print()
        print()
        print("yo tengo " + self.hair_color + " palo")
        print("yo tengo " + self.eye_color + " ojos")
        print("yo soy ", self.height, "feet alto")
        print("yo peso ", self.weight, " lbs")
        print("yo soy un " + self.race + " " + self.gender + " " + "con un iq de ", self.iq)

    def iq_self(self):
        print()
        print()
        print("tu current iq is:", self.iq)
        q1 = input("que es el forma de la tierra? ").lower()
        if q1 == "circle" or "sphere":
            print("eso es correcto!!!")
            self.iq += 15
            print("tu iq es ahora:", self.iq)
        else:
            print("lo siento que no es correcto")

    def BMI_self(self):
        print()
        print()
        print("tu BMI es basa en su altura:", self.height, "feet alto, y tu peso:", self.weight, "lbs")
        kilo = self.weight * 0.453592
        meter = self.height * 0.3048
        meter2 = meter * meter
        bmi = kilo // meter2
        print("tu bmi es:", bmi)
        if bmi > 30:
            print("Eres obeso")
        elif bmi > 25:
            print("tienes sobrepeso")
        elif bmi > 18:
            print("tu BMI es normal / saludable")
        else:
            print("estas bajo de peso")


jared = Human("Jared", "rubio", "azul", 5.9, 153, 99, "masculino", "americano")

jared.intro_self()
jared.describe_self()
jared.iq_self()
jared.BMI_self()
