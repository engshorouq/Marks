import marks
class student():
	Student=[]
	def __init__(self,student_id,student_name):
		assert type(student_id)==int,'Plesae enter number'
		assert type(student_name)==str,'Plesae enter string'
		self.student_id=student_id
		self.student_name=student_name

	def add_student(self):
		student.Student.append(self)

	
	def display():
		for x in student.Student:
			print('Student ID : '+str(x.student_id))
			print('Student Name : '+x.student_name)
			c1=int(input('mark course 1 : '))
			c2=int(input('mark course 2 : '))
			c3=int(input('mark course 3 : '))
			c4=int(input('mark course 4 : '))
			c5=int(input('mark course 5 : '))
			mark=marks.marks(c1,c2,c3,c4,c5,x.student_name)
			marks.marks.add_marks(mark)
			print('*'*10)



