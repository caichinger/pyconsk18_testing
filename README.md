# Testing Essentials for Scientists and Engineers

**Interactive vs? Test Driven Development**

A PyCon SK 2018 Workshop by [Claus Aichinger](https://2018.pycon.sk/en/speakers/Aichinger.html).

[Feedback Form](https://goo.gl/forms/fBW6Bkeht9bxsC6B3)

If you find any Issues or have ideas for improvment, please to not
hesitate to file an Issue or Pull request, I appreciate your feedback!


## Installation & Setup

Please make sure you have the environment specified in [env.yml](env.yml)
set up prior to the workshop.

If you use [conda](https://conda.io/docs/), you can do

**on Linux**
```
conda env create --file environment.yml
source activate testing
```

**on Windows**
```
conda env create --file environment.yml
activate testing
```

or use your preferred way to create a (virtual) coding environment.

conda is a package and environment manager (like pip and virtualenv
combined), you do not have to use it; but we do require the packages listed
in `environment.yml`.


## Outline

- General introduction
- Useful tools and their application (exercise based)
  - [engarde](http://engarde.readthedocs.org/)
  - [doctest](https://docs.python.org/3/library/doctest.html)
  - [pytest](http://pytest.org/)
- Interactive exploration of a computation problem (live coding, all together)
  - Specification
  - How to approach it?
  - How to devise tests?

## Description

### Goals
**Primary Goal:**
How can I integrate testing in my interactive development process?

**Non-Goal:**
How can I do this or that kind of test or how does this particular feature of
\*test work?

### Motivation
Software testing is an undisputed cornerstone of software development. However,
as I know from my personal experience, Python users with a
non-software-engineering or otherwise scientific background are often not so
familiar with the concept of testing.

Computational problems are regularly approached by means of interactive
development, which is both fast and fun and one of the reasons why Python is so
successful in a wide range of scientific/engineering areas. The widespread
adoption of the [IPython](http://ipython.org/) and
[Jupyter](http://jupyter.org/) project are living proof of that.

When carrying out computations, “testing” is implicitly carried out by “looking
at the result” - which, on a small range, works pretty well. Yet, this is not
what is meant automatic tests.
Writing tests beforehand, as suggested by [Test Driven Development](https://en.wikipedia.org/wiki/Test-driven_development) (TDD), is
sometimes considered clumsy and an approach that does not align very well with
the experimental nature of interactive development. Yet, without tests one may
quickly get lost in the complexity of even rather small problems.

In this workshop I want to share my personal experience with testing in
scientific/engineering applications and how testing works for me.

On one hand side this includes tools like
- [engarde](http://engarde.readthedocs.org/),
- [doctest](https://docs.python.org/3/library/doctest.html), and
- [pytest](http://pytest.org/)

and on the other hand side requires test-affine development workflow as well
as system design.

Hence, to deal with the question "How can I integrate testing in my
interactive development process?" we first take a look at above libraries
and then approach together a small computational problem while keeping
testability in mind.

### Target audience
Engineers/Scientists doing interactive development who would like to pay more
attention to automatic testing.

This workshop is not aimed at people who already know their way around above
libraries.
