# Variables in Python

## Why use variables?
<br>
Let's say that you are writting a story in python and you want to change the name or age of the character.

```python

print("This is a story about a person named Sam")
print("Sam is 16 years old")
print("Sam is a good person")
print("Sam needs to go to the grocery store")
print("At the grocery store Sam goes to buy some food")

```

In the example above, we have a story with a character named Sam. Let's say that you have to change the name of the character or the age of the character.  Doing that by hand would take a while and using search and replace would be a pain.  Instead, we can use variables to store that name and age. Using variables is a lot easier and much more efficient.  It would look something like this:

```python
# quick note about the str(age) function)
# str(age) converts the integer 'age' to a string
# without it, the program would crash
# we will talk about this later

name = "Sam"
age = 16
print("This is a story about a person named " + name)
print(name + " is " + str(age) + " years old")
print(name + " is a good person")
print(name + " needs to go to the grocery store")
print("at the grocery store " + name + " goes to buy some food")
```

Instead of changing every individual line of code, we can just change the variable.  This is much easier and much more efficient.


## Variables in Python
Variables in any programming language are a key part of any programming.  They allow you to store a value in a variable and then use that value later.  In Python, variables are created using the `=` symbol.  For example:

```python
x = 5
# x is now 5
print(x)
# output: 5

test = "Hello"
print(test)
# output: Hello
```
<br>

Note that in the example above, instead of putting quotation marks around test (which would make it a string), we put the name of the variable down to print the value of the variable.  This is because Python will automatically convert the variable to a string.  If you want to store a string in a variable, you can use quotation marks around the variable name as shown in the example above.

<br>

Variables can also change their value while the program is running.  For example:

```python
x = 5
x = x + 1
print(x)
# output: 6
```

<br>

In the example above, we add 1 to the value of x.  This is because Python is a dynamic language.  This means that the value of x can change at any time.  This is why we can add 1 to the value of x.

<br>

## Standard Naming Patterns

In most languages, there are standard conventions and patterns to naming variables.  This is so code is easy to read and understand when working with others.  According to the Python documentation, *"Function names should be lowercase, with words separated by underscores as necessary to improve readability.  Variable names follow the same convention as function names."*  This convention is known as snake case.  This means that the variable name should be lowercase and separated by underscores.  For example:
```python
# this is the correct way to name a variable
character_name = "Sam"
character_age = 16
y_pos = 0
x_pos = 0
age = 16
```
While it is not strictly necessary to follow these conventions to the letter, it is a good idea to follow them to the best of your ability.  
For more information on standard conventions, see the [Python documentation](https://www.python.org/dev/peps/pep-0008/#prescriptive-naming-conventions).
<br>


## Common Errors With Variables

Learning how variables work at first can be complex and confusing.  There are a few common errors that can make it difficult to use variables.  The following are some of the most common errors that can make it difficult to use variables.

<br>

Variables cannot be used until they are defined.  For example:

```python
# this will not work
print(x)
```
Since x is not defined yet in the program, Python will not know what to do with it.  This is why we need to define the variable before we can use it.  For example, this will also not work since x is not defined yet in the program:

```python
print(x)
x = 5
```
<br>

It is important to keep the case of the variable name the same as the variable name.  For example:

```python
num_apples = 5
num_apples = num_Apples + 1
```

Since x is lowercased when we defined it, we need to make sure that the variable name is lowercased as well.  `num_apples` and `num_Apples` are not the same variable.  This is why we need to make sure that the variable name is spelt exactly the same when using it 

<br>


We will talk about variables and using them in math equations in the next section.
