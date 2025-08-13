from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
import random
from faker import Faker
from typing import Optional


engine = create_engine('sqlite:///homework22.db', echo=True)
Base = declarative_base()

fake = Faker()
random.seed(42)

enrollment = Table(
    'enrollment',
    Base.metadata,
    Column('student_id', ForeignKey('student.id'),  primary_key=True),
    Column('course_id', ForeignKey('course.id'), primary_key=True)
)

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    courses = relationship("Course", secondary=enrollment,  back_populates="students")
    def __repr__(self):
        return f'<Student id={self.id}, name={self.name}, age={self.age}>'

class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    students = relationship("Student", secondary=enrollment,  back_populates="courses")
    def __repr__(self):
        return f'<Course id={self.id}, title={self.title}>'

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def seed_courses():
    existing = session.query(Course).count()
    if existing > 0:
        return session.query(Course).all()

    courses = [Course(title=t) for t in ["Math", "English", "Science", "History", "Cyber Security" ]]
    session.add_all(courses)
    session.commit()
    return courses

def seed_students_random(courses, n=20, min_courses=1, max_courses=5):
    current = session.query(Student).count()
    if current >= n:
        return session.query(Student).all()

    if not courses:
        raise ValueError("Немає курсів для запису студентів")
    max_allowed = len(courses)
    min_courses = max(1, min_courses)
    max_courses = min(max_courses, max_allowed)
    if min_courses > max_courses:
        min_courses = max_courses

    to_create = n - current
    students = []
    for _ in range(to_create):
        name = fake.name()
        age = random.randint(18, 30)
        st = Student(name=name, age=age)

        k = random.randint(min_courses, max_courses)
        st.courses = random.sample(courses, k)

        students.append(st)
    session.add_all(students)
    session.commit()
    return session.query(Student).all()

#READ
def get_students_by_course_title(title: str):
    course = session.query(Course).filter(Course.title == title).first()
    if not course:
        return []
    return course.students
def get_courses_by_student_name(name: str):
    student = session.query(Student).filter(Student.name == name).first()
    if not student:
        return []
    return student.courses
#UPDATES
def update_course(course_id: int, *, title: Optional[str]= None) -> Course:
    cr = session.get(Course, course_id)
    if not cr:
        raise ValueError(f'Курс id={course_id} не знайдено')
    if title is not None:
        cr.title = title
    session.commit()
    session.refresh(cr)
    return cr
def update_student(student_id: int, *, name: Optional[str] = None, age: Optional[int] = None ) -> Student:
    st = session.get(Student, student_id)
    if not st:
        raise ValueError(f' Студента  id={student_id} не знайдено')
    if name is not None:
        st.name = name
    if age is not None:
        st.age = age
    session.commit()
    session.refresh(st)
    return st
#delete
def delete_student(student_id: int):
    st = session.get(Student, student_id)
    if not st:
        raise ValueError(f' Студента  id={student_id} не знайдено')
    st.courses.clear()
    session.delete(st)
    session.commit()

if __name__ == '__main__':
    courses = seed_courses()
    students = seed_students_random(courses, n=20, min_courses=1, max_courses=5)
    print(f'Курсів: {len(courses)}, Студентів: {len(students)}')

    print("\n=== Студенти, зареєстровані на курс 'Math' ===")
    print([s.name for s in get_students_by_course_title("Math")])

    any_student = session.query(Student).first()
    print(f'\n=== Курси, на які записано студента {any_student.name} ===')
    print([c.title for c in get_courses_by_student_name(any_student.name)])
#оновлення
    print("\n=== Оновлюємо дані студента ===")
    updated = update_student(any_student.id, name=any_student.name + " (Updated)")
    print(updated)

    any_course = session.query(Course).filter_by(title="English").first()
    print("\n=== Оновлюємо назву курсу 'English' ===")
    updated_cousre = update_course(any_course.id, title="English (Updated)")
    print(updated_cousre)
#видалення
    print("\n=== Видаляємо студента (демо) ===")
    delete_student(updated.id)
    print("Існує після видалення? ->", session.get(Student, updated.id))






