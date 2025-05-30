# Python General Questions

## 1. What is meant by callable functions

- An object is callable if it can use the function-call syntax on it like `obj()` which under the hood calls `obj.__call__()`.
-  all regular `functions`, `classes`, `methods` and `instances` implement `__call__`.
    ### Q1. in classes do we need to define __call__ functions or its implicitly defined?
    - By default, classes themselves are callable because their meta classes  provides a `__call__` 
    - however, instances of the class are **not** callable unless explicitly define a `__call__` method in the class.

    ``` python
    class A:
        pass
    class B:
        def __call__(self):
            print("***callable***")
    print("callable(A)",callable(A))
    print("callable(B)",callable(B))
    a=A()
    b=B()
    print("callable(a)",callable(a))
    print("callable(b)",callable(b))
    b()
    a()
    """
    callable(A) True
    callable(B) True
    callable(a) False
    callable(b) True
    ***callable***
    ERROR!
    Traceback (most recent call last):
    File "<main.py>", line 13, in <module>
    TypeError: 'A' object is not callable
    """
    ``` 

## 2. Self