# vuln_demo.py

import os
import subprocess

# 任意命令執行
user_input = "ls; rm -rf /"
os.system(user_input)

# SQL injection pattern
query = "SELECT * FROM users WHERE id = " + user_input

# Hardcoded secret
API_KEY = "12345-SECRET"

# Dangerous eval
dangerous = "1+2"
print(eval(dangerous))
