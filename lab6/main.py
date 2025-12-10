from decorator import repeat

@repeat(5)
def hello():
    print("Hello from decorator!")

hello()
