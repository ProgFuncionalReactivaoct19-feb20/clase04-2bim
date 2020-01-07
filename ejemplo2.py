"""
    @reroes
    # Decoradore
"""

def decorador(f):
    def la_funcion(*args, **kwargs):
        print("---------------")
        return f(*args, **kwargs)
    return la_funcion 

@decorador
def saludo():
    return "Hola Mundo"

print(saludo())
