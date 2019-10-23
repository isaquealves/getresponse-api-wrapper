# GetResponse API Wrapper

Wrapping GetResponse API to simplify integrations

## Motivation

GetResponse is one of the most used email marketing automation tools and its API is awesome, but somehow complex to use in user applications.\
The intent of this library is to provide an simpler way to integrate GetResponse into python applications.

## Setting things up as colaborator

As colaborator you can help to implement the right resource calls and improve the code quality, but, first, you need to prepare you environment.\
We recommend to use [Pyenv](https://github.com/pyenv/pyenv) and [Poetry](https://poetry.eustace.io/). Both tools work well together and make very easy to handle environment configuration changes.

### Clone this repository

First thing to do is to clone the repository. Go on and clone it:

```shell

git clone git@github.com:isaquealves/getresponse-api-wrapper.git
```

### Install Pyenv

You can find instructions on how to install and configure Pyenv on its repository. Prior to proceed with installation, we recommend you to take a careful read on section [How it Works](https://github.com/pyenv/pyenv#how-it-works).\
After installing, remember to add pyenv-virtualenv plugin, run commands as follows:\

```shell
cd getresponse-api-wrapper
$ pyenv install 3.7.1
...
pyenv local 3.7.1
```

### Install Poetry

To install poetry, just follow the instructions from [Poetry Documentation](https://poetry.eustace.io/).\
After installing, go to project directory and run:

```shell
poetry install
```

This should install all project dependencies.

### Choose or create an issue and implement solution

Take a look at issues tab to find out something you can help to solve.

---

## Table Of Contents

* **[Understanding GetResponse API Wrapper](#understanding)**
  * [The Resources](#the_resources)
  * [The Client](#the_client)

## Understanding GetResponse API Wrapper

GetResponse API offers a large collection of resources, as can be seen on [Documentation](https://apireference.getresponse.com), so we start building this wrapper to ease integration for other apps.
Basically, this wrapper provides a simple and concise interface to access get response api resources.

### The Resources

Each remote GetReponse api resource is wrapped up by a resource class

### The Client

GetResponse Api Wrapper Client class uses Facade pattern, covering all the complexity related to the resources.

