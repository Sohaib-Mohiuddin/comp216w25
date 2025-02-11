class Person:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f'This person\'s name is { self.name }'

