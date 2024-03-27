import sys
sys.path.append("C:\\Users\\srika\\OneDrive\\Desktop\\Hexaware\\TECHNICAL FOUNDATION - PYTHON\\PYTHON\\CODING CHALLENGES\\OrderManagementSystem")

from dao.order_processor import OrderProcessor
from entity.model import User, Electronics, Clothing
from datetime import date
from exception.custom_exceptions import UserNotFoundException, UnauthorizedAccess

class OrderManagement:
    @staticmethod
    def main():
        while True:
            print("\nMenu:")
            print("1. Create User")
            print("2. Create Product")
            print("3. Create Order")
            print("4. Cancel Order")
            print("5. Get All Products")
            print("6. Get Orders by User")
            print("7. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                OrderManagement.create_user()
            elif choice == "2":
                OrderManagement.create_product()
            elif choice == "3":
                OrderManagement.create_order()
            elif choice == "4":
                OrderManagement.cancel_order()
            elif choice == "5":
                OrderManagement.get_all_products()
            elif choice == "6":
                OrderManagement.get_orders_by_user()
            elif choice == "7":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def create_user():
        # Implement logic to collect user details and create a new user
        userId = int(input("Enter user ID: "))
        username = input("Enter username: ")
        password = input("Enter password: ")
        role = input("Enter role (Admin/User): ")
        
        user = User(userId, username, password, role)
        OrderProcessor().createUser(user)
        print("User created successfully.")

    @staticmethod
    def create_product():
        # Collect user details
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        # Fetch user details from the database based on username and password
        user = OrderProcessor().getUserByUsernameAndPassword(username, password)
        if user is None:
            raise UserNotFoundException("Invalid username or password. User not found.")
        
        # Check if the user is an admin
        try:
            if user.getRole() != "Admin":
                raise UnauthorizedAccess()
        except UnauthorizedAccess as e:
            print(e)  
            return
        
        # Collect product details
        productId = int(input("Enter product ID: "))
        productName = input("Enter product name: ")
        description = input("Enter product description: ")
        price = float(input("Enter product price: "))
        quantityInStock = int(input("Enter quantity in stock: "))
        productType = input("Enter product type (Electronics/Clothing): ")
        
        if productType.lower() == "electronics":
            brand = input("Enter brand: ")
            warrantyPeriod = int(input("Enter warranty period: "))
            product = Electronics(productId, productName, description, price, quantityInStock, brand, warrantyPeriod)
        elif productType.lower() == "clothing":
            size = input("Enter size: ")
            color = input("Enter color: ")
            product = Clothing(productId, productName, description, price, quantityInStock, size, color)
        else:
            print("Invalid product type.")
            return
        
        OrderProcessor().createProduct(user, product)
        print("Product created successfully.")

    @staticmethod
    def create_order():
        # Collect user details
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        # Fetch user details from the database based on username and password
        user = OrderProcessor().getUserByUsernameAndPassword(username, password)
        try:
            if user is None:
                raise UserNotFoundException()
        except UserNotFoundException as e:
            print(e,'Create New User')
            return

        # Collect product details
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity: "))
        order_date = date.today()
        
        # Create the order
        OrderProcessor().createOrder(user, product_id, quantity, order_date)
        print("Order created successfully.")

    @staticmethod
    def cancel_order():
        # to cancel an existing order
        userId = int(input("Enter user ID: "))
        orderId = int(input("Enter order ID: "))
        
        OrderProcessor().cancelOrder(userId, orderId)
        print("Order canceled successfully.")

    @staticmethod
    def get_all_products():
        # to retrieve and display all products
        products = OrderProcessor().getAllProducts()
        if products:
            print("All Products:")
            for product in products:
                print("Product ID:", product.getProductId())
                print("Product Name:", product.getProductName())
                print("Description:", product.getDescription())
                print("Price:", product.getPrice())
                print("Quantity In Stock:", product.getQuantityInStock())
                print("Category:", product.getType())
                print() 
        else:
            print("No products found.")

    @staticmethod
    def get_orders_by_user():
        # to retrieve and display orders placed by a specific user
        user_id = int(input("Enter user ID: "))
        user = User(user_id, "", "", "")  
        orders = OrderProcessor().getOrderByUser(user)
        if orders:
            print(f"Orders placed by user {user_id}:")
            for order in orders:
                print("Order ID:", order[0])
                print("User ID:", order[1])
                print("Product ID:", order[2])
                print("Order Date:", order[3])
                print()  
        else:
            print(f"No orders found for user {user_id}.")

if __name__ == "__main__":
    OrderManagement.main()