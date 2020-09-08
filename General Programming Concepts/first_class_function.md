
<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Assigning-the-function" data-toc-modified-id="Assigning-the-function-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Assigning the function</a></span></li><li><span><a href="#Passing-the-function-as-argument" data-toc-modified-id="Passing-the-function-as-argument-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Passing the function as argument</a></span></li><li><span><a href="#Returning-function-from-another-function" data-toc-modified-id="Returning-function-from-another-function-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Returning function from another function</a></span><ul class="toc-item"><li><span><a href="#A-useful-example" data-toc-modified-id="A-useful-example-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>A useful example</a></span></li></ul></li><li><span><a href="#Reference" data-toc-modified-id="Reference-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Reference</a></span></li></ul></div>

<br>

In computer science, a programming language is said to have **first-class functions** if it treats functions as first-class citizens. This means the language supports:

- passing functions as arguments to other functions
- returning them as the values from other functions 
- and assigning them to variables or storing them in data structures.

In programming language design, a **first-class citizen** (also type, object, entity, or value) in a given programming language is an entity which supports all the operations generally available to other entities. These operations typically include being passed as an argument, returned from a function, modified, and assigned to a variable.

In languages with first-class functions, the names of functions do not have any special status; they are treated like ordinary variables with a function type.


### Assigning the function


```python
def square(x):
    return x*x

# assigning the return value of function
f1 = square(5)

# assigning the function itself: we don't give the parenthesis as we don't to call/execute the function
f2 = square

print(f1)
print(f2)
print(square)

# now we can use f2 same as function square
print(f2(5))
print(square(5))
```

    25
    <function square at 0x000002A4168990D0>
    <function square at 0x000002A4168990D0>
    25
    25
    

### Passing the function as argument



Classic example of this is built-in *map* function.


```python
# this map function that takes another function and a list as input
# it applies the function on each element of the list and then returns the result

def my_mapper(fns, arr):
    res = [fns(elem) for elem in arr]
    return res


arr = [1,2,3,4,5]

# again, we don't use parenthesis while passing the "square" fns as argument
my_mapper(square, arr)
```




    [1, 4, 9, 16, 25]




```python
# it can also accept lambda functions
my_mapper(lambda x: x**3, arr)
```




    [1, 8, 27, 64, 125]



### Returning function from another function

Useful for logging, decorators


```python
def logger(msg):
    def log_message():
        print('message:', msg)
    
    # no parenthesis as we aren't calling the fns, we are returning it
    return log_message


# at this point log1 is equivalent to log_message as that's what is being returned by logger()
log1 = logger("hello")

# now we call the log_message: hence parenthesis
# the function remembered the variable passed to it: this is concept of Closure
log1() 

```

    message: hello
    


```python
# it doesn't remember past messages..:(
log1 = logger("hello")
log1 = logger("hello world")

log1()
log1()
```

    message: hello world
    message: hello world
    

#### An useful example


```python
def html_tag(tag):
    def wrap_text(text):
        print(f"<{tag}>{text}</{tag}")
    
    # returning the function
    return wrap_text

print_h1 = html_tag("h1")

# will remember the tag with which the function was created
print_h1("Headline")
print_h1("Another Headline")

print_p = html_tag("p")
print_p("A paragraph")
```

    <h1>Headline</h1
    <h1>Another Headline</h1
    <p>A paragraph</p
    

### Reference

https://en.wikipedia.org/wiki/First-class_function

https://www.youtube.com/watch?v=kr0mpwqttM0&ab_channel=CoreySchafer
    



