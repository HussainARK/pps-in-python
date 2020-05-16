# OOP Principles:

# # Encapsulation

class Human:
    # You can define method and properties and constructors
	def __init__(self, given_name, given_age):
		self.name = given_name
		self.age = given_age

	def walk(self):
		return f"{self.name} is walking..."

# # Inheritance


class Baker(Human):
    # the "Baker" class
    # extends all the methods and properties and even
    # the "__init__" method from the "Human" class

	def __init__(self, given_name, given_age, loves_to_bake):
		super().__init__(given_name, given_age)
		self.what_loves_to_bake = loves_to_bake


# # Polymorphism

class Runner(Human):
	def __init__(self, given_name, given_age):
		super().__init__(given_name, given_age)

    # The Same Method with many forms

	def run(self):
		return f"{self.name} is walking..."

	def run(self, meters):
		return f"{self.name} is walking {meters} meters..."

# # Abstraction

class Developer(Human):
	def __init__(self, given_name, given_age, given_github_account_password):
		super().__init__(given_name, given_age)
        # This is a Private property
        self.__github_account_password = given_github_account_password
