def normalization():
    print("Normalizing the data")

def normalization2(a,b):
    print("Normalizing2 the data"+str(a+b))

# print("hello") # This will execute if you call modules from someother script

# Written generally to test the current file, if this was written outside, any imports would execute them as well
if __name__ == "__main__": # To let the developer test his own code example `python modules.py`
    print(2+3)
    normalization2(2,4)

