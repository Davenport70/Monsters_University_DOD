from Monsters_class import *

class Student(Monsters):

    def __init__(self, f_name, l_name, student_id):
        super().__init__(f_name, l_name)
        self.student_id = student_id
        self.skills = []
    # def fly(self):
    #     return 'flying'
    #
    # def speed(self):
    #     return 'ZOOM!'
    #
    # def sonar(self):
    #     return 'Bleep bleep bleep'
    #
    # def strength(self):
    #     return 'Lift'



        #             (self, fly, speed, sonar, strength):
        # self.fly = fly
        # self.speed = speed
        # self.sonar = sonar
        # self.strength = strength



