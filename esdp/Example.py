class Example:
    def __init__(self):
        self.protected_variable="I am protected"

    def protected_method (self):
        return "I am protected"
obj=Example()
print(obj.protected_variable)
print(obj.protected_method())

    
        