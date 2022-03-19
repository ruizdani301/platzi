#!/usr/bin/python3

DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
def run():
# list comprehension
    all_py_devs = [worker['name']for worker in DATA if worker["language"] == 'python']
    all_platzi_worker = [worker['name']for worker in DATA if worker["organization"] == 'Platzi']
    all_asociate = [worker['name']for worker in DATA if worker["position"] == 'Associate']
    all_javas = [java_users['age']for java_users in DATA if java_users['language'] == 'javascript']

# Pongamos en practica filters
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker['name'], adults))
    all_platzi = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    all_platzi = list(map(lambda worker: worker['name'], all_platzi))
    all_javas = list(filter(lambda worker: worker['language'] == 'javascript', DATA))
    all_javas = list(map(lambda worker: worker['name'], all_javas))
    for worker in all_javas:
        print(worker)

if __name__ == "__main__":
    run()