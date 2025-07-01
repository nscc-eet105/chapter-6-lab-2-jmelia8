#Joe Melia EET-107
import matplotlib.pyplot as plt

def main():
    print("This program will graph a line when given the slope and the intercept.")
    print("Please enter the values for m and b given the form y = mx + b")
    m = int(input("m: "))
    b = int(input("b: "))
    graph(m, b)

def graph(m, b):
    Xvalue = [x for x in range(-20, 21)]
    Yvalue = [ m * x + b for x in Xvalue]
    plt.axis('square')
    plt.xlim(-20, 20)
    plt.ylim(-20, 20)
    plt.grid(True)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.plot(Xvalue, Yvalue)
    plt.show()
main()
    
