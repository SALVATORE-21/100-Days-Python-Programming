class user:
    #__init__ method is a special method in Python classes that is automatically called when a new instance of the class is created. 
    # It is used to initialize the attributes of the class with default or user-defined values.
    def __init__(self, id, username, follower=0):
        print("Initializing user object...") #This line prints a message indicating that the user object is being initialized.
        self.id = id
        self.username = username
        self.follower = follower #Defaults to 0 if not provided, but can be overridden by an argument.


user1 = user("001", "john_doe") #This line creates an instance of the user class named user1, passing in the values "001" and "john_doe" as arguments for the id and username attributes, respectively. The __init__ method is automatically called, initializing the attributes and printing the initialization message.
print(user1.id) #This line prints the id attribute of the user1 object, which is "001".
print(user1.username) #This line prints the username attribute of the user1 object, which
#When the attribute follower is set to default the user need not compulsarily provide a value for it when creating a new user object. If the user does not provide a value, the attribute will be initialized to 0 by default. However, if the user wants to set a specific value for the follower attribute, they can do so by providing it as an argument when creating the user object.
user2 = user("002", "jane_doe") #This line creates another instance of the user class named user2, passing in the values "002" and "jane_doe" as arguments for the id and username attributes, respectively. The __init__ method is automatically called, initializing the attributes and printing the initialization message.
print(user2.id) #This line prints the id attribute of the user2 object, which
user3 = user("003", "alice_smith","4000") #This line creates another instance of the user class named user3, passing in the values "003" and "alice_smith" as arguments for the id and username attributes, respectively. The __init__ method is automatically called, initializing the attributes and printing the initialization message.
print(user3.follower)
