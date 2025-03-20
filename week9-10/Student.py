class Student:
    def __init__(self, name: str, age: int, course_name: str):
        self.name = name
        self.age = age
        self.course_name = course_name

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'course_name': self.course_name
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data['name'], data['age'], data['course_name'])