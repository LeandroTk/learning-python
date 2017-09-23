# ----- Public Instance Variable -----

class Person:
    def __init__(self, first_name):
        self.first_name = first_name

tk = Person('TK')
print(tk.first_name) # => TK

tk = Person('TK')
tk.first_name = 'Kaio'
print(tk.first_name) # => Kaio

class Person:
    first_name = 'TK'

tk = Person()
print(tk.first_name) # => TK

# ----- Private Instance Variable -----

class Person:
    def __init__(self, first_name, email):
        self.first_name = first_name
        self.__email = email

    def update_email(self, new_email):
        self.__email = new_email

    def email(self):
        return self.__email

tk = Person('TK', 'tk@mail.com')
# print(tk.__email) # => AttributeError: Person instance has no attribute '__email'
print(tk.email()) # => tk@mail.com
tk.__email = 'new_tk@mail.com'
print(tk.email()) # => tk@mail.com
tk.update_email('new_tk@mail.com')
print(tk.email()) # => new_tk@mail.com
