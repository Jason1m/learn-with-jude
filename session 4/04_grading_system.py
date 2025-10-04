# Session 4: Grading System - Step by Step Build

print("=" * 60)
print("BUILDING A GRADING SYSTEM")
print("=" * 60)

print("Let's build a comprehensive grading system!")
print("We'll start with basic grade conversion and add advanced features.")

# STEP 1: Basic Grade Converter
print("\n" + "="*50)
print("STEP 1: BASIC GRADE CONVERTER")
print("="*50)

def basic_grade_converter(score):
    """Convert numerical score to letter grade"""
    print(f"Converting score: {score}")
    
    if score >= 90:
        grade = "A"
        description = "Excellent"
    elif score >= 80:
        grade = "B"
        description = "Good"
    elif score >= 70:
        grade = "C"
        description = "Satisfactory"
    elif score >= 60:
        grade = "D"
        description = "Needs Improvement"
    else:
        grade = "F"
        description = "Failing"
    
    print(f"Grade: {grade} ({description})")
    return grade

# Test basic converter
test_scores = [95, 87, 72, 65, 45]
print("Testing basic grade converter:")
for score in test_scores:
    basic_grade_converter(score)
    print()

# STEP 2: Enhanced Grade System with Plus/Minus
print("\n" + "="*50)
print("STEP 2: ENHANCED GRADE SYSTEM (A+, A-, etc.)")
print("="*50)

def enhanced_grade_converter(score):
    """Convert score to letter grade with plus/minus"""
    print(f"Converting score: {score}")
    
    if score < 0 or score > 100:
        print("❌ Invalid score! Must be between 0-100")
        return None
    
    if score >= 97:
        grade = "A+"
    elif score >= 93:
        grade = "A"
    elif score >= 90:
        grade = "A-"
    elif score >= 87:
        grade = "B+"
    elif score >= 83:
        grade = "B"
    elif score >= 80:
        grade = "B-"
    elif score >= 77:
        grade = "C+"
    elif score >= 73:
        grade = "C"
    elif score >= 70:
        grade = "C-"
    elif score >= 67:
        grade = "D+"
    elif score >= 63:
        grade = "D"
    elif score >= 60:
        grade = "D-"
    else:
        grade = "F"
    
    print(f"Grade: {grade}")
    return grade

# Test enhanced converter
test_scores = [98, 91, 86, 74, 61, 45]
print("Testing enhanced grade converter:")
for score in test_scores:
    enhanced_grade_converter(score)
    print()

# STEP 3: Grade Point Average (GPA) Calculator
print("\n" + "="*50)
print("STEP 3: GPA CALCULATOR")
print("="*50)

def letter_to_gpa(letter_grade):
    """Convert letter grade to GPA points"""
    gpa_scale = {
        "A+": 4.0, "A": 4.0, "A-": 3.7,
        "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7,
        "D+": 1.3, "D": 1.0, "D-": 0.7,
        "F": 0.0
    }
    return gpa_scale.get(letter_grade, 0.0)

def calculate_gpa(scores):
    """Calculate GPA from list of scores"""
    print("Calculating GPA...")
    print("-" * 30)
    
    total_points = 0
    total_courses = len(scores)
    
    for i, score in enumerate(scores, 1):
        grade = enhanced_grade_converter(score)
        gpa_points = letter_to_gpa(grade)
        total_points += gpa_points
        print(f"Course {i}: {score} → {grade} → {gpa_points} points")
    
    if total_courses > 0:
        gpa = total_points / total_courses
        print("-" * 30)
        print(f"Total Points: {total_points}")
        print(f"Total Courses: {total_courses}")
        print(f"GPA: {gpa:.2f}")
        
        # GPA interpretation
        if gpa >= 3.5:
            print("🎉 Dean's List! Excellent academic performance!")
        elif gpa >= 3.0:
            print("✅ Good academic standing")
        elif gpa >= 2.0:
            print("⚠️  Satisfactory - room for improvement")
        else:
            print("❌ Academic probation - seek help")
        
        return gpa
    else:
        print("No courses to calculate GPA")
        return 0.0

# Test GPA calculation
student_scores = [92, 87, 78, 84, 91]
print("Student transcript:")
calculate_gpa(student_scores)

# STEP 4: Complete Student Grading System
print("\n" + "="*50)
print("STEP 4: COMPLETE STUDENT GRADING SYSTEM")
print("="*50)

