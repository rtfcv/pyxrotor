# pyXrotor

a python wrapper around `xrotor`

## usage

```
from pyxrotor import Xrotor

xrotor = Xrotor(silent=True)
output = xrotor.run('DISP') # write the result in output
print(output)
xrotor.run('Q') # make sure you quit manually
```
