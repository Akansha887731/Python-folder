import threading
import time

condition = threading.Condition()
items = []

def producer():
    global items
    with condition:
        for i in range(5):
            items.append(f"Item-{i}")
            print(f"Produced {i}")
            condition.notify()
            time.sleep(1)

def consumer(name):
    global items
    with condition:
            print(f"{name} waiting for items...")
            while not items:
                condition.wait()
            item = items.pop(0)
            print(f"Consumed {item}")
            time.sleep(2)

producer_thread = threading.Thread(target=producer, name="Producer Thread")
consumer_thread1 = threading.Thread(target=consumer, args=("Consumer Thread 1",), name="Consumer Thread 1")
consumer_thread2 = threading.Thread(target=consumer, args=("Consumer Thread 2",), name="Consumer Thread 2") 


consumer_thread1.start()
consumer_thread2.start()
producer_thread.start()

producer_thread.join()
consumer_thread1.join()
consumer_thread2.join()
