from constants import *

class Item:
    def __init__(self, name, length, width, height, weight):
        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight
        self.rotation_type = 0 # initial rotation type: (x, y, z) --> (l, w, h)
        self.position =  START_POSITION # initial position: (0, 0, 0)
        
        
    def get_volume(self):
        return (self.length * self.height * self.width)
    
    def get_dimension(self): # 6 orientation types -- (x-axis, y-axis, z-axis)
        if self.rotation_type == RotationType.RT_LWH:
            dimension = [self.length, self.width, self.height]
        elif self.rotation_type == RotationType.RT_HLW:
            dimension = [self.height, self.length, self.width]
        elif self.rotation_type == RotationType.RT_HWL:
            dimension = [self.height, self.width, self.length]
        elif self.rotation_type == RotationType.RT_WHL:
            dimension = [self.width, self.height, self.length]
        elif self.rotation_type == RotationType.RT_WLH:
            dimension = [self.width, self.length, self.height]
        elif self.rotation_type == RotationType.RT_LHW:
            dimension = [self.length, self.height, self.width]
        else:
            dimension = []
        
        return dimension
        
    def string(self):
        rotation_list = ["LWH","HLW","HLW","WHL","WLH","LHW"]
        return "%s(%sx%sx%s, weight: %s) pos(%s) rt(%s) vol(%s)" % (
            self.name, self.length, self.width, self.height, self.weight,
            self.position, rotation_list[self.rotation_type], self.get_volume()
        )