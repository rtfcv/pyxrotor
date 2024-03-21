from pyxrotor import Xrotor
import pandas as pd
import numpy as np

def xrotrec_main():
    xr = Xrotor()
    cmds: list = []

    while xr.isAlive():
        cmd = input()
        output = xr.run(cmd, noEcho=True)
        print(output, end='')
        cmds.append([cmd, output])

    df = pd.DataFrame(cmds, columns=np.array(['COMMANDS', 'OUTPUTS']))
    df.to_csv('xrotor_log.csv')

if __name__ == '__main__':
    xrotrec_main()
