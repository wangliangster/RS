#import numpy as np
import random

#import Data
from Alg import *
#import User

class Recommender(object):
    RsUser = User.classShareUser
    RsData = Data.classSharedDataset
    #data = Data.SharedDataset()
    RsAlg = Alg
    RsResult = []

    def __init__(self, objUser= None, objData=None, objAlg = None, AlgMethold = None):
        if objUser is None:
            objUser = Recommender.RsUser
        if objData is None:
            objData = Recommender.RsData
        if objAlg is None:
            objAlg = Recommender.RsAlg
        self.user = objUser
        self.data = objData
        self.alg = objAlg
        if AlgMethold == "CNN":
            Recommender.RsResult=self.alg.CNN(self.user,self.data)
        if AlgMethold == "LSTM":
            Recommender.RsResult=self.alg.LSTM(self.user,self.data)
        if AlgMethold == "GNN":
            Recommender.RsResult = self.alg.GNN(self.user, self.data)
        if AlgMethold is None:
            Recommender.RsResult = self.alg.Random(self.user, self.data)

    # Display 的所有功能在此开发，比如今天天气
    def display(self):
        try:
            try:
                print("Hi:", self.user['Name'])
            except:
                print("Hi:", Recommender.RsUser['Name'])
            print("今天中午，向您推荐:")
        except:
            print("Except User:", self.user)
            print("Except Data:", self.data)
            print("Except Alg:", self.alg)
    def Display(self):
        try:
            print("User", Recommender.RsUser)
            print("Data", Recommender.RsData)
            print("Alg", Recommender.RsAlg)
        except:
            print("User", Recommender.RsUser)
            print("Data", Recommender.RsData)
            print("Alg", Recommender.RsAlg)

u = {"Name": "Wang GuiXing","Sex": "Male", "Prefer": "Spice and Sweet", "From": "JiangXi"}
d = {1: "焦耳食堂", 2: "兰州拉面", 3: "牛汤哥", 4: "江西米粉", 5: "美食城", 6: "便利峰",7:"随便吃", 8:"不吃了"}
a = 'CNN'


if __name__ == '__main__':
    # # Default Recommender Result:
    # print("Default Recommender Result:", Recommender.RsResult)
    #
    # # Usage 1
    # rsobj1 = Recommender(u,d,AlgMethold=a)
    # rsobj1.display()
    # print(Recommender.RsResult)
    #
    # # Usage 2
    # rsobj2 = Recommender(u,d,AlgMethold="LSTM")
    # rsobj2.display()
    # print(Recommender.RsResult)
    #
    # # Usage 3
    # rsobj3 = Recommender(u,d)
    # rsobj3.display()
    # print(Recommender.RsResult)
    #
    # # Usage 4
    # rsobj4 = Recommender(u)
    # rsobj4.display()
    # print(Recommender.RsResult)
    #
    # # Usage 5
    # rsobj5 =Recommender(objData=d)
    # rsobj5.display()
    # print(Recommender.RsResult)

    # Usage 6, Nothing input, just use default value
    rsobj6 =Recommender()
    rsobj6.display()
    print(Recommender.RsResult)
