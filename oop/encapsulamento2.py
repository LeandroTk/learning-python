# -*- coding: utf-8 -*-
class SecretString:

	def __init__(self, plain_string, pass_phrase):
		self.__plain_string = plain_string
		self.__pass_phrase = pass_phrase

	def decrypt(self, pass_phrase):
		if pass_phrase == self.__pass_phrase:
			return self.__plain_string
		else:
			return ""

secret_string = SecretString("ACME: Top Secret", "antwerp")
print(secret_string.decrypt("antwerp"))

# Let's try to access the object's attribute
# print(secret_string.__plain_string)
# AttributeError: 'SecretString' object has no attribute
# if we use double underscore, nobody can access the "plain_string" attribute.

# But we can "hack" this:
# When we use a double underscore, the property is prefixed with _<classname>. Let's try to access this attribute
print(secret_string._SrectString__plain_string)