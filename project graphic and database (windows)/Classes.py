class Users :
    
    UserName = None
    password = None
    FirstName = None
    LastName = None
    Age = None
    Adress = None
    PhoneNumber = None
    Email = None
    
    def __init__(self,UN,P,FN,LN,A,AD,PN,E) -> None:
        self.UserName = UN
        self.password = P
        self.FirstName = FN
        self.LastName = LN
        self.Age = A
        self.Adress = AD
        self.PhoneNumber = PN
        self.Email = E
        
class Admins:
    UserName = None
    password = None
    FirstName = None
    LastName = None
    Age = None
    Adress = None
    PhoneNumber = None
    Email = None
    
    def __init__(self,UN,P,FN,LN,A,AD,PN,E) -> None:
        self.UserName = UN
        self.password = P
        self.FirstName = FN
        self.LastName = LN
        self.Age = A
        self.Adress = AD
        self.PhoneNumber = PN
        self.Email = E