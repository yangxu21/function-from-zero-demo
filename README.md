# function-from-zero-demo
[![CI](https://github.com/yangxu21/function-from-zero-demo/actions/workflows/main.yml/badge.svg)](https://github.com/yangxu21/function-from-zero-demo/actions/workflows/main.yml)


## Step 1: configure devlopment env

* Configure github codespaces or the equivalent (could9, etc)
* Create scaffold for struction of project: "Makefile", "requirements.txt"
* Optional (setup virtualenv) (install ipython outside of requirements)

## Step 2: Get interactive dubugging working

* Use IPython and ipdb

'''python
x = 1
y = 2
import ipdb; ipdb.set_trace()
print(x + y)
'''

## Step 3: Build a library and use it
