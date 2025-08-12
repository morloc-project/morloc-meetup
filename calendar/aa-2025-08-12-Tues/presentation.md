---
title: "Morloc Meetup #1"
author: ""
date: "2025-08-12"
#paging: ""
# theme: "glamour.json"
---
######
######

# Morloc Meetup #1: Practical Morloc in the Shell
Aug 12, 2025

---

## Purpose of Morloc

*Morloc is programming language that composes functions across languages under a common type system*

---

## Purpose of Morloc

*Morloc is a means to organize, describe, and compose functions*

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

<!-- ---                                                                         -->
<!--                                                                             -->
<!-- ## Morloc Principles                                                        -->
<!--                                                                             -->
<!--  1. Foreign code should be independent and idiomatic                        -->
<!--  2. Invisible interop                                                       -->
<!--  3. Logically equivalent functions should be substitutable                  -->
<!--  4. No performance compromises                                              -->
<!--  5. Builds must be reproducible and verifiable (no compiler AI)             -->
<!--     * The core Morloc compiler will always be classical                     -->
<!--     * In theory, AI could generate binaries directly from the Morloc code   -->
<!--     * *I have a long off-topic argument for why AI should not be compilers* -->

---

## Meetup focus: practical use of Morloc in CLI tooling

 * (Week 1) Build light-weight, composable CLI tools

 * (Week 2) Configure and specialize tools

 * (Week 3) Fancy data: binary, tables, matrices, and tensors

 * (Week 4) Morloc as a workflow language (job submission, caching etc)


---

## Basic plan
 
 * Meet for four weeks in this series (may start new series afterwards)

### My roles

 * present a new demo every week

 * walk through the code and explain new ideas

 * answer questions and guide discussions

---

## Basic plan
 
 * Meet for four weeks in this series (may start new series afterwards)

### Your roles

 * be critical (ask why)
 * be patient (Morloc is in beta, there are lots of sharp edges)
 * let me know if you find bugs, including:
   * unexpected behavior (normal bugs)
   * poorly documented features
   * bad error messages
   * anything that is more harder than it ought to be 
 * share your work

---

## Today's agenda

 * Explore three simple CLI tools
 * Compose them together to make one tool
 * In the following weeks we'll build on this tool

---
