import time
from queue import Queue
import random

queue = Queue()
idx = 0

def generate_request():
    '''створення заявок та додання їх до черги'''
    global queue, idx

    reqs = random.choice([0,1,2,0])
    while reqs > 0:
        new_data = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        print(f"Generate new request with id: {idx}")
        queue.put({'id': idx, 'data': new_data})
        idx += 1
        reqs -= 1

def process_request():
    '''Обробка заявок по черзі'''
    global queue

    if queue.empty():
        print("The Queue is empty - nothing to do")
        return
    req = queue.get();
    print(f"Process requiest with id: {req['id']}")



if __name__ == "__main__":
    try:
        while True:
            generate_request()
            process_request()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Goodbye")
        