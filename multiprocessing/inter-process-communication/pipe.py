import multiprocessing

def sender(conn, message):
    conn.send(message)
    print(f"Sent: {message}")
    response = conn.recv()
    print(f"Response from receiver: {response}")
    print("Process finished")
    conn.close()


def receiver(conn):
    message =conn.recv()
    print(f"Received: {message}")
    conn.send("Acknowledged")
    conn.close()

if __name__ == "__main__":
    sender_conn, receiver_con = multiprocessing.Pipe()

    sen = multiprocessing.Process(target=sender, args=(sender_conn, "Hello from sender!"))
    rec = multiprocessing.Process(target=receiver, args=(receiver_con,))

    sen.start()
    rec.start()

    sen.join()
    rec.join()
