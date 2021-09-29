"""
Any fool can write code that a computer can understand.
Good programmers write code that humans can understand.
    - Martin Fowler

Clean Code Checklist:
1.  Good names -> why it exists, what it does, and how it is used
2.  Keep it short -> short functions, small files
3.  Functions should do one thing
4.  Write DRY code -> Dont Repeat YOURSELF
5.  Use version control -> https://github.com is your friend

src: https://www.freecodecamp.org/news/clean-coding-for-beginners/
"""

# Closure:
a = 10

def hello():
    b = a
    a = 15

# print(a)
# print(b)

# Structure code in different files:
from library.greeting import *
from library.stringCounters import characterCounter
from library.stringCounters import vocalCounter as vc

greeting("Silvan")
goodbye("Lea")

print(characterCounter("Crown Bar"))
print(vc("How many vocals do I have?"))
