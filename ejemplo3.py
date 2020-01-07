"""
    @reroes
    # Decoradores
"""

def decorador(f):
    def la_funcion(*args, **kwargs): # convención
        print(args)
        for i, arg in enumerate(args[0]):
            print("argumento %d : valor %d" % (i, arg))
        return f(*args, **kwargs)
    return la_funcion 

@decorador
def sumar_lista(lista):
    return sum(lista)

print(sumar_lista([10, 20, 30]))
