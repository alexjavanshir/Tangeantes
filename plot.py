import numpy as np
import matplotlib.pyplot as plt
import time

def main():
    x = np.arange(-10, 10, 0.1)
    y1 = x**2
    y2 = 3*x**2+50

    f, ax = plt.subplots(1)
    plt.title("Function")
    plt.xlabel("Values of x")
    plt.ylabel("Values of y")

    ax.plot(x, y1)
    plt.wait
    ax.plot(x, y2)

    plt.show()


if __name__ == "__main__":
    main()