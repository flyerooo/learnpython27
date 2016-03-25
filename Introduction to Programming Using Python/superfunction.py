__metaclass__ = type

class Person:
    def __init__(self):
        self.height = 160

    def about(self, name):
        print "{} is about{}".format(name, self.height)

class Girl(Person):
    def __init__(self):
        super(Girl, self).__init__()
        self.breast = 90
    def about(self, name):
        print "{} is a hot girl, shi is about {}, and her breast is {}".format(name, self.height, self.breast)

if __name__ == "__main__":
    cang = Girl()
    cang.about("canglaoshi")