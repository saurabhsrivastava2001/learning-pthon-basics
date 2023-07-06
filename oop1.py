class Person :
    
    def __init__(self,name,surname,email_id,yob ):
        self.name=name
        self.surname=surname
        self.email_id=email_id
        self.yob=yob
        
         #if we create 2 init hen it will consider 2nd , because it understands we are overwriting the init consructor
        
    def age(self,current_year):
        return current_year-self.yob  
        
        
saurabh= Person("saurabh","sriv","sri@gmail.com",2001 )
print(saurabh.name)
print(saurabh.surname)
print (saurabh.email_id)
print(saurabh.yob)

print(saurabh.age(2823))

