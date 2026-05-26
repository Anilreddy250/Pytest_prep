def test_invoice_generation(premium_user):
    # This file gets access to the exact same premium_user fixture definition
    # print(assert premium_user["id"] == 42)

    user_id = premium_user["id"]

    assert user_id == 42
    print(premium_user["id"])
# 