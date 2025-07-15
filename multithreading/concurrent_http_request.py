import threading
import requests

urls = [
    "https://www.example.com",
    "https://www.google.com",
    "https://www.wikipedia.org",
    "https://www.python.org"
]

def make_requests(url):
    response = requests.get(url)
    print(f"Response from {url}: {response.status_code}")

if __name__ == "__main__":
    threads_list = []
    for url  in urls:
        thread = threading.Thread(target=make_requests, args=(url,))
        threads_list.append(thread)
        thread.start()

    for thread in threads_list:
        thread.join()
