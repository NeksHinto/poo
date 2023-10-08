from typing import Set, Dict, List

class Student:
	
    students:Dict[int, 'Student'] = {} # => {student_id:Student}

    def __init__(self, student_id: int, name: str):
        self.student_id=student_id
        self.name=name 
        self.courses:Set[Course] = set() # atributo de instancia (cada estudiante está anotado en cursos distintos, propios de cada estudiante)
    
    def __repr__(self):
        return f"{self.student_id}-{self.name}"
    
    @staticmethod
    # MAL = instancia_particular_de_student.add_student() (es como si student se comiera a el mismo)
    # BIEN = add_student(instancia_particular_de_student), es un metodo de clase y agrega al conjunto generico students, actua sobre la clase Student
    def add_student(student): #el usuario para la instancia 
        Student.students[student.student_id] = student

    @staticmethod
    def get_student(student_id): #puedo inicializar students en constructor, como es un método de la clase, no necesito pasarlo como parámetro para poder acceder
        #no pasar por parámetro todos los estudiantes
        return Student.students.get(student_id)
        #raise ValueError("El id ingresado no se encontró.")

    
class Course: 

    courses: Dict[str, 'Course'] = {} #atributo de clase, el listado de cursos siempre es igual para todas las instancias de la clase

    def __init__(self, course_id:str, description:str):
        self.description = description 
        self.course_id = course_id
        self.students: Set[Student] = set() #atributo de instancia. Cada curso tiene SU lista de estudiantes. 
    
    def __repr__(self): 
        return f"{self.course_id}-{self.description}"
    
    @staticmethod
    def get_course(course_id): 
        return Course.courses.get(course_id)
    
    def enroll(self, student_id): #comportamiento del curso particular (método de instancia de la clase Curso)
        student = Student.get_student(student_id)
        if student is not None:
            self.students.add(student)
            Course.courses[self.course_id] = self

student1=Student(123, "Juana")
print(str(student1))

# Código de prueba consigna
course1 = Course("CS101", "Introduction to Programming")
student1 = Student(1023, "Jack Black")
student2 = Student(2011, "Robin Williams")
course1.enroll(1023) #instancia.enroll()
course1.enroll(2011)

# course1.students => {1023-Jack Black, 2011-Robin Williams} => {student1, student2}



