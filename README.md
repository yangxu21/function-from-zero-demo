# function-from-zero-demo

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