class StudentGrades:
    def __init__(self, student_name):
        self.student_name = student_name
        self.grades = []
        self.course_names = []
    
    def add_grade(self, course_name, score):
        """Add a grade for a specific course"""
        if 0 <= score <= 100:
            self.course_names.append(course_name)
            self.grades.append(score)
            print(f"Added {course_name}: {score}")
        else:
            print("❌ Invalid score! Must be between 0-100")
    
    def get_letter_grade(self, score):
        """Get letter grade for a score"""
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
    
    def calculate_average(self):
        """Calculate average score"""
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0
    
    def get_final_grade(self):
        """Get final letter grade based on average"""
        average = self.calculate_average()
        return self.get_letter_grade(average)
    
    def print_transcript(self):
        """Print complete transcript"""
        print(f"\n📋 TRANSCRIPT FOR {self.student_name}")
        print("="*50)
        
        if not self.grades:
            print("No grades recorded")
            return
        
        # Individual course grades
        for course, score in zip(self.course_names, self.grades):
            letter = self.get_letter_grade(score)
            print(f"{course:<20}: {score:>3}% ({letter})")
        
        print("-" * 50)
        
        # Statistics
        average = self.calculate_average()
        final_grade = self.get_final_grade()
        highest = max(self.grades)
        lowest = min(self.grades)
        
        print(f"Average Score: {average:.1f}%")
        print(f"Final Grade: {final_grade}")
        print(f"Highest Score: {highest}%")
        print(f"Lowest Score: {lowest}%")
        print(f"Courses Completed: {len(self.grades)}")
        
        # Performance analysis
        print(f"\n📊 PERFORMANCE ANALYSIS:")
        
        # Count grades by letter
        grade_counts = {}
        for score in self.grades:
            letter = self.get_letter_grade(score)
            grade_counts[letter] = grade_counts.get(letter, 0) + 1
        
        for grade in ["A", "B", "C", "D", "F"]:
            count = grade_counts.get(grade, 0)
            if count > 0:
                print(f"{grade}: {count} course(s)")
        
        # Overall assessment
        if average >= 90:
            print("🎉 Outstanding performance! Keep up the excellent work!")
        elif average >= 80:
            print("✅ Good performance! You're doing well!")
        elif average >= 70:
            print("⚠️  Satisfactory performance. Consider study improvements.")
        elif average >= 60:
            print("❌ Below average performance. Seek academic help.")
        else:
            print("🚨 Failing performance. Immediate intervention needed.")

# Test the complete grading system
print("Creating student record...")
student = StudentGrades("Alice Johnson")

# Add some grades
student.add_grade("Mathematics", 92)
student.add_grade("English", 87)
student.add_grade("Science", 78)
student.add_grade("History", 84)
student.add_grade("Art", 91)

# Print transcript
student.print_transcript()

# STEP 5: Class Grade Distribution Analysis
print("\n" + "="*50)
print("STEP 5: CLASS GRADE DISTRIBUTION")
print("="*50)

def analyze_class_grades(class_scores):
    """Analyze grade distribution for entire class"""
    print(f"Analyzing grades for {len(class_scores)} students...")
    print("-" * 40)
    
    if not class_scores:
        print("No scores to analyze")
        return
    
    # Calculate statistics
    total_students = len(class_scores)
    average_score = sum(class_scores) / total_students
    highest_score = max(class_scores)
    lowest_score = min(class_scores)
    
    # Count grades
    grade_distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    
    for score in class_scores:
        if score >= 90:
            grade_distribution["A"] += 1
        elif score >= 80:
            grade_distribution["B"] += 1
        elif score >= 70:
            grade_distribution["C"] += 1
        elif score >= 60:
            grade_distribution["D"] += 1
        else:
            grade_distribution["F"] += 1
    
    # Print results
    print(f"Class Average: {average_score:.1f}%")
    print(f"Highest Score: {highest_score}%")
    print(f"Lowest Score: {lowest_score}%")
    print(f"Total Students: {total_students}")
    
    print(f"\n📊 GRADE DISTRIBUTION:")
    for grade, count in grade_distribution.items():
        percentage = (count / total_students) * 100
        bar = "█" * int(percentage / 5)  # Visual bar
        print(f"{grade}: {count:2d} students ({percentage:4.1f}%) {bar}")
    
    # Class performance assessment
    passing_students = total_students - grade_distribution["F"]
    pass_rate = (passing_students / total_students) * 100
    
    print(f"\n📈 CLASS PERFORMANCE:")
    print(f"Pass Rate: {pass_rate:.1f}% ({passing_students}/{total_students})")
    
    if pass_rate >= 90:
        print("🎉 Excellent class performance!")
    elif pass_rate >= 80:
        print("✅ Good class performance!")
    elif pass_rate >= 70:
        print("⚠️  Average class performance.")
    else:
        print("❌ Poor class performance. Review teaching methods.")

# Test class analysis
class_scores = [92, 87, 78, 84, 91, 76, 89, 93, 67, 82, 88, 74, 96, 81, 79]
analyze_class_grades(class_scores)

# STEP 6: Interactive Grading System
print("\n" + "="*50)
print("STEP 6: INTERACTIVE GRADING SYSTEM")
print("="*50)

def interactive_grading_system():
    """Interactive system for teacher to input grades"""
    print("Welcome to the Interactive Grading System!")
    
    student_name = input("Enter student name: ")
    student = StudentGrades(student_name)
    
    print(f"\nEntering grades for {student_name}")
    print("Enter 'done' when finished adding courses")
    
    while True:
        course = input("\nEnter course name (or 'done' to finish): ")
        if course.lower() == 'done':
            break
        
        try:
            score = float(input(f"Enter score for {course} (0-100): "))
            student.add_grade(course, score)
        except ValueError:
            print("❌ Please enter a valid number")
    
    # Show final transcript
    student.print_transcript()
    
    return student

# Uncomment to test interactively:
# interactive_grading_system()

print("\n" + "="*60)
print("🎯 GRADING SYSTEM COMPLETE!")
print("You've learned how to build a comprehensive grading system!")
print("Key concepts covered:")
print("• Conditional logic for grade ranges")
print("• Data organization and management")
print("• Statistical calculations")
print("• Class-based programming")
print("• User interaction and input validation")
print("• Data analysis and visualization")
print("="*60)