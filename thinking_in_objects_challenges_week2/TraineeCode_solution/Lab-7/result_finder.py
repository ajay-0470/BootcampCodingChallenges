class ResultFinder:
    """
    Properties of the fields of this class
    """
    def __init__(self):
        self._marks1 = 0
        self._marks2 = 0
        self._marks3 = 0

    @property
    def marks1(self):
        return self._marks1
    
    @marks1.setter
    def marks1(self,value):
        value = int(value)
        if value < 0 or value > 100:
            raise ValueError("Marks must be 0..100")
        self._marks1 = value

    @property
    def marks2(self):
        return self._marks2
    
    @marks2.setter
    def marks2(self,value):
        value = int(value)
        if value < 0 or value > 100:
            raise ValueError("Marks must be 0..100")
        self._marks2 = value

    @property
    def marks3(self):
        return self._marks3
    
    @marks3.setter
    def marks3(self,value):
        value = int(value)
        if value < 0 or value > 100:
            raise ValueError("Marks must be 0..100")
        self._marks3 = value

    
    """
    Method to display marks obtained
    """
    def display_marks(self):
        print("Displaying marks of 3 subjects: ")
        print("Marks 1 :", self.marks1)
        print("Marks 2 :", self.marks2)
        print("Marks 3 :", self.marks3)

    """
    Method to get the total of the marks in subjects
    """
    def get_total(self):
        return self.marks1+self.marks2+self.marks3

    """
    Method to calculate the average of the marks
    """
    def get_average(self):
        total_val = self.get_total()
        return total_val/3

    """
    Method to get the result for the marks given
    """
    def get_result(self):
         pass_mark = 35
   
         if self.marks1 < pass_mark or self.marks2 < pass_mark or self.marks3 < pass_mark:
            return "FAIL"

         avg = self.get_average()

         if avg >= 75:
            return "Distinction"
         if avg >= 60:
            return "First Class"
         if avg >= 50:
            return "Second Class"
  
         return "Pass"
