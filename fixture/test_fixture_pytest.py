import pytest

class DatabaseConnection:
    def __init__(self):
        self.connected = True
    def fetch_user_role(self, user_id):
        return "admin" if user_id == 1 else "guest"
    def close(self):
        self.connected = False

# The Must-Know Pytest Concept
@pytest.fixture
def db_conn():
    """Sets up a database connection before the test, and closes it after."""
    conn = DatabaseConnection()
    yield conn  # This is where the test happens!
    conn.close() # Clean up code runs after the test completes

# Using the fixture by passing its name as an argument
def test_admin_user_role(db_conn):
    assert db_conn.fetch_user_role(1) == "admin"

def test_guest_user_role(db_conn):
    assert db_conn.fetch_user_role(42) == "guest"