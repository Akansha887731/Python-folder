import time
import threading

print("Threading lock expample started...")
lock = threading.Lock()
shared_variable = 0

def increment_flag():
    global shared_variable
    for k in range(5):
        with lock:
            print(f"Inside lock : {k} in {threading.current_thread().name}")
            current_value = shared_variable
            time.sleep(0.1)
            shared_variable = current_value + 1

    print(f"Finished {threading.current_thread().name} with shared_variable =", shared_variable)

threads = [threading.Thread(target=increment_flag, name=f"Thread-{i}") for i in range(5)]
for t in threads:
    t.start()

for t in threads:
    t.join()