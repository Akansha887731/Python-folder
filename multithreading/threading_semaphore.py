import time
import threading

semaphore = threading.Semaphore(2)  # Allow 2 threads to access the resource at a time
semaphore_resources = []

def access_resource():
    with semaphore: # Decreases the count, or waits if the count is 0
        print(f"{threading.current_thread().name} is accessing the resource")
        semaphore_resources.append(threading.current_thread().name)
        time.sleep(2)
        print(f"{threading.current_thread().name} has finished accessing the resource")

    # Increase the count when exit the with block

threads = [threading.Thread(target=access_resource, name=f"Seamphore Thread-{i}") for i in range(5)]
[t.start() for t in threads]
[t.join() for t in threads]
