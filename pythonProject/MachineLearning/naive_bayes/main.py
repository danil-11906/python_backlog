# coding=utf-8
import json

from naive_bayes.property import Property

file_handle = open('events.json', 'r')
data = json.load(file_handle)

events = {}
for event in data:
    events[event['id']] = event['name']

file_handle = open('cases.json', 'r')
data = json.load(file_handle)

cases = {}
for event_case in data:

    probabilities = {}
    for event_id in events.keys():
        probabilities[event_id] = event_case[str(event_id)]

    cases[event_case['id']] = Property(event_case['name'], probabilities)

file_handle = open('input.json', 'r')
current_cases = json.load(file_handle)

print('-------------------------------------------------------------------------')
print(ljust(' Болезнь', 48) + ' | Вероятность')
print('-------------------------------------------------------------------------')

most_likely_event = ''
most_likely_event_probability = 0.0
for event_id in events.keys():
    probability = 1.0
    for case in current_cases:
        probability *= cases[case].probabilities[event_id]

    if most_likely_event_probability < probability:
        most_likely_event_probability = probability
        most_likely_event = events[event_id]

    print(' ' + ljust(events[event_id], 40) + u' | Вероятность: ' + str(probability))
print('-------------------------------------------------------------------------')

print(' Наиболее вероятно:')
print(' ' + ljust(most_likely_event, 40) + u' | Вероятность: ' + str(most_likely_event_probability))

