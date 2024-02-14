import subprocess

class Ping:
    def __init__(self, target):
        self.target = target
        self.result = self.check()

    def check(self):
        return subprocess.run(['ping', '-c', '1', '-i', '0.2', '-w', '1', self.target], capture_output=True, text=True)        


