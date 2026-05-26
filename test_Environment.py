import pytest
class ShoppingCart:
    def __init__(self, user: dict):
        self.user = user          # Stores user info, e.g., {"username": "test_user", "tier": "premium"}
        self.items = []           # Keeps track of items as a list of dictionaries
        self.total_price = 0.0
        self.total_items = 0

    def add_item(self, item_name: str, price: float):
        """Adds an item to the cart and updates totals."""
        self.items.append({"name": item_name, "price": price})
        self.total_items += 1
        self.total_price += price

    def apply_discounts(self):
        """Applies a 10% discount if the user belongs to the 'premium' tier."""
        if self.user.get("tier") == "premium":
            self.total_price = self.total_price * 0.90
# 1. We define a fixture using the decorator
@pytest.fixture
def empty_cart():
    """Sets up a realistic environment: a fresh, empty shopping cart for a test user."""
    # Setup phase
    
    user = {"username": "test_user", "tier": "premium"}
    cart = ShoppingCart(user=user) 
    
    return cart # This is what gets passed to the test

# 2. We inject the fixture into our tests by matching its name as an argument
def test_add_first_item(empty_cart):
    # Notice how 'empty_cart' is already available and ready to use!
    empty_cart.add_item("Wireless Mouse", price=25.00)
    
    assert empty_cart.total_items == 1
    assert empty_cart.total_price == 25.00

def test_premium_user_discount(empty_cart):
    # This test gets a completely fresh, brand-new cart instance too
    empty_cart.add_item("Mechanical Keyboard", price=100.00)
    empty_cart.apply_discounts()
    
    # Premium users get 10% off
    assert empty_cart.total_price == 90.00
# import pytest

@pytest.mark.shopping_cart  # <--- Labeling the test
def test_premium_user_discount(empty_cart):
    print("Shopping_cart is full no space")
    ...

