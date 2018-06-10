class marks():
	Marks=[]
	def __init__(self,course1,course2,course3,course4,course5,student_name):
		assert type(course1)==int and 0<=course1<=100 ,'Plesae enter corret number'
		assert type(course2)==int and 0<=course2<=100 ,'Plesae enter corret number'
		assert type(course3)==int and 0<=course3<=100 ,'Plesae enter corret number'
		assert type(course4)==int and 0<=course4<=100 ,'Plesae enter corret number'
		assert type(course5)==int and 0<=course5<=100 ,'Plesae enter corret number'
		self.course1=course1
		self.course2=course2
		self.course3=course3
		self.course4=course4
		self.course5=course5
		self.student_name=student_name

	def add_marks(self):
		marks.Marks.append(self)	
	def display():
		for x in marks.Marks:
			print("Student name :"+x.student_name)
			print("Student course 1 mark :"+str(x.course1))
			print("Student course 2 mark :"+str(x.course2))
			print("Student course 3 mark :"+str(x.course3))
			print("Student course 4 mark :"+str(x.course4))
			print("Student course 5 mark :"+str(x.course5))
			total=x.course1+x.course2+x.course3+x.course4+x.course5
			print("Total : "+str(total))
			average=float(total/5)
			regard=''
			if average>=90:
				regard='Exellent'
			elif average>=80 and average<90:
				regard='Very Good'
			elif average>=70 and average<80:
				regard='Good'
			elif average>=60 and average<70:
				regard='Accept'
			else:
				regard='Fail'				
			print("Average : "+ str(average)+'% , Regard : '+regard)

			print('*'*10)

					