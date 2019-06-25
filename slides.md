#### Charming The Snake <br/> Python For System Admins

##### Tony Williams <br/> Systems Engineer

Please download https://bit.ly/xw19-python

### What We Will Talk About

- Simple types
- Lists
- IPython
- Dictionaries
- Conditionals
- Looping
- Functions
- Standard modules
	- Subprocess
	- os and paths
- Requests
- plistlib

### Numbers

The interpreter acts as a simple calculator: you can type an expression 
in it and it will write the value. Expression syntax is straightforward: 
the operators +, -, * and / work just like in most other languages 
(for example, Pascal or C); parentheses (()) can be used for grouping. 

For example:


``` python
>>> 2 + 2
4
>>> 50 - 5 * 6
20
>>> (50 - 5) * 6
270
```

<div class="notes">
Notice that numbers are not enclosed by quotes or anything else. 
</div>

### Numbers

```
8 / 5
8 % 5
8 / 5.0
8 / 2.0
round(8/5.0)
int(round(8/5.0))
type(5)
type(5.0)
```

<div class="notes">
Let's work through these examples. To start, there are two sorts of numbers, integers
and floating point, with a decimal point. The percent sign is the mod operator. The
result of any operation with a floating point number is always a floating point number.
The function `type` returns the type of a number.
</div>

### More Numbers

The equal sign (=) is used to assign a value to a variable. Afterwards,
no result is displayed before the next interactive prompt.

``` python
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
```

If a variable is not “defined” (assigned a value), trying to use it will
give you an error:

``` python
>>>
>>> n  # try to access an undefined variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
```

### Lists and iteration

``` python
a_list = [1, 2, 3, 45]
a_list[0]
a_list[-1]
a_list[1:3]

for item in a_list:
    print(item)

mixed = [4, "Tony's", 3.14, True, 'bees']
for thing in mixed:
    print (thing, type(thing))

show = 'My quote has it\'s text: "strings are good"'
print(show)
show2 = "My quote has it's text: \"strings are good\""
print(show2)
```

<div class="notes">
Lists are a way of collecting values together. Notice that the first value in the
list is number zero. You can count from the end using minus numbers and the colon
operator allows you to "slice" the list.

A note here on strings - strings are any text enclosed in quotes. You can actually use
either single or double quotes to surround them. If you need to use a quote in a string
you can escape it with a backslash.
</div>

### Starting IPython

| command            | description                                       |
|:-------------------|:--------------------------------------------------| 
| ipython            | run IPython                                       |
| jupyter qtconsole  | runs ipython in QT window                         |
| jupyter notebook   | runs the IPython notebook server                  |
| ipython --help     | IPython man page                                  |

<div class="notes">
At this point let's move on to a better Python interpreter - IPython.

IPython has sort of been renamed Jupyter, so we use the jupyter name for
some functions.
</div>

### Dictionaries

```python
staff_ids = {'Alice': 312, 'Ted': 519, 'Carol': 781}

staff_ids['Ted']

for key in staff_ids:
    print(staff_ids[key])
    
staff_ids['Ted'] = 783

for key in staff_ids:
    print (key, staff_ids[key])
    
hgttg = {'Life': True, 'Meaning': 42, 'Motto': "Don't Panic"}
print(hgttg["Meaning"])
```

<div class="notes">
Our final type are dictionaries.
- A key and a value (think of a plist)
- Surrounded by "{}"
- Unordered
- keys
    - Case sensitive
    - Unique
    - New value overwrites
</div>

### Conditionals

``` python
num = 4

if num == 4:
    print("Four")

if num > 4:
    print("Huge")
else:
    print("Not huge")

if num > 3:
    print("Biggest")
elif num > 2:
    print("Big")
else:
    print("Small")

```

<div class="notes">
Conditionals are where we can make decisions. As you can you can make
complex decisions. One thing to note is that unlike some other languages Python
does not have a a case statemtn.
</div>

### More Loops

``` python
tm = 1
while tm <= 10:
    print(tm)
    tm = tm + 1
```

``` python
for x in range(1,11):
    print(x)
```

<div class="notes">
A "while" loop will loop until a condition becomes false. A "for" loop loops
across a range of values.
</div>

### Iterating

``` python
collection = ['hey', 5, 'd']
for x in collection:
    print(x)
```

```python
[print(i) for i in collection]
```

``` python
list_of_lists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list in list_of_lists:
    for x in list:
        print(x)
```
<div class="notes">
We saw looping over a  list earlier. Here we see the same thing done with
what's called a list comprehension. Finally, we see how to iterate over a list
of lists.
</div>

### Functions

- Use `def` keyword
- May use `return` keyword

``` python
def hello_world():
    print("Hello World!")
    
hello_world()
```

``` python
def times_two(x):
    return x * 2
    
times_two(21)
```

### Running Commands

Call external system commands

```python
import subprocess

cmd = ['find', '/usr', '-iname', 'zip-*']
subprocess.run(cmd)
ret = subprocess.run(cmd, capture_output=True)

ret.stdout
ret.stderr
ret.returncode
```

<div class="notes">
If we want to run a CLI command we can do that with the subprocess module.
A module is a collection of Python functions that perform a set of tasks. Python
includes a number of modules in a it's standard library and subprocess is one.
subprocess.run returns an *object* and the object has properties.

