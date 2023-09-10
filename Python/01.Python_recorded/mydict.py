class dict_parse :
    def __init__(self , dic):
        self.dic = dic
        
    def key(self):
        if self.notdict() :
            return list(self.dic.keys())
                 
    def value(self):
        if self.notdict() :
            return list(self.dic.values())  
    def notdict(self):
        if type(self.dic) != dict :
            raise Exception('Not a dictionary')
        return 1
    def parse(self):
        self.dic = eval(input())
        print(self.dic , type(self.dic))
        print(self.key())
        print(self.value())
        
    def insert(self,k,v) :
        self.dic[k] = v