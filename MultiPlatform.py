from sys import platform

class PlatformClass:
    def __init__(self,*args, **kwargs):
        self.__platform__ = platform
        self.__uni_init__(*args, **kwargs)
        if platform.startswith("win32"):
            self.__win32_init__(*args, **kwargs)
            self.__add_func__ = self.__win32_add__
            self.__str_func__ = self.__win32_str__
            self.__del_func__ = self.__win32_del__
            
        elif platform.startswith("darwin"):
            self.__darwin_init__(*args, **kwargs)
            self.__add_func__ = self.__darwin_add__
            self.__str_func__ = self.__darwin_str__
            self.__del_func__ = self.__darwin_del__
            
        elif platform.startswith("linux"):
            self.__linux_init__(*args, **kwargs)
            self.__add_func__ = self.__linux_add__
            self.__str_func__ = self.__linux_str__
            self.__del_func__ = self.__linux_del__
            
        elif platform.startswith("cygwin"):
            self.__cygwin_init__(*args, **kwargs)
            self.__add_func__ = self.__cygwin_add__
            self.__str_func__ = self.__cygwin_str__
            self.__del_func__ = self.__cygwin_del__
            
        elif platform.startswith("emscripten"):
            self.__emscripten_init__(*args, **kwargs)
            self.__add_func__ = self.__emscripten_add__
            self.__str_func__ = self.__emscripten_str__
            self.__del_func__ = self.__emscripten_del__
            
        elif platform.startswith("aix"):
            self.__aix_init__(*args, **kwargs)
            self.__add_func__ = self.__aix_add__
            self.__str_func__ = self.__aix_str__
            self.__del_func__ = self.__aix_del__
            
        elif platform.startswith("wasi"):
            self.__wasi_init__(*args, **kwargs)
            self.__add_func__ = self.__wasi_add__
            self.__str_func__ = self.__wasi_str__
            self.__del_func__ = self.__wasi_del__
            
        elif platform.startswith('freebsd'):
            self.__freebsd_init__(*args, **kwargs)
            self.__add_func__ = self.__freebsd_add__
            self.__str_func__ = self.__freebsd_str__
            self.__del_func__ = self.__freebsd_del__
            
    def __uni_init__(self):return None
    def __win32_init__(self,*args, **kwargs):return None
    def __darwin_init__(self,*args, **kwargs):return None
    def __linux_init__(self,*args, **kwargs):return None
    def __cygwin_init__(self,*args, **kwargs):return None
    def __emscripten_init__(self,*args, **kwargs):return None
    def __aix_init__(self,*args, **kwargs):return None
    def __wasi_init__(self,*args, **kwargs):return None
    def __freebsd_init__(self,*args, **kwargs):return None

    def __del__(self):
        return self.__del_func__()
    
    def __win32_del__(self):raise NotImplementedError("win32 del dunder function has not been Implemented yet")
    def __darwin_del__(self):raise NotImplementedError("darwin del dunder function has not been Implemented yet")
    def __linux_del__(self):raise NotImplementedError("linux del dunder function has not been Implemented yet")
    def __cygwin_del__(self):raise NotImplementedError("cygwin del dunder function has not been Implemented yet")
    def __emscripten_del__(self):raise NotImplementedError("emscripten del dunder function has not been Implemented yet")
    def __aix_del__(self):raise NotImplementedError("aix del dunder function has not been Implemented yet")
    def __wasi_del__(self):raise NotImplementedError("wasi del dunder function has not been Implemented yet")
    def __freebsd_del__(self):raise NotImplementedError("freebsd del dunder function has not been Implemented yet")

    
    def __add__(self,anotherObj):
        return self.__add_func__(anotherObj)
    
    def __win32_add__(self,anotherObj):return None
    def __darwin_add__(self,anotherObj):return None
    def __linux_add__(self,anotherObj):return None
    def __cygwin_add__(self,anotherObj):return None
    def __emscripten_add__(self,anotherObj):return None
    def __aix_add__(self,anotherObj):return None
    def __wasi_add__(self,anotherObj):return None
    def __freebsd_add__(self,anotherObj):return None


    def __sub__(self, anotherObj):
        pass
    def __mul__(self, anotherObj):
        pass
    def __matmul__(self, anotherObj):
        pass
    def __truediv__(self, anotherObj):
        pass
    def __floordiv__(self, anotherObj):
        pass

    def __lt__(self, anotherObj):
        pass
    def __le__(self, anotherObj):
        pass
    def __eq__(self, anotherObj):
        pass
    def __ne__(self, anotherObj):
        pass
    def __gt__(self, anotherObj):
        pass
    def __ge__(self, anotherObj):
        pass


    def __str__(self):
        return self.__str_func__()
    
    def __win32_str__(self):raise NotImplementedError("win32 str dunder function has not been Implemented yet")
    def __darwin_str__(self):raise NotImplementedError("darwin str dunder function has not been Implemented yet")
    def __linux_str__(self):raise NotImplementedError("linux str dunder function has not been Implemented yet")
    def __cygwin_str__(self):raise NotImplementedError("cygwin str dunder function has not been Implemented yet")
    def __emscripten_str__(self):raise NotImplementedError("emscripten str dunder function has not been Implemented yet")
    def __aix_str__(self):raise NotImplementedError("aix str dunder function has not been Implemented yet")
    def __wasi_str__(self):raise NotImplementedError("wasi str dunder function has not been Implemented yet")
    def __freebsd_str__(self):raise NotImplementedError("freebsd str dunder function has not been Implemented yet")

    def __repr__(self):
        pass
    
    def __win32_repr__(self):raise NotImplementedError("win32 repr dunder function has not been Implemented yet")
    def __darwin_repr__(self):raise NotImplementedError("darwin repr dunder function has not been Implemented yet")
    def __linux_repr__(self):raise NotImplementedError("linux repr dunder function has not been Implemented yet")
    def __cygwin_repr__(self):raise NotImplementedError("cygwin repr dunder function has not been Implemented yet")
    def __emscripten_repr__(self):raise NotImplementedError("emscripten repr dunder function has not been Implemented yet")
    def __aix_repr__(self):raise NotImplementedError("aix repr dunder function has not been Implemented yet")
    def __wasi_repr__(self):raise NotImplementedError("wasi repr dunder function has not been Implemented yet")
    def __freebsd_repr__(self):raise NotImplementedError("freebsd repr dunder function has not been Implemented yet")
