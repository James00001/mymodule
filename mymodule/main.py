# in main.py
try:
    # An import that works if the current module is installed with pip
    from .otherfile import some_func
    print("The .otherfile import worked")
except ImportError:
    # An import that works of I run ./main.py from my source code folder
    print("The .otherfile import failed")
    from otherfile import some_func
    print("The otherfile import worked")

def run_me():
    print("Hello", some_func())

if __name__ == "__main__":
    run_me()
