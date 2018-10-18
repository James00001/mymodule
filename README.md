## A test case for an import problem I am having

(October 10 2018)

Hi there! I often find myself writing python 3 relative imports that look like this:

```python
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
```

This code example works as intended, I can do both of the following:

```
[username@localhost mymodule]# python3.6 mymodule/main.py
The .otherfile import failed
The otherfile import worked
Hello World?
```

```
[username@localhost mymodule]# python3.6
Python 3.6.5 (default, Apr 10 2018, 17:08:37)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-16)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import mymodule
The .otherfile import worked
>>> mymodule.run_me()
Hello World?
>>>
```

And my imported function runs in both cases, but I can't help but think I am doing my import wrong somehow. There must be a way to do a simple relative import that works properly for both pip installed code and code that I run directly.

And if I just try a plain `from otherfile import some_func` it works fine for `python3.6 mymodule/main.py` but when i try it from the pip installed module, I get:

```
[username@localhost mymodule]# python3.6
Python 3.6.5 (default, Apr 10 2018, 17:08:37)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-16)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import mymodule
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/testuser/src/mymodule/mymodule/__init__.py", line 1, in <module>
    from .main import run_me
  File "/home/testuser/src/mymodule/mymodule/main.py", line 3, in <module>
    from otherfile import some_func
ModuleNotFoundError: No module named 'otherfile'
```
