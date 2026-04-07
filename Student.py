class Student:
    def __init__(self, student_id: str, name: str, score: float):
        self.__student_id = student_id
        self.__name = name
        self.score = score # Use setter for validation

    # Getter for student_id
    @property
    def student_id(self):
        return self.__student_id
    
    # Getter for name
    @property
    def name(self):
        return self.__name
    
    @property
    def score(self):
        return self.__score
    
    # Setter for score (with validation)
    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
        else:
            print("Error: Score must be between 0 and 100. ")
    
    # Method to compute the grade
    def get_grade(self):
        if 70 <= self.__score <= 100:
            return "A"
        elif 60 <= self.__score <= 69:
            return "B"
        elif 50 <= self.__score <= 59:
            return "C"
        elif 45 <= self.__score <= 49:
            return "D"
        else:
            return "F"


if __name__ == "__main__":
    # Valid student
    student1 = Student("10970888", "Emmanuel Weyttey", 75)

    print("Student ID:", student1.student_id)
    print("Name:", student1.name)
    print("Score:", student1.score)
    print("Grade:", student1.get_grade())

    # Invalid score (should be prevented)
    print("\n--- Invalid Score ---")
    student1.score = 120

    # Check that score did not change
    print("Score after invalid attempt:", student1.score)
