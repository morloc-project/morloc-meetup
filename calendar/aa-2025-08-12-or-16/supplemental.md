---
title: "Morloc Meetup #1 - principles"
author: ""
date: "2025-08-12"
---
######
######

# Morloc Meetup #1: Practical Morloc in the Shell - principles
Aug 12, 2025

---

## Morloc Principles

 1. Foreign code should be independent and idiomatic
    * No Morloc library imports
    * No Morloc-specific syntax
    * Code is useable elsewhere, no lock-in
    * natural data types
    * natural naming conventions
    * standard packaging organization (e.g., R code in R packages)

*Write foreign code as you normally would*

```
~~~pygmentize -l python
# This is all that is needed on the foreign side:
def mean(xs : list[float]) -> float:
    return sum(xs) / len(xs)
~~~
```

---

## Morloc Principles

 1. Foreign code should be independent and idiomatic
 2. Invisible interop

    * Foreign code is not responsible for data marshalling 
    * The compiler handles all serialization
    * The user only specifies how complex types are simplified

*Compose functions across languages as easily as within languages*

---

## Morloc Principles

 1. Foreign code should be independent and idiomatic
 2. Invisible interop
 3. Logically equivalent functions should be substitutable
    * Functions may be substituted across languages
    * Substitution should never effect final results

---

## Morloc Principles

 1. Foreign code should be independent and idiomatic
 2. Invisible interop
 3. Logically equivalent functions should be substitutable
 4. No performance compromises
    * Native compositions should have zero overhead
    * Foreign call overhead should be close to the data refactoring cost
    * Distributed computing should be simple
