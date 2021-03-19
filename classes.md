# Classes in Python

A Class is similar to an object constructor, a sort of blueprint for creating objects.

Data values within an object are called _attributes_ and functions within the class are called _methods_.

## Table of Contents

- [Creating a Class](#creating-a-class)
  - [The init function](#the-init-function)
  - [self](#self)
  - [Pass statement](#pass-statement)
  - [Deleting object properties](#deleting-object-properties)
  - [Modifying object properties](#modifying-object-properties)
- [Getters and Setters](#getters-and-setters)
  - [@ property](#property)
- [Inheritance](#inheritance)
  - [Overriding](#overriding)
  - [Adding method to a child](#adding-methods-to-the-child)
  - [Useful in-built functions](#useful-in-built-functions)
- [References](#references)
- [Possible Extensions](#possible-extensions)

## Creating a Class

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def introduction(self):
    print("Hello my name is " + self.name)

p1 = Person("Laura", 54)

print(p1.name) # prints Laura
p1.introduction # prints Hello my name is Laura
```

The code above creates a class called Person, with two properties, name and age, and one method defined as introduction.

It is convention for the first letter of a class to be capitalised. A style guide can be found in the references below.

### The init function

Init is most likely a shorthand for initialisation. The `__init__()` function is called automatically every time the class is being used to create a new object (initialised). Use the `__init__()` function to assign values to object properties, or other operations that are necessary to do when the object is being created.

#### Why use an init function?

It allows us to set attributes upon creation, or have a method run when the instance is created.

```python
class Cat:
  def __init__(self, name, owner):
    self.name = name
    self.owner = owner
    self.isAdorable = True

class Duck:
  self.name = None
  self.owner = None
  self.canSwim = True

marge = Cat("Marge", "Claire")

donald = Duck()
donald.name = "Donald"
donald.owner = "Disney"
```

Looking at the example code above, we can see that having a `__init__` function means we can create an object and specify attributes using less lines of code. Also, it is useful in instances where we want a function to run based on what values were submitted in the initialisation.

### self

The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class. For those coming from other languages, it is similar to a `this`. 

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class.

e.g. Use the words mysillyobject and abc instead of self:
```python
class Person:
  def __init__(mysillyobject, name, age = 0):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
```

### Pass statement

class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

```python
class Person:
  pass
```

### Deleting Object Properties

Use the `del` keyword to delete either an attribute, method or the whole instance of the class.

e.g. `del p1.age` or `del p1`

**Interesting fact**: When you create a new object from a class, a new instance object is created in memory and the name (e.g. p1) binds with it. On the command `del p1`, this binding is removed and the name p1 is deleted from the corresponding namespace. The object however continues to exist in memory and if no other name is bound to it, it is later automatically destroyed. This automatic destruction of unreferenced objects in Python is also called *garbage collection*.

### Modifying Object Properties

You can modify an attribute using two ways:
- Directly
  - e.g.  `p1.name = 'Ibrahim'` 
- Using getters and setters
  - more information on this below, however, getters and setters are intermediaries so the attribute is never directly accessed or modified
  - requires the existence of a getter and a setter function resulting in more code

## Getters and Setters

Getters and setters are intermediaries used to access or change an attribute within a class. In object-oriented languages, it is usually used for *data encapsulation*. Also, it is useful for data validation i.e. when we want to make sure only a number is set to a certain attribute. 

### @property

Python's property decorater is an easy way to create getters, setters and a deleter. It is more compact and readable compared to traditional getter setter syntax.

The example below shows us how to use the property decorator and how to access the getter, setter and deleter.

```python
class Person:
  def __init__(self, name, age):
    self._name = name
    self._age = age
  
  @property
  def age(self):
    return self._age
  
  @age.setter
  def age(self, new_age):
    if new_age > self.age and isinstance(new_age, int):
      self._age = new_age
    else:
      print("Please enter a valid age. Age cannot be lower than previous age and must be an integer")
  
  @age.deleter
  def age(self):
    del self._age

human = Person("Candan", "24")
human.age #accesses age attribute
human.age = 30 #sets a new value for age if it fulfils criteria in function
del human.age #deletes the attribute
```

It is convention in Python that adding a leading underscore to the name of something means it is *protected*. By that, we mean that developers should not access or modify this directly; intermediaries (like getters and setters) should be used instead if available.

Check out the references below if you'd like to read more about the property decorator.

#### Arguments against Getters and Setters

Both these articles talk about java and are mainly saying it's not quite following the principles of object-oriented programming
- https://dev.to/scottshipp/avoid-getters-and-setters-whenever-possible-c8m
- https://www.infoworld.com/article/2073723/why-getter-and-setter-methods-are-evil.html

## Inheritance

Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class. Any class can be a parent class, so the syntax is the same as creating any other class.

Child class is the class that inherits from another class, also called derived class. To create a class that inherits the functionality (same properties and methods) from another class, send the parent class as a parameter when creating the child class.

### Overriding

The child's __init__() function overrides the inheritance of the parent's __init__() function.

To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

```python
class Student(Person):
  def __init__(self, fname, lname, year):
    Person.__init__(self, fname, lname)
    self.graduationyear = 2019
```

Another way of writing the code above is by using the `super()` function. This function will make the child class inherit all the methods and properties from its parent. The benefits are you do not have to use the name of the parent element.

```python
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
```

### Adding Methods to the Child

To add a method just define it as you would normally.

If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.

### Useful in-built functions

(Maybe change examples in this section to work with student/person)
Python has two built-in functions that work with inheritance:
- Use `isinstance()` to check an instance’s type: `isinstance(obj, int)` will be `True` only if `obj.__class__ `is int or some class derived from int.
- Use `issubclass()` to check class inheritance: `issubclass(bool, int)` is True since bool is a subclass of int. However, `issubclass(float, int)` is False since float is not a subclass of int.

## References:

1. [Python docs - classes](https://docs.python.org/3/tutorial/classes.html)
2. [Python PEP 8 Standard - naming conventions](https://www.python.org/dev/peps/pep-0008/#id34) PEP 8 is a widely used style guide within the Python community, published by the Python Software Foundation
3. Two summaries of the PEP 8 Standard Naming Conventions
    - [University of Colorado Earth Lab](https://www.earthdatascience.org/courses/intro-to-earth-data-science/write-efficient-python-code/intro-to-clean-code/python-pep-8-style-guide/)
    - [Medium article - 10 Points you should know](https://medium.com/@dasagrivamanu/python-naming-conventions-the-10-points-you-should-know-149a9aa9f8c7)
4. [w3schools - classes](https://www.w3schools.com/python/python_classes.asp)
5. [w3schools - inheritance](https://www.w3schools.com/python/python_inheritance.asp)
6. [Python docs  - property](https://docs.python.org/3/library/functions.html#property)
7. [freeCodeCamp - python property decorator](https://www.freecodecamp.org/news/python-property-decorator/)
8. [3 Types of Python Methods - instance, static, class](https://www.makeuseof.com/tag/python-instance-static-class-methods/)
9. [Programiz python tutorials - easy to read and understand](https://www.programiz.com/python-programming/class)

## Possible extensions

- What are public/private variables
- Advantages of using inheritance
- What are special operators
