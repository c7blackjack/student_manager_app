class HighSchoolStudent(Student):

    school_name = "Jefferson High School"


    def get_school_name(self):
        return self.school_name


    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + " - HS"
