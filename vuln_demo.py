import yaml, subprocess

# ⚠ 1. Insecure YAML load (CVE known)
yaml.load("a: 1")

# ⚠ 2. Command injection risk
subprocess.call("ls " + input("name: "))

# ⚠ 3. Hardcoded credential
password = "123456"
