import multiprocessing
import time

def perform_operation(name):
    print(f"Process {name} starting")

    result= 0
    for i in range(5000):
        result += i * i
    print(f"Process {name} finished")

if __name__ == "__main__":
    start_time = time.time()

    p1 = multiprocessing.Process(target=perform_operation, args=("One",))
    p2 = multiprocessing.Process(target=perform_operation, args=("Two",))
                                 
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
    print("Both processes finished execution")