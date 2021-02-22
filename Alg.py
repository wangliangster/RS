import random
from Data import *
from User import *

class Alg(object):
    DefaultData = Data.classSharedDataset
    DefaultUser = User.classShareUser
    Result = []
    def __init__(self,dataInit= None, userInt= None):
        if dataInit is None or userInt is None:
            dataInit = Alg.DefaultData
            userInt = Alg.DefaultUser
        self.data = dataInit
        self.user = userInt
    def Random(self, user = None, data = None):
        if user is None or data is None:
            data = Alg.DefaultData
            user = Alg.DefaultUser
            #### 算法部分 ####
            try:
                Alg.Result = random.choices(data)
            except:
                print("here, dataset is null, please input data for Recommendation")
        return Alg.Result
    def CNN(self, User = None, Data = None):
        print("using CNN Alg")
        return Alg.Result
    def LSTM(self, User = None, Data = None):
        print("using LSTM Alg")
        return Alg.Result
    def GNN(self, User = None, Data = None):
        print("using GNN Alg")
        return Alg.Result
