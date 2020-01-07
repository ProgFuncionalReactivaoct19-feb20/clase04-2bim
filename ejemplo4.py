"""
    @reroes
    # Decoradores
"""

def decorador_int(f):
    def la_funcion(*args, **kwargs): # convención
        assert isinstance(args[0], int)
        return f(*args, **kwargs)
    return la_funcion 

@decorador_int
def presentar_valor(a):
    return a

print(presentar_valor("10"))
