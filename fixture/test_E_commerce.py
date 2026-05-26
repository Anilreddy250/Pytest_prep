import pytest

# The function we want to test
def calculate_discount(price: float, coupon: str) -> float:
    if coupon == "WELCOME10":
        return price * 0.90
    elif coupon == "SUMMER20":
        return price * 0.80
    elif coupon == "FREEPASS":
        return 0.0
    return price

# The Must-Know Pytest Concept
@pytest.mark.parametrize(
    "original_price, coupon_code, expected_price",
    [
        (100.0, "WELCOME10", 90.0),   # Case 1: 10% off
        (100.0, "SUMMER20", 80.0),    # Case 2: 20% off
        (50.0, "FREEPASS", 0.0),      # Case 3: 100% off
        (100.0, "INVALID", 100.0),    # Case 4: No discount for bad coupon
    ]
)
def test_calculate_discount(original_price, coupon_code, expected_price):
    assert calculate_discount(original_price, coupon_code) == expected_price