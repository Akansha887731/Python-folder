import multiprocessing

def producer(queue):
    for i in range(5):
        print(f"Producing {i}")
        queue.put(i)
    queue.put(None)  # Signal that production is done

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consuming {item}")


if __name__ == "__main__":
    queue = multiprocessing.Queue()
    prod = multiprocessing.Process(target=producer, args=(queue,))
    cons = multiprocessing.Process(target=consumer, args=(queue,))

    prod.start()
    cons.start()

    prod.join()
    cons.join()
