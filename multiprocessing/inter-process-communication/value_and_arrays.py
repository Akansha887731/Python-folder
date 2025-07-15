import multiprocessing


def increment_value(lock, shared_value):
    for _ in range(100):
        with lock:
            shared_value.value += 1
            print(f"Incremented value: {shared_value.value}")

if __name__ == "__main__":
    lock = multiprocessing.Lock()
    shared_value = multiprocessing.Value('i', 0)

    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=increment_value, args=(lock, shared_value))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"Final value: {shared_value.value}")

    shared_arr = multiprocessing.Array('i', 3)
    shared_arr[0] = 100

    print(shared_arr[0])
    