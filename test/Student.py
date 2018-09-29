class Student(object):
    birthday = 22;
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self, value):
        self._birth = value

s = Student()
s.birth = 28;
print(s.birth)
print(Student.birth);
