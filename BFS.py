from collections import deque

graph = {}
graph['you'] = ['mame', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['mame'] = ['peggy']
graph['claire'] = ['thoa', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thoa'] = []
graph['jonny'] = []

def end_with_a(person):
    return person[-1] == 'a'

def search_in_your_connection_with_name_start_with_a():
    search_deque = deque()
    search_deque += graph['you']
    checked = []
    while search_deque:
        person = search_deque.popleft()
        if person not in checked:
            if end_with_a(person):
                return person + " End his name with Letter A"
            else:
                search_deque += graph[person]
                checked.append(person)
    return "no Friends end hhis name with Letter A"

print(search_in_your_connection_with_name_start_with_a())