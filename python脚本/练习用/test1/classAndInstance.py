#!/usr/bin/python
#-*-coding:UTF-8-*-

class SchoolMember:
    '''this is a school member class'''
    def __init__(self,name,age):
        '''initialize a new school member'''
        self.name = name
        self.age = age

    def showDetail(self):
        print 'I am %s , mage age is %s'%(self.name,self.age)

class Student(SchoolMember):
    '''this is a student in school member'''
    countNum = 0

    def __init__(self,name,age,mark):
        self.countNum += 1
        SchoolMember.__init__(self,name,age)
        self.mark = mark
    def __del__(self):
        self.countNum -= 1
        print ' (%s say bye) ' %self.name
        print ' (%s students left) ' %self.countNum

    def showDetail(self):
        '''show the detail message of the student'''
        print 'I am %s , my age is %s , my mark is %s'%(self.name,self.age,self.mark)


print SchoolMember

person = SchoolMember('rose',45)
person.showDetail()
print SchoolMember.__doc__

student = Student('jack',20,100)
student.showDetail()
# print student.showDetail.__doc__

student2 = Student('jim',20,60)
student2.showDetail()

# student.showDetail()
