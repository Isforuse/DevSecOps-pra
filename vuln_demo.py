import yaml
import subprocess

def bad():
    yaml.load("dangerous", Loader=yaml.Loader)
    subprocess.call("rm -rf /", shell=True)
    eval("print('bad')")
