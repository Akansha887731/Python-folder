import multiprocessing
import time

class CustomProcess(multiprocessing.Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"Process {self.name} starting")
        result =0
        for i in range(5000):
            result += i*i
        
        print(f"Process {self.name} finished")

if __name__ =="__main__":
    p1 = CustomProcess("One")
    p2 = CustomProcess("Two")

    p1.start()
    p2.start()

    p1.join()
    p2.join()