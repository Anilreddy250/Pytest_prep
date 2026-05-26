import pytest

@pytest.fixture(scope="session")
def db_connection():
    """Sets up a database connection once for the entire test run."""
    print("\n[Setup] Connecting to Database...")
    db = {"url": "localhost:5432", "status": "connected"}
    yield db
    print("\n[Teardown] Closing Database Connection...")

@pytest.fixture
def premium_user():
    """Provides a fresh premium user dictionary for individual tests."""
    return {"id": 42, "username": "alex_premium", "tier": "premium"}