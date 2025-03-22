# Humans Library
a Python collection of biblical rkhumans and their family relations.
<br>
Please note, this is the source code of version 0.0.1, which is the starter file for my "Create Python Package" tutorial on YouTube:
<br>
https://youtu.be/9Ii34WheBOA

## Quickstart
the library provides different scopes of information

### Father Objects
a set of classes that represent biblical fathers, such as Abraham, Isaac and Jacob.

```
import rkhumans

abraham = rkhumans.Abraham()
print(abraham.__dict__)
```
### List of Humans
on a broader scope, the library traces different categories of rkhumans, such as fathers, mothers and children.
```
import rkhumans

all_mothers = rkhumans.mothers
print(all_mothers)
```
