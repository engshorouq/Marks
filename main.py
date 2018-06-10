import marks
import student


for k in range(1,51):
	exec(f'student{k} = student.student({k},"student{k}")')
for x in range(1,51):
	exec(f'student.student.add_student(student{x})')
	
student.student.display()
print('All Students Marks And Degrees ')
marks.marks.display()
