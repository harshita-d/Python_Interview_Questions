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

## multiple decorators

- multiple decorators can be applied by stacking them on top of the function and the implementation goes from bottom to up

  ```python
  def decorator1(func):
      ...
  def decorator2(func):
      ...

  @decorator1
  @decorator2
  def greet(name):
      print(f'hello {name}')
  greet("hrs")
  ```

## Function Decorators

### Forwarding Arguments in functional Decorators with \*args and \*\*kwargs

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

### functional Decorator with arguments

- If an argument is send to a decorator than we need to add one more function layer
- `outer function` takes the decorator arguments and return
- `inner function` accepts the function to wrap and return
- `wrapper` that arguments the function behaviour
  ```python
  def decorator_outer(n):
      def decorator_inner(func):
          def wrapper(*args, **kwargs):
              print(f"n: {n}")
              print(f"args {args}")
              res=func(*args,**kwargs)
              return res
          return wrapper
      return decorator_inner
  @decorator(3)
  def greet(name):
      print(f"hello {name}")
  greet("hrs")
  ```

### functools.wraps

- when we apply decorator to a function than original functions meta data like function name, docstring, etc are lost
- this happens because the decorator typically replaces the original function with a new function
- the original function does not inherit the meta data
- for this we use `@functools.wraps`

  ```python
  import functools
  def decorator(func):
      @functools.wraps(func)
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
  print(greet.__name__) # with functool.wraps it give "wrapper"
  ```

## class Decorators

- its instances are used to wrap another callable
- it has two parts:

  - `__init__(self, func)`: It receives the func/class being decorated and stores it on self.
  - `__call__(self, *args, **kwargs)`: makes the instance istelf callable. This method is invoked whenever the decorated function is called.

  ```python
  import functools
  class class_decorator:
      def __init__(self, func):
          functools.wraps(func)(self)
          self.func=func
      def __call__(self, *args, **kwargs):
          print("=====")
          res=self.func(*args, **kwargs)
          return res

  @class_decorator
  def greet(name):
      print(f"hello {name}")
  greet("hrs")
  ```

### flow chart for the above

```python
  1. Decorator Definition Phase (During Module Load / Decoration)
  ───────────────────────────────────────────────────────────────
  @MyDecorator
  def greet(name):
      print(f"Hello, {name}")
  ↓
  Python evaluates:
  greet = MyDecorator(greet)
          │
          └───> __init__(self, fn)
              ├─ self.fn = fn         ← store original function
              ├─ (optional) functools.wraps(fn)(self)
              └─ returns instance of MyDecorator
  Final result:
  greet → instance of MyDecorator

  2. Function Call Phase (Runtime when greet("Alice") is called)
  ───────────────────────────────────────────────────────────────
  greet("Alice")
  │
  └───> MyDecorator.__call__(self, "Alice")
      ├─ print("[MyDecorator] Before calling greet")
      ├─ self.fn("Alice")   ← call original greet function
      │     └───> def greet(name):
      │               print(f"Hello, {name}")
      │           ↓ Output: Hello, Alice
      ├─ print("[MyDecorator] After calling greet")
      └─ return result of self.fn("Alice") → (None in this case)

  3. Output
  ──────────────────────
  [MyDecorator] Before calling greet
  Hello, Alice
  [MyDecorator] After calling greet
```

### class decorator without arguments

- In this case the `__init__` gets the function

  ```python
    Step 1: greet = MyDecorator(greet)     → __init__(self, fn=greet)
    Step 2: greet("Alice")                 → __call__(self, "Alice")
  ```

### class decorators with arguments

- For class decorators to accept its own arguments the class itself is treated as decorator factory

  ```python
  | Decorator Style | **init** gets...        | **call** gets...          | Do you need a nested "wrapper"         |
  | --------------- | ----------------------- | ------------------------- | -------------------------------------- |
  | **Non-param d** | the target function     | the call args ("*args")   | No — "__call__" *is* the wrapper       |
  | **Param d**     | your decorator params   | the target function       | Yes — "__call__" returns a "wrapper"   |
  ```

- `__init__` takes the decorator arguments and stores them on self
- `__call__` is invoked once with the function to wrap
- `__call__` cannot be used as wrapper in parameterized class decorator because `__init__` does not receive the function, it only receives the decorator arguments.
- We must return a separate wrappper function from `__call__`
- This is beacuse with arguments, python evaluates `@decorator(arg1, arg2)` as
  ```python
  decorator_instance=decorator(args1, args2)
  function=decorator_instance(function)
  ```
  ```pyhton
    temp = MyDecorator("foo")        # __init__("foo")
    greet = temp(greet)              # __call__(fn)
  ```
- therefore in this case `__init__` gets the arguments and not the function
- the function is only available only after the `__call__`

    ```python
    class class_decorator:
        def __init__(self, n):
            self.times=n
        def __call__(self, func):
            def wrapper(*args, **kwargs):
                print(f"n: {self.times}")
                res=func(*args, *kwargs)
                return res
            return wrapper

    @class_decorator(3)
    def greet(name):
        print(f"hello {name}")
    greet("hrs")
    ```

## What is difference between class decorator and function decorator

### 1. function based

-

### 2. class based
