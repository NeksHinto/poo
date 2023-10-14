from typing import Set, Dict, List

class Student:
	
    students_data_base:Dict[int, 'Student'] = {} # => {student_id:Student} 123: instancia Juana

    def __init__(self, student_id: int, name: str):
        self.student_id=student_id
        self.name=name 
        self.courses:Set[Course] = set() # atributo de instancia (cada estudiante está anotado en cursos distintos, propios de cada estudiante)
    def __repr__(self):
        return f"{self.student_id}-{self.name}"
    
    @staticmethod
    # MAL = instancia_particular_de_student.add_student() (es como si student se comiera a el mismo)
    # BIEN = add_student(instancia_particular_de_student), es un metodo de clase y agrega al conjunto generico students, actua sobre la clase Student
    def add_student(student_particular: 'Student'): #el usuario pasa la instancia 
        Student.students_data_base[student_particular.student_id] = student_particular

    @staticmethod
    def get_student(student_id): #puedo inicializar students en constructor, como es un método de la clase, no necesito pasarlo como parámetro para poder acceder
        #no pasar por parámetro todos los estudiantes
        return Student.students_data_base.get(student_id)
        #raise ValueError("El id ingresado no se encontró.")

    def get_scores(self) -> Dict['Course', List[int]]:
        scores={}
        for course in self.courses:
            if self in course.exams:
                scores[course]=course.get_scores(self.student_id) #asociación, pero no herencia!!!
        return scores #si no está anotado en ningún curso (o sea, que self.courses = []), devuelve diccionario vacía

    
class Course: 

    courses_data_base: Dict[str, 'Course'] = {} #atributo de clase, el listado de cursos siempre es igual para todas las instancias de la clase
    
    def __init__(self, course_id:str, description:str):
        self.description = description 
        self.course_id = course_id
        self.students_enrolled: Set[Student] = set() #atributo de instancia. Cada curso tiene SU lista de estudiantes. 
        # Exams es un atributo de instancia de la clase Course donde almaceno todos los exámenes del curso en una colección
        # de tipo Dict donde los pares clave:valor se corresponden a los tipos Student:List[int] (por cada estudiante (key), 
        # tenemos una lista de enteros que representan sus notas (valor))
        # { 
        #   { 123-"Juana": [3, 4, 6] }, #guardo todo el objeto antes de los dos puntos, no solo esos dos atributos
        #   { 1023-"Jack Black": [7, 3, 5] }
        # }
        self.exams: Dict[Student, List[int]] = {} #no se pasa por parámetro, usuario no ingresa datos 
    
    def __repr__(self): 
        return f"{self.course_id}-{self.description}-{self.exams}"
    
    @staticmethod
    def get_course(course_id): 
        return Course.courses_data_base.get(course_id)
    
    def enroll(self, student_id): #comportamiento del curso particular (método de instancia de la clase Curso)
        # Buscamos la instancia de student que quiero enrollear con el método get_student de la clase Student
        student = Student.get_student(student_id)
        if student is not None:
            self.students_enrolled.add(student)
            student.courses.add(self) #no hace falta ponder Student.stuent porque get st ya está arriba
    
    def add_exam(self, student_id: int, score: int): 
        student=Student.get_student(student_id)
        if student is not None: 
            if student in self.exams:
                self.exams[student].append(score)
            else:
                self.exams[student] = [] #inicializar lista en vacío
                self.exams[student].append(score)

    def get_scores(self, student_id: int) -> List[int]:
        student=Student.get_student(student_id)
        if student is not None and student in self.exams: #asumo que si no tiene subidas notas, no devuelve nada (porque no está aclarado en el código de prueba)
            return self.exams[student]
        else: 
            return None    


student1=Student(123, "Juana")

# Código de prueba consigna
course1 = Course("CS101", "Introduction to Programming")
student1 = Student(1023, "Jack Black")
student2 = Student(2011, "Robin Williams")
Student.add_student(student1)
Student.add_student(student2)
course1.enroll(1023) #instancia.enroll()
course1.enroll(2011)

course1.add_exam(1023, 20)
course1.add_exam(1023, 40)
course1.add_exam(2011, 80)
course1.add_exam(4321, 70)
print(course1) # => {1023-Jack Black: [20, 40], 2011-Robin Williams: [80], 4321-Steve Carell: [70]}

# course1.students => {1023-Jack Black, 2011-Robin Williams} => {student1, student2}



