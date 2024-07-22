class Subjects():
    physics = "physics"
    chemistry = "chemistry"
    maths = "maths"

    subject_choices = ( ("Physics","physics"),("Chemistry","chemistry"),("Maths","maths")  )
    
    
    eleventh = "11th"
    tweleth = "12th"
    class_choices = (( "11th","Eleventh"),( "12th","Tweleth"))
class FeedbackConstants():
    PERFECT = 1
    TOO_EASY = 0
    TOO_HARD = 2
    
    SESSION_FEEL_CHOICES = [
        (PERFECT, 'Perfect'),
        (TOO_EASY, 'Too Easy'),
        (TOO_HARD, 'Too Hard'),
    ]
     
class PrirorityConstants():
    HIGH = 1
    MEDIUM = 2
    LOW = 3
    
    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]
class YearConstants():
    JEE_2024 = 1
    JEE_2025 = 2
    JEE_2026 = 3
    YEAR_CHOICES = [
      (JEE_2024, "JEE 2024"),
      (JEE_2025, "JEE 2025"),
      (JEE_2026, "JEE 2026"),
    ]