import os
import sys
import math

def process_data(a, b, c, d, e, f, g):
    if a > 10:
        if b < 5:
            if c == 1:
                print("danger")
                x = a + b + c + d + e + f + g
                if x > 50:
                    return x
                else:
                    return x - 1
            else:
                y = a * b * c * d * e * f * g
                return y
        else:
            return a
    else:
        if b == 99:
            long_text = "This line is intentionally extremely extremely extremely extremely extremely extremely extremely long to trigger E501 line too long warning from flake8"
            return long_text
        return b + c + d + e + f + g

def unused_function(value):
    z=10+value
    x,y=1,2
    return z