#import numpy as np

defaultUser = {"Name": "Wang Liang","Sex": "Male", "Prefer": "Spice and Sweet", "From": "JiangXi"}

class User(object):
    classShareUser= defaultUser
    def __init__(self,UserInit = None):
        if UserInit is None:
            UserInit = User.classShareUser
        self.user = UserInit
    def modify(self, key = None, element = None):
        if key is None:
            key = "Name"
            element = "Wang GuiXing"
        self.user[key]=element
    def Modify(self, key = None, element = None):
        if key is None:
            key = "Name"
            element ="Wang GuiXing"
        User.classShareUser[key]=element
    def format1(self):
        # op
        return self.user
    def format2(self):
        # op
        return self.user
    def Format1(self):
        #op
        return User.classShareUser
    def Format2(self):
        return User.classShareUser
