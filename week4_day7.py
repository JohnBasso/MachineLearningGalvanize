# Assigment 1
# Build a Company class, used to represent some company (Denver Beer Co., Qdoba, Chipotle, etc.).

class Company():
    
    # name - str holding the name of the company
    # industry_type - str holding what industry the company belongs to
    # num_employees - int holding the number of employees the company has
    # total_revenue - float holding the total revenue of the company
    def __init__(self,name, industry_type, num_employees, total_revenue):
        self.name = name
        self.industry_type = industry_type
        self.num_employees = num_employees
        self.total_revenue = total_revenue
        print (self.name,self.industry_type,self.num_employees,self.total_revenue)
    
    def serve_customer(self,cost):
        self.total_revenue += cost
        print(self.total_revenue)
    
    def gain_employees(self,new_employees):
        self.num_employees += len(new_employees)
        print(self.num_employees)
        
my_comp = Company("kick ass inc.","Software",100,100000) 
my_comp.serve_customer(44)
my_comp.gain_employees(["john","jeff","jack"])


# Assignment 2
# build a TV class, used to represent a television.
        
class TV():
    
    # brand - str holding the brand of the television ('Sony', 'LG', etc.)
    # on_status - bool holding whether or not the television is on. This should default to False (e.g. off).
    # current_channel - int holding the current channel number. If the television is off, then the current_channel should be 0. 
    # life_perc - float holding the percentage of life left in the TV. This should start out at 100% (i.e. default to 100).

    def __init__(self,brand):
        self.brand = brand
        self.on_status = False
        self.current_channel = 0
        self.life_perc = 100
        print (self.brand,self.on_status,self.current_channel,self.life_perc)
    
    def hit_power(self):
        self.on_status = not self.on_status
        
        if self.on_status == False:
            self.current_channel = 0
        if self.life_perc > .01: # check to make sure there is any life in the tv at all.  Not really covered in this assignment
            self.life_perc -= .01
        print(self.on_status,self.life_perc,self.current_channel)
    
    def change_channel(self,new_channel):
        if (self.on_status):
            self.current_channel += new_channel
        else:
            print("Television is not on!")
        print(self.current_channel)
        
my_TV = TV("Samsung") 
my_TV.hit_power()
my_TV.hit_power()
my_TV.hit_power()
my_TV.hit_power()
my_TV.hit_power()
my_TV.change_channel(55)
my_TV.hit_power()
my_TV.change_channel(65)  # Try changing the channel with the TV is off - Sorry dad
my_TV.hit_power()         # Turn TV on so you can change the channel
my_TV.change_channel(65)  # Now change the channel

# Assignment - Hard Part 1
# Refactor OurClass

class OurClass():

    def __init__(self, name, location, members = None, size=0):
        self.name = name
        self.location = location
        self.size = size
        
        if members == None:
            self.members = []
        else:
            self.members = members
     #   self.questions_asked = []
    
        self.check_if_at_capacity()

    #def add_question_asked(self, question):
    #    self.questions_asked.append(question)

    def add_class_members(self, member):
        self.members.append(member)

        self.check_if_at_capacity()

    def check_if_at_capacity(self):
       
        if self.size >= 31:
            print('Capacity Reached!!')
            self.at_capacity = True
        else:
            self.at_capacity = False
            
        return self.at_capacity
    
my_class = OurClass("Boulder High","Boulder")
my_class.add_class_members("Joe")
my_class.add_class_members("Jack")
my_class.add_class_members("John")
print (my_class.members)

# Assignment - Hard Part 2
# add member class    

class Member():
    def __init__(self,name,hair_color,birthdate):
        self.questions_asked = []
        self.lines_of_code = []
        self.num_lines_coded = 0
        self.coding_level = "beginner"

    def add_question_asked(self, question):
        self.questions_asked.append(question)
        
    def add_coded_line(self,code):
        self.lines_of_code.append(code)
        self.num_lines_coded += 1
        self.get_coding_level()
    
    def get_coding_level(self):
        if self.num_lines_coded > 10000:
            self.coding_level = "master"
        elif self.num_lines_coded > 1000:
            self.coding_level = "intermediate"
            
my_member = Member("John","Brown","01/01/2000")
        
# Assignment - Hard Part 2
# add member class  

class OurClass():

    def __init__(self, name, location, members = None, size=0):
        self.name = name
        self.location = location
        self.size = size
        
        if members == None:
            self.members = []
        else:
            self.members = members
        
        self.check_if_at_capacity()

    def add_class_members(self, member):
        self.members.append(member)
        self.check_if_at_capacity()
        
    def check_if_at_capacity(self):
        if self.size >= 31:
            print('Capacity Reached!!')
            self.at_capacity = True
        else:
            self.at_capacity = False
            
        return self.at_capacity
    
    def get_num_questions_asked(self):
        for x in self.members:
            return x.len(questions_asked)    
        
    def get_num_lines_code(self):
        for x in self.members:
            return x.num_lines_coded
        
    def list_members(self):
        for x in self.members:    # !!!!! Why do I have to do this? !!!!!!
            print(x.name,x.hair_color,x.questions_asked,x.lines_of_code,x.num_lines_coded,x.coding_level)
   
class Member():
    def __init__(self,name,hair_color,birthdate):
        self.name = name
        self.hair_color = hair_color
        self.questions_asked = []
        self.lines_of_code = []
        self.num_lines_coded = 0
        self.coding_level = "beginner"

    def add_question_asked(self, question):
        self.questions_asked.append(question)
        
    def add_coded_line(self,code):
        self.lines_of_code.append(code)
        self.num_lines_coded += 1
        self.get_coding_level()
    
    def get_coding_level(self):
        if self.num_lines_coded > 10000:
            self.coding_level = "master"
        elif self.num_lines_coded > 1000:
            self.coding_level = "intermediate"

mem1 = Member("john","brown","01/01/2000")
mem1.add_question_asked("This is a test")
mem1.add_coded_line("More code here")
mem2 = Member("jack","brown","01/01/1990")
mem3 = Member("joe","green","01/01/1995")
mem4 = Member("frank","yellow","01/01/1996")
mem5 = Member("nacny","brown","01/01/1997")
mem6 = Member("gina",'blonde','11,11.1966')

list_of_mems = [mem1,mem2,mem3,mem4,mem5]

        
my_class = OurClass ("BHS","Boulder",list_of_mems,len(list_of_mems))
my_class.add_class_members(mem6)

my_class.list_members()