class PlatformFunction:
    def __init__(self):
        self.func = None
        if platform.startswith("win32"):self.func = self.__win32__
        elif platform.startswith("darwin"):self.func = self.__darwin__
        elif platform.startswith("linux"):self.func = self.__linux__
        elif platform.startswith("cygwin"):self.func = self.__cygwin__
        elif platform.startswith("emscripten"):self.func = self.__emscripten__
        elif platform.startswith("aix"):self.func = self.__aix__
        elif platform.startswith("wasi"):self.func = self.__wasi__
        elif platform.startswith('freebsd'):self.func = self.__freebsd__
    def __win32__(self, *args,**kwargs):raise NotImplementedError("win32 function body has not been Implemented yet")
    def __darwin__(self, *args,**kwargs):raise NotImplementedError("darwin function body has not been Implemented yet")
    def __linux__(self, *args,**kwargs):raise NotImplementedError("linux function body has not been Implemented yet")
    def __cygwin__(self, *args,**kwargs):raise NotImplementedError("cygwin function body has not been Implemented yet")
    def __emscripten__(self, *args,**kwargs):raise NotImplementedError("emscripten function body has not been Implemented yet")
    def __aix__(self, *args,**kwargs):raise NotImplementedError("aix function body has not been Implemented yet")
    def __wasi__(self, *args,**kwargs):raise NotImplementedError("wasi function body has not been Implemented yet")
    def __freebsd__(self, *args,**kwargs):raise NotImplementedError("freebsd function body has not been Implemented yet")
    def __call__(self, *args,**kwargs):
        return self.func(*args,**kwargs)
