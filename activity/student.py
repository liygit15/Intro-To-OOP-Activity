# add your Student class here!
class Student:
    def __init__(self, name, grade, classes):
        self.name = name
        self.grade = grade
        self.have_class = classes

    def add_class(self, new_class):
        self.have_class.append(new_class)
        return self.have_class     # need return or not?
    
    def get_num_classes(self):
        return len(self.have_class)
    
    def summary(self):
        return f"{self.name} is a {self.grade} enrolled in {self.get_num_classes()} classes"      # return or print?
