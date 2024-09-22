class Example:
    def __init__(self):
        self.public_variable="I am public"

    def public_method (self):
        return "I am public"
obj=Example()
print(obj.public_variable)
print(obj.public_method())