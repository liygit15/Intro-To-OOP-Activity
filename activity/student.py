# add your Student class here!
class Student:
    def __init__(self, name, grade, classes):
        self.name = name
        self.grade = grade
        self.class_enrolled = classes

    def add_class(self, new_class):
        self.class_enrolled.append(new_class)
        return self.class_enrolled     # need return or not?
    
    def get_num_classes(self):
        return len(self.class_enrolled)
    
    def summary(self):
        return f"{self.name} is a {self.grade} enrolled in {self.get_num_classes()} classes"      # return or print?
