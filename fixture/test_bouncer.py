import pytest
# Import the function from our bouncer.py file
from bouncer import check_admission

def test_adult_allowed():
    """Test standard positive case: an adult should be allowed."""
    assert check_admission(25) == "Welcome to the VIP Club!"

def test_minor_denied():
    """Test standard negative case: a minor should be denied."""
    assert check_admission(15) == "Access Denied"

def test_boundary_eighteen():
    """Edge Case: Exactly 18 should be allowed."""
    assert check_admission(18) == "Welcome to the VIP Club!"

def test_boundary_seventeen():
    """Edge Case: Exactly 17 should be denied."""
    assert check_admission(17) == "Access Denied"

def test_negative_age_raises_error():
    """Error Case: A negative age must raise a ValueError with the correct message."""
    with pytest.raises(ValueError, match="Age cannot be negative"):
        check_admission(-5)