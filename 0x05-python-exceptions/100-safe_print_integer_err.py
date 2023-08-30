import sys
#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}\n".format(value), end="")
        return True
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return False
