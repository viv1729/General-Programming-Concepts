- [Definition](#definition)
- [First Class Function](#first-class-function)
- [Simple Closure](#simple-closure)
- [Closure with Parameters](#closure-with-parameters)


## Definition

In programming languages, a **closure**, also **lexical closure** or **function closure**, is a technique for implementing lexically scoped name binding in a language with first-class functions. Operationally, a closure is *a record storing a function* together with an environment.

The environment is a mapping associating each free variable of the function (variables that are used locally, but defined in an enclosing scope) with the value or reference to which the name was bound when the closure was created.

Unlike a plain function, a *closure allows the function to access those captured variables through the closure's copies of their values or references*, even when the function is invoked outside their scope.

In simple terms: 
A closure is an inner function that remembers and has access to variables in the local scope in which it was created (i.e. local scope of outer function) even after the outer function has finished executing.

<br>

## First Class Function


```python
def outer_func():
    message = "Hi"
    
    def inner_func():
        # message is a free variable as it's not actually defined in the inner function but it still has access to it
        print(message)
    
    # executing the inner function as we have given parenthesis
    return inner_func()

```


```python
outer_func()
```

    Hi
    

## Simple Closure


```python
def outer_func():
    message = "Hi"
    
    def inner_func():
        # message is a free variable as it's not actually defined in the inner function but it still has access to it
        print(message)
    
    # return the function w/o executing it
    return inner_func

```


```python
outer_func()
```




    <function __main__.outer_func.<locals>.inner_func()>




```python
# my_func is actually equivalent to inner_func
my_func = outer_func()

print(my_func)
print(my_func.__name__)

# calling the inner function
my_func()
my_func()
```

    <function outer_func.<locals>.inner_func at 0x000001F32BBE8730>
    inner_func
    Hi
    Hi
    

Above, we can see that even after we had finished executing outer_func(), my_func still has access to the variable. This is what we mean by Closure.

A Closure closes over the free variables from their environment.


## Closure with Parameters

```python
def outer_func(msg):
    message = msg
    
    def inner_func():
        # message is a free variable as it's not actually defined in the inner function but it still has access to it
        print(message)
    
    # return the function w/o executing it
    return inner_func

```


```python
hi_func = outer_func('hi')
bye_func = outer_func('hello')

print(hi_func.__name__)
print(bye_func.__name__)
```

    inner_func
    inner_func
    


```python
# again both function remember their the respective value of their free variable
hi_func()
bye_func()
```

    hi
    hello
    

