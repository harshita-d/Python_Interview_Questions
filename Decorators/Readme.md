# Decorators

## what is decorators

- A Decorator is a callable, which takes another function as its argumet, wraps its behavior in some way, and returns a new callable.
- A decorator is a python function that modifies the behavior of the other function and class without modifying the structure of original function.
- we apply decorator with `@[decorator_name]` above function
- when the module is loaded the python transforms the decorator as
  ```python
  @decorator
  def greet(name):
      print("hello")
  ```
  into the below
  ```python
  def greet(name):
      print("hello")
  greet = decorator(greet)
  ```

## Forwarding Arguments in Decorators with \*args and \*\*kwargs

- when we wrap a function that itself takes an argument, the wrapper needs to accept nd forward those arguments so that nothing gets lost in the decoration.
- for this `*args, **kwargs` are used
  ```python
  def decorator(fun):
    def wrapper(*args, **kwargs):
        print("decorator start")
        res= func(*args, **kwargs)
        print("decorator name")
        return res
    return wrapper

  @decorator
  def greet(name):
    print(f'hello {name}')
  greet("hrs")
  ```

## multiple decorators

- 