from MultiPlatform import PlatformClass, PlatformFunction
import os

class DefineClearScreen(PlatformFunction):
    @staticmethod
    def __win32__():
        os.system("cls")
    @staticmethod
    def __darwin__():
        os.system("clear")
    @staticmethod
    def __linux__():
        os.system("clear")


class test(PlatformClass):
    def __win32_init__(self,val):
        #print("hello windows")
        self.b = val
    def __win32_add__(self,a):
        return test(self.b + a.b)
    def __win32_str__(self):
        return f"windows_test({self.b})"

class ComputerPerson(PlatformClass):
    def __uni_init__(self,name):
        self.name = name
        self.os = None
    def __win32_init__(self,*args,**kwargs):
        self.os = "Windows"
    def __darwin_init__(self,*args,**kwargs):
        self.os = "Mac"
    def __linux_init__(self,*args,**kwargs):
        self.os = "Linux"
    def __str__(self):
        if self.os == None:
            return f"hello, my name is {self.name} and I use no platform"
        return f"hello, my name is {self.name} and I am using the {self.os} platform on my computer"
    


if __name__ == "__main__":
    #clearscreen = DefineClearScreen()
    #clearscreen()

    person = ComputerPerson("isaac")
    print(str(person))
