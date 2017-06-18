# -*- coding: utf-8 -*-

class MySubClass(Object):
	''' A superclasse é a classe que será herdada
		E a subclasse é a classe que herdará (os métodos e atributos) da superclasse 
		Nesse caso: A superclasse é a object e a subclasse é MySubClass'''	
	pass

# ================================================================================================================

# Um exemplo simples de uso de herança é adicionar funcionalidades (atributos e métodos) na classe que já existe.

class Contact:

	# A classe possui essa lista (all_contacts), que será para todos os objetos que são criados a partir dessa classe.
	all_contacts = ContactList()

	def __init__(self, name, email):
		self.name = name
		self.email = email
		Contact.all_contacts.append(self)

class Supplier(Contact):
	def order(self, order):
		print("If this were a real system we would send {} order to {}".format(order, self.name))

contact = Contact("Leandro", "leandrodtk@hotmail.com")
supplier = Supplier("Kaio", "kaiohiroki@gmail.com")
print(contact.name, contact.email, supplier.name, supplier.email)

print(Contact.all_contacts)
# Serão printados os dois objetos que foram criados (contact e supplier). Nesse caso aparecerá o <hashcode> de cada objeto
# Lista com os dois objetos criados: [<__main__.Contact object at 0xb7375ecc>, <__main__.Supplier object at 0xb7375f8c>]

# Vamos verificar se o método "order" funciona para o objeto criado a partir da classe Contact.
print(contact.order("lala"))
# Resultado: erro --> Esse objeto não possui esse método

# Já o objeto supplier (criado a partir da classe Supplier) possui esse método "order"
print(supplier.order("lala"))
# Resultado do print: If this were a real system we would send lala order to Kaio

# Como a classe Supplier herda da classe Contacts, ela pode fazer tudo que a classe Contacts pode fazer (Métodos, atributos, possui a lista all_contacts)
# Mas o que foi adicionado (no caso: método order), só pode ser acessado pelo objeto supplier.

# ================================================================================================================

# Criação de uma subclasse "ContactList" herdando da classe "list", e definição do método search.
class ContactList(list):
	def search(self, name):
		'''Return all contacts that contain the search value in their name.
		   retornar uma lista com todos os contatos cujo nomes são encontrados de acordo com a pesquisa'''
		matching_contacts = []
		for contact in self:
			if name in contact.name:
				matching_contacts.append(contact)
		return matching_contacts

# Criação de 3 objetos Contact
c1 = Contact("John A", "johna@net.com")
c2 = Contact("John B", "johnb@net.com")
c3 = Contact("Jenn", "jenn@net.com")

# Criação de uma lista com todos os nomes dos contatos, após a feita a pesquisa
lista = [c.name for c in Contact.all_contacts.search("John")]
print(lista)

# ================================================================================================================

# Overriding - Sobreescrever métodos: Alterar métodos em classes que herdam da superclasse

# Not the best way: duplicate code - Esse método temo código duplicado, já que o __init__ do Contact já possui o mesmo código.
class Friendx(Contact):
	def __init__(self, name, email, phone):
		self.name = name
		self.email = email
		self.phone = phone

# Better way: using super(). A ideia é chamar o código da superclasse
class Friend(Contact):
	def __init__(self, name, email, phone):
		''' A função super() chama o código da função __init__ da superclasse "Contact".
		No caso, essa função __init__ possui os mesmos atributos da função __init__ da superclasse: name e email'''
		super().__init__(name, email)
		self.phone = phone