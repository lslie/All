#创建一个书类
#学生借书还书
#书的内容丰富


class Student(object):
	def __init__(self,name):
		self.name=name

	#学生借书
	#def student_book(self,book):
	def student_books(self,book):
		f=open('book.txt','r')
		f.read()
		f.close()

	#学生还书
class Book(object):
	def __init__(self,name,author):
		self.book_name=name
		self.book_author=author



student=Student("小白")
book=Book("漂流记","鲁滨孙")

student.student_book(book)