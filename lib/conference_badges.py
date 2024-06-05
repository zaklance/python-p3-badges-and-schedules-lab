def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    list = []
    for name in names:
        list.append(f'Hello, my name is {name}.')
    return list

def assign_rooms(names):
    list = []
    i = 1
    for name in names:
        list.append(f"Hello, {name}! You'll be assigned to room {i}!")
        i += 1
    return list

def printer(names):
    for name in names:
        print(f'Hello, my name is {name}.')
    for name in assign_rooms(names):
        print(name)
    
