class A:
	a = 10
	b = 20
	def addd(self):
		print(self.a + self.b)
		
class B:
	d = 100
	e = 200
	def add(self):
		print(self.d + self.e)
	
class C(A, B):
	pass
		
c = C()
c.add()
	
