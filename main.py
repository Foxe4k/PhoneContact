class PhoneContact ():
    #def __init__(self,name, contactNumber, note):
    #    self.name=name
    #    self.contactNumber = contactNumber
    #    self.note = note
    def convertor(self,name, contactNumber, note):
        self.name=str(name)
        self.contactNumber = str(contactNumber)
        self.note = str(note)
pa=0
class PhoneBook():
    def newContact(self,name,contactNumber):
        self.name = name
        self.contactNumber = contactNumber
        contactNumber=[]
        global pa
        pa+=1
        contactNumber[pa] += self.name
        contactNumber[pa+1] += self.contactNumber
        print(contactNumber)
    def getContactByName(self,name):
        for i in self.contactNumber:
            if self.contactNumber[i]==name:
                print(self.contactNumber[i])
        print(self.contactNumber)
test=PhoneContact()
test.convertor(1,1,1)
test2=PhoneBook()
test2.newContact("ff",1)
test2.getContactByName("m")