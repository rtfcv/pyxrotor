import subprocess


class Xrotor:
    def __init__(self, silent: bool = False):
        self.silent = silent
        self.p = subprocess.Popen(
            ['xrotor'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE)
        output = self.readStdOut()
        if not silent:
            print(output, end='')

    def readStdOut(self) -> str:
        output: str = ''
        assert self.p.stdout is not None
        while self.p.poll() is None:
            char: str = self.p.stdout.read(1).decode()
            output += char
            # print(f'"{char}"')
            if output.endswith('>  '):
                break
        return output

    def writeStdIn(self, command: str, noEcho=False) -> None:
        assert self.p.stdin is not None
        self.p.stdin.write(f'{command}\n'.encode())
        if not noEcho and not self.silent:
            print(command)
        self.p.stdin.flush()

    def run(self, command:str, noEcho: bool = False) -> str:
        self.writeStdIn(command=command, noEcho=noEcho)
        output: str = self.readStdOut()
        return output

    def isAlive(self) -> bool:
        return (self.p.poll() is None)


if __name__ == '__main__':
    xr = Xrotor()
    while xr.isAlive():
        output = xr.run(input(), noEcho=True)
        print(output, end='')
