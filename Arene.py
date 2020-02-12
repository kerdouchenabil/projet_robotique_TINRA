from Robot import Robot


class Arene:
    def __init__(self, dimx, dimy):
        self.dimx = dimx
        self.dimy = dimy
        self.r1 = Robot(100, 50, "robot1")

    def getdimx(self):
        return self.dimx

    def getdimy(self):
        return self.dimy