from typing import List     # typing is a built-in Python module used to specify data types of variables, function inputs

class Product:
    def __init__(self, name: str, price: float, popularity: int):
        self.name = name
        self.price = price
        self.popularity = popularity

    def __repr__(self):
        return f"{self.name} - Price: {self.price}, Popularity: {self.popularity}"


def sort_products(products: List[Product], criteria: str) -> List[Product]:
    """
    Sort the list of products based on the specified criteria.
    """

    if criteria == "price":
        return sorted(products, key=lambda x: x.price)

    elif criteria == "popularity":
        return sorted(products, key=lambda x: x.popularity, reverse=True)

    elif criteria == "alphabetical":
        return sorted(products, key=lambda x: x.name)

    else:
        raise ValueError("Invalid sorting criteria")


# Example usage
if __name__ == "__main__":
    products = [
        Product("Laptop", 999.99, 8),
        Product("Smartphone", 499.99, 10),
        Product("Headphones", 199.99, 7),
        Product("Smartwatch", 299.99, 5)
    ]

    print(" Original list of products:")
    for product in products:
        print(product)

    print("\nProducts sorted by popularity:")
    for product in sort_products(products, "popularity"):
        print(product)

    print("\nProducts sorted alphabetically:")
    for product in sort_products(products, "alphabetical"):
        print(product)  

    sorted_by_price = sort_products(products, "price")
    print("\nSorted by price:") 
    for product in sorted_by_price:
        print(product) 
    
    sorted_by_popularity = sort_products(products, "popularity")
    print("\nSorted by popularity:") 
    for product in sorted_by_popularity:
        print(product)

    sorted_alphabetically = sort_products(products, "alphabetical")
    print("\nSorted alphabetically:") 
    for product in sorted_alphabetically:
        print(product)