Also notice that we are using a *named* parameter in the second subprocess call
</div>

### More Subprocess

```python
out = subprocess.check_output(['ls'])
out

out = subprocess.check_output(['find', 'shjsd'])

try:
    out = subprocess.check_output(['find', 'shjsd'])
except subprocess.CalledProcessError as CP_err:
    print("Error in find: %d" % CP_err.returncode)
```

<div class="notes">
There is a function that will just return stdout. It does have one drawback that you
need to be aware of. When Python gets an error it performs something we call raising
an exception and we should handle this if we use it.

</div>

### Joining Paths

```python
import os
plugin_path = os.path.join("/", "Library", "Internet Plug-Ins")
print(plugin_path)
```

#### Manipulating Paths

```python
from os import path
path.basename(plugin_path)
path.dirname(plugin_path)
path.splitext("com.apple.Safari.plist")
```

<div class="notes">
Let's have a look at using the `os` library on paths and files. Notice in the second
block I am using a different form of `import`. Here we are importing just one object
from the `os` module.
</div>

### Tests on Files

```python
who

from os.path import *
who

exists(plugin_path)
isdir(plugin_path)
islink("/etc")
```
<div class="notes">
We can also perform tests on a file. Notice a third form of import. If we run the
IPython command `who` it lists our entire namespace. If we use our new form of import
we get every member of os.path. This makes the function calls shorter but we have
to be careful as you can confuse things if you import too many names.
</div>

#### glob

```python
import glob
ess = glob.glob("/Applications/Utilities/" "S*.app")
print(ess)

```

<div class="notes">
- Equivalent to shell globbing 
- Returns matching path(s) as a list
- glob uses the fnmatch module
</div>

### Requests

```python
import requests
url = 'https://icanhazdadjoke.com/'
r = requests(url)
r.status_code
r.text
r.headers
```

```python
headers = {'Accept': 'text/plain'}
r = requests.get(url, headers=headers)
r.text
```

<div class="notes">
If we want to talk to a web server there is another module we can use ,`requests`.
We can even set the headers for our request easily.
</div>

### JSON

```python
headers = {'Accept': 'application/json'}
r = requests.get(url, headers=headers)
r.text
r.json()
r.json()['joke']
```

#### Queries

```python
url = 'https://api.openbrewerydb.org/breweries?by_city=new_york'
r = requests(url)
r.json()
for brewery in r.json():
    print(brewery['name'], "Street: ", brewery['street'])
url = 'https://api.openbrewerydb.org/breweries'
query = {'by_city': 'new_york'}
r = requests.get(url, params=query)
r.json()
r.url

```
<div class="notes">
Because JSON is becoming something of a standard for an API to return requests has
built-in JSON handling.

We can also get requests to assemble the URL of a query or other parameter.
</div>

### Bigger Queries

```python
query = {'by_city': 'williamsburg'}
r = requests.get(url, params=query)
len(r.json())
query = {'by_city': 'williamsburg', 'by_state': 'virginia'}
r = requests.get(url, params=query)
len(r.json())
r.url
```

<div class="notes">
And our query can be complex and requests does the right thing.
</div>

### plistlib

```python
import plistlib
prefs = {'fname': 'Tony', 'sname': 'Williams'}
fp = open('example.plist', 'wb')
plistlib.dump(prop, fp)
fp.close()
```

```python
with open('example.plist', 'rb') as fd:
	pl = plistlib.load(fd)
    print(pl['fname'])
    
pl['fname'] = 'Anthony'

with open('example.plist', 'rb') as fd:
	plist.dump(pl, fd)

```

<div class="notes">
There is another library specifically for talking to preference or plist files. Let's
start by creating a plist file.

Now we can read it. We can also change an item then write it back.
</div>

### XML

```python
auth=('xworld', 'passwd')
base_url=('https://twxworld.jamfcloud.com/JSSResource/')
url = base_url + 'categories'
cat = requests.get(url, auth=auth)
cat.text
cat.xml

import xml.etree.ElementTree as ET
root = ET.fromstring(cat.text)
categories = root.findall('category')
for i in categories:
	print(i.find('id').text, i.find('name').text)
```
<div class="notes">
Now we have a more complex requests call. requests doesn't handle XML internally so
we use another module, Elementree. 
</div>

### PUT and POST With Requests

```	
url = base_url + 'categories/id/3'
cat = requests.get(url, auth=auth)
root = ET.fromstring(cat.text)
root.find('name').text
root.find('name').text = "Changed"

new = ET.tostring(root)
ret = requests.put(url, auth=auth, data=new)
ret.status_code
ret.text

root.find('name').text = 'Inserted'
root.find('id').text = '0'
new = ET.tostring(root)
url = base_url + 'categories/id/0'
ret = requests.post(url, auth=auth, data=new)
ret.status_code
ret.text

```
<div class="notes">
</div>

### Further Places

- [Dive Into Python 3](http://www.diveintopython3.net) - A good tutorial for experienced programmers
- [A Byte of Python](https://python.swaroopch.com) - Good tutorial for beginners
- [A Byte of Python PDF](https://legacy.gitbook.com/book/swaroopch/byte-of-python/details) - The above as a PDF
- [Python for NonProgrammers](https://wiki.python.org/moin/BeginnersGuide/NonProgrammers) - An exhaustive list
