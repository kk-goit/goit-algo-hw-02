from collections import deque 

def check_is_polyndrom(data: str) -> bool:
    '''Перевірка строки чи є вона поліндром'''   
    q = deque()
    for c in data.lower():
        if c != ' ':
            q.append(c)

    if len(q) <= 1:
        return True

    while len(q) > 1:
        if q.pop() != q.popleft():
            return False
        
    return True

if __name__ == "__main__":
    try:
        while True:
            str = input("Please enter a word: ")
            print(f"The word '{str}' is {'not ' if not check_is_polyndrom(str) else ''}a polyndrom")
    except KeyboardInterrupt:
        print("Goodbye")
