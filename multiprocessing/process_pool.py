import multiprocessing
import time

def intensive_calculation(number):
    print(f"{multiprocessing.current_process().name}: Starting calculation for {number}")
    time.sleep(0.2)
    return number * number


if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        number = range(10)

        #1. map(): Applies function to all items in iterable, returns results in order
        results_map = pool.map(intensive_calculation, number)
        print("Results from map:", results_map)


        #2. apply_async():  Submits a single task asynchronously, returns AsyncResult object
        results_map_async = pool.apply_async(intensive_calculation, (11,))
        print(results_map_async.get())  # Waits for result

        #3. imap(): Similar to map(), but returns an iterator, yielding results as they are ready
        results_imap = pool.imap(intensive_calculation, range(12, 15))
        print("Results from imap:", [result for result in results_imap])

        #4. imap_unordered(): Similar to imap(), but results can be returned in any order
        results_imap_inordered = pool.imap_unordered(intensive_calculation, range(15, 18))
        print("Results from imap_unordered:", [result for result in results_imap_inordered])

        print("All calculations completed.")
