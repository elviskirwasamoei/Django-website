class Base:
   print("public method")
 def _fun(self)
   print("private method")

class Derived(Base):
   def _init_(self):
      Base._init_(self)
   def call_public(self):
      print("inside derived class")



