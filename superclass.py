class Base(object):
    def __init__(self):
        self.B_leader =  None
        self.B_gender = "male"
        self.G_leader =  None
        self.G_gender = "female"

    def Status(self):
        print("会長:{0} 性別:{1} 女子部長:{2} 性別:{3}".format(self.B_leader, self.B_gender, self.G_leader, self.G_gender))

class Weekend(Base):
    def __init__(self, name1, name2):
        super().__init__()
        self.B_leader = name1
        self.G_leader = name2


#, name1=None,name2=None
#
