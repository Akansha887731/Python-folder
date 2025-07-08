import time
import concurrent.futures


def sleep(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return f"Slept for {seconds} seconds"


if __name__ == "__main__":
    print("Starting the sleep tasks...")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        list_of_seconds = [5, 4, 3, 2, 1]
        results = executor.map(sleep, list_of_seconds)

        for result in results:
            print(result)
