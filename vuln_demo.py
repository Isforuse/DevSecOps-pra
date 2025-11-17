import yaml
import subprocess
import hashlib

def bad1():
    eval("print('Hello')")

def bad2():
    yaml.load("foo")  # unsafe load

def bad3(cmd):
    subprocess.call(cmd, shell=True)

def bad4(pwd):
    hashlib.md5(pwd.encode()).hexdigest()

bad1()
bad2()
bad3("ls; rm -rf /")
bad4("mypassword")
