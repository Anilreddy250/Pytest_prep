def test_create_order(db_connection, premium_user):
    # Pytest automatically finds 'db_connection' and 'premium_user' from conftest.py
    assert db_connection["status"] == "connected"
    assert premium_user["tier"] == "premium"
    print(f"Order created successfully for {premium_user['username']}!")