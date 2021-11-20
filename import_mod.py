import time

db = [
    {
        'time': time.time(),
        'name': 'Vladimir',
        'mess': 'hello'
    }
]

def print_message(message):
    print(message['time'], message['name'])
    print(message['mess'])
    print()

def print_messages(db):
    for message in db:
        print_message(message)

print_messages(db)

def create_message(name, mess):
    message = {'time': time.time(), 'name': name, 'mess': mess}
    db.append(message)

def get_messages(after):
    messages = []
    for message in db:
        if message['time'] > after:
            messages.append(message)
    return message

create_message('tima', 'fuck')
print('-' * 20)

get_messages(0)

