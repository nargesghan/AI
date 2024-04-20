class School:
    def __init__(self):
        self.students={}
        self.added_students=[]

    def add_student(self, name, grade):
        nameadded=False
        for value in self.students.values():
             for current in value:
                 if current==name:
                    nameadded=True
        if not nameadded:
            self.students.setdefault(grade,[])
            self.students[grade].append(name)
            self.added_students.append(True)
        else:
            self.added_students.append(False)
        return not nameadded

    def roster(self):
        self.students = dict(sorted(self.students.items()))
        for key,list in self.students.items():
            self.students[key]=sorted(list)
        fulllist=[]
        for list in self.students.values():
            fulllist.extend(list)
        return fulllist

    def grade(self, grade_number):
        
        listofnames=self.students.get(grade_number,[])
        return sorted(listofnames)

    def added(self):
        return self.added_students
