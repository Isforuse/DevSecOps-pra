import os
import yaml

# Command injection
user = input("Enter command: ")
os.system(user)

# Unsafe YAML
data = yaml.load("foo: bar")

# eval injection
def insecure_eval(code):
    eval(code)

insecure_eval("print('bad')")
