class Tostring :
    def __init__(self,list_str) :
        self.orig_list=list_str
    def tostr(self) :
        # print("This function will return a string from a list")
        return " ".join(self.orig_list)

