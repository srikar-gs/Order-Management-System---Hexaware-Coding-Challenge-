class Product:
    def __init__(self, productId, productName, description, price, quantityInStock, type, **kwargs):
        self.productId = productId
        self.productName = productName
        self.description = description
        self.price = price
        self.quantityInStock = quantityInStock
        self.type = type

        # Additional attributes for Electronics products
        if type.lower() == "electronics":
            self.brand = kwargs.get("brand", "")
            self.warrantyPeriod = kwargs.get("warrantyPeriod", 0)

        # Additional attributes for Clothing products
        elif type.lower() == "clothing":
            self.size = kwargs.get("size", "")
            self.color = kwargs.get("color", "")

    def getProductId(self):
        return self.productId
    def setProductId(self, productId):
        self.productId = productId

    def getProductName(self):
        return self.productName
    def setProductName(self, productName):
        self.productName = productName

    def getDescription(self):
        return self.description
    def setDescription(self, description):
        self.description = description

    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price

    def getQuantityInStock(self):
        return self.quantityInStock
    def setQuantityInStock(self, quantityInStock):
        self.quantityInStock = quantityInStock

    def getType(self):
        return self.type
    def setType(self, type):
        self.type = type


class Electronics(Product):
    def __init__(self, productId, productName, description, price, quantityInStock, brand, warrantyPeriod):
        super().__init__(productId, productName, description, price, quantityInStock, "Electronics")
        self.brand = brand
        self.warrantyPeriod = warrantyPeriod

    def getBrand(self):
        return self.brand
    def getWarrantyPeriod(self):
        return self.warrantyPeriod

    def setBrand(self, brand):
        self.brand = brand
    def setWarrantyPeriod(self, warrantyPeriod):
        self.warrantyPeriod = warrantyPeriod

class Clothing(Product):
    def __init__(self, productId, productName, description, price, quantityInStock, size, color):
        super().__init__(productId, productName, description, price, quantityInStock, "Clothing")
        self.size = size
        self.color = color

    def getSize(self):
        return self.size
    def getColor(self):
        return self.color

    def setSize(self, size):
        self.size = size
    def setColor(self, color):
        self.color = color
        
class User:
    def __init__(self, userId, username, password, role):
        self.userId = userId
        self.username = username
        self.password = password
        self.role = role

    def getUserId(self):
        return self.userId
    def setUserId(self, userId):
        self.userId = userId

    def getUsername(self):
        return self.username
    def setUsername(self, username):
        self.username = username

    def getPassword(self):
        return self.password
    def setPassword(self, password):
        self.password = password

    def getRole(self):
        return self.role
    def setRole(self, role):
        self.role = role

class Order:
    def __init__(self, orderId, userId, productId, quantity, orderDate):
        self.orderId = orderId
        self.userId = userId
        self.productId = productId
        self.quantity = quantity
        self.orderDate = orderDate

    def getOrderId(self):
        return self.orderId
    def setOrderId(self, orderId):
        self.orderId = orderId

    def getUserId(self):
        return self.userId
    def setUserId(self, userId):
        self.userId = userId

    def getProductId(self):
        return self.productId
    def setProductId(self, productId):
        self.productId = productId

    def getQuantity(self):
        return self.quantity
    def setQuantity(self, quantity):
        self.quantity = quantity

    def getOrderDate(self):
        return self.orderDate
    def setOrderDate(self, orderDate):
        self.orderDate = orderDate
