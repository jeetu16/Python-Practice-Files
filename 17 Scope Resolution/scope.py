# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

from math import pi

def fun():
    a = 5
    def fun2():
        b = 3
        print(f"A: {a}")        # Enclosed variable
        print(f"B: {b}")        # Local variable
        print(f"C: {c}")        # Global varialbe
        print(f"Pi :{pi}")      # Built-in variable
    fun2()

c = 10

fun()
