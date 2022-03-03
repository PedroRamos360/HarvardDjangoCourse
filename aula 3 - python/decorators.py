# Decorator => uma função que altera a funcionalidade de uma função

def announce(f):
    def wrapper():
        print('about to run the function')
        f()
        print('done with function')
    return wrapper

@announce
def hello():
    print('hello world')

hello()