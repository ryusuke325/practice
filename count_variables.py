class Nth_power():
    """本当はn乗を指定できるようにしたい"""
    def __init__(self,x,n):
        self.n = n
        self.x = x

    def main(self):
        a = self.x
        b = self.x ** 2
        return a,b
