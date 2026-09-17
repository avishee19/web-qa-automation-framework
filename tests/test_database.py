from db.database import create_database, get_product


def test_product_database_validation():

    connection = create_database()

    product = get_product(
        connection,
        "Sauce Labs Backpack"
    )

    assert product is not None

    product_name, price, quantity = product

    assert product_name == "Sauce Labs Backpack"
    assert price == 29.99
    assert quantity == 1

    connection.close()