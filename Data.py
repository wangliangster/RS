#import numpy as np
#May change to other type as requirement in future
defaultData = {1: "焦耳食堂", 2: "兰州拉面", 3: "牛汤哥", 4: "江西米粉", 5: "美食城", 6: "便利峰"}

class Data(object):
    # Class DataSet maybe declared here
    #dataset = {1: "焦耳食堂", 2: "兰州拉面", 3: "牛汤哥", 4: "江西米粉", 5: "美食城", 6: "便利峰"}
    classSharedDataset = defaultData
    def __init__(self, initData=None):
        if initData is None:
            initData = defaultData
        # object private dataset
        self.dataset=initData
    def add(self, element=None):
        if element is None:
            element = {1:"今天随便吧"}
        self.dataset.update((element))
    def AddToClass(self,element = None):
        if element is None:
            element = {1:"今天随便吧"}
        Data.classSharedDataset.update(element)
    def remove(self,element =None):
       if self.dataset is not None:
            if element is None:
                self.dataset.pop(1)
            else:
                self.dataset.popitem()
    def RemoveFromClass(self, element = None):
        if Data.classSharedDataset is not None:
            if element is None:
                Data.classSharedDataset.pop(1)
            else:
                # operate relate to element
                Data.classSharedDataset.popitem()
#                del Data.classSharedDataset[2]
    def modify(self,element = None):
        if element is None:
            element = {1:"带饭"}
        self.dataset.update(element)
    def ModifyClassData(self,element = None):
        if element is None:
            element = {1:"不吃了"}
        Data.classSharedDataset.update(element)
    def format1(self):
        # op in here
        return self.dataset
    def format2(self):
        # op in here
        return self.dataset
    def format3(self):
        # op in here
        return self.dataset
    def Format1(self):
        # op Class Shared Data
        return Data.classSharedDataset
    def Format2(self):
        # op Class Shared Data and output as format2 for using
        return Data.classSharedDataset
    def Format3(self):
        # op Class Shared Data and output as format2 for using
        return Data.classSharedDataset
    def SharedDataset(self):
        return Data.classSharedDataset
    def otherOP(self):
        pass
