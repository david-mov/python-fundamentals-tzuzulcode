from uuid import uuid4
from operator import itemgetter

class Products:

	products = {}

	def create(self, name, price, stock):
		product = {
			'name': name,
			'price': price,
			'stock': stock
		}
		self.products[str(uuid4())] = product
		return 'New product added successfully'

	def getAll(self):
		return self.products

	def getById(self, code):
		if not self.products[code]:
			return 'Product not found'
		else:
			return self.products[code]

	def update(self, code, data):
		name, price, stock = itemgetter('name', 'price', 'stock')(data)

		if not self.products[code]:
			return 'Product not found'
		else:
			if name: self.products[code].name = name
			if price: self.products[code].price = price
			if stock: self.products[code].stock = stock
		return self.products[code]

	def delete(self, code):
		if not self.products[code]:
			return 'Product not found'
		else:
			self.products[code].pop()
			return 'Product deleted successfully'

class Cart:

	cart = {}

	def getAll(self):
		return self.cart

	def add(self, data):
		code, name, price, stock = itemgetter('code', 'name', 'price', 'stock')(data)

		if self.cart[code]:
			self.cart[code].quantity += 1
		else:
			self.cart[code] = {
				name: name,
				price: price,
				quantity: self.cart.code.quantity + 1
			}

		return 'Product added successfully'

	def remove(self, code):
		if self.cart[code]:
			del self.cart[code]
			return 'Product removed successfully'
		else:
			return 'Product not found'

	def checkout(self):
		total = 0
		#print('Code - Name - Quantity - Price')
		#for el in self.cart.items():
 		#	print(el.code, el.name, el.quantity, el.price)
 		#	total += (el.price * el.quantity)
 		#print(f'Total: {total}U$D')


userMenu = {
	'cart add [code]': 'Add product to cart',
    'cart remove [code]': 'Remove product to cart',
    'cart checkout': 'Make checkout',
  	'mode admin': 'Go to admin menu',
    'exit': 'Exit',
}

adminMenu = {
	'list add [data]': 'Add product to list',
	'list get': 'Get all products from list',
	'list get [code]': 'Get a product from list by code',
	'list update [code] [data]': 'Update product from list',
	'mode user': 'Go to normal user menu',
	'exit': 'Delete product from list',
}

def printUserMenu():
    for key in userMenu.keys():
        print(key, '--', userMenu[key])

#def printAdminMenu():
#	for key in adminMenu.keys():
#        print(key, '--', adminMenu[key])

while True:
	printUserMenu()
	cart = Cart()

	cmd = input('Enter a command: ')

	if cmd == 'exit':
		break
	if cmd[:9] == 'cart add ':
		productCode = cmd[9:]
		print('product_code--' + productCode)
	if cmd[:12] == 'cart remove ':
		productCode = cmd[12:]
		print('product_code--' + productCode)
	if cmd == 'cart checkout':
		cart.checkout()