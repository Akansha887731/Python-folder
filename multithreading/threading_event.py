import threading
import time

event = threading.Event()

def waiter():
    event.wait()
    print("Waitier has been signaled and is now proceeding")

def signaler():
    print("Signaler is about to signal the event")
    time.sleep(1)  # Simulate some work before signaling
    event.set()
    print("Signaled the event")

thread_waiter = threading.Thread(target=waiter, name="Waiter Thread")
thread_signaler = threading.Thread(target=signaler, name="Signaler Thread")

thread_waiter.start()
thread_signaler.start()

thread_waiter.join()
thread_signaler.join()
