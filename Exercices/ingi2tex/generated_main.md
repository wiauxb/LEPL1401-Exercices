---
title: "LEPL1401 exercices"
authors:Robin Verschuren,Bastien Wiaux
date: January 2019
output:
  pdf_document:
    toc: true
    number_sections: true
    highlight: pygments
---

# Introduction

# Session 1

## Median

Énoncé disponible via [ce lien](https://inginious.info.ucl.ac.be/course/LSINF1101-PYTHON/Median)

#### Implémentation {-}
```python
if (a>=b and a<=c) or (a>=c and a<=b):
    median = a
elif (b>=a and b<=c) or (b>=c and b<=a):
    median = b
else:
    median = c


```

#### Implémentation {-}
```python
print("test902883")
print("hih")

```


## QBF

Énoncé disponible via [ce lien](https://inginious.info.ucl.ac.be/course/LSINF1101-PYTHON/QBF01)

#### Implémentation {-}
```python
print(s0)
while s0 != 1:
    if s0%2 == 0:
        s0 =int(s0/2)
    else:
        s0 = 3*s0+1
    print(s0)

```

