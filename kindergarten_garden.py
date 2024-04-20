class Garden:
    def __init__(self, diagram, students=["Alice",'Bob','Ginny','Harriet','Charlie','David',
                                        'Eve','Ileana','Fred','Larry','Kincaid','Joseph']):
        self.students=sorted(students)
        self.abbrivations={'G':'Grass','C':'Clover','R':"Radishes",'V':'Violets'}
        self.diagram=diagram

    def plants(self,name):
        index=self.students.index(name)+1
        rows=self.diagram.split('\n')
        string=''
        string=string+rows[0][2*index-2:2*index]
        string=string+rows[1][2*index-2:2*index]
        fullPlants=[]
        for char in string:
            fullPlants.append(self.abbrivations[char])

        return fullPlants
            
        