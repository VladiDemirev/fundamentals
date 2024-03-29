from typing import List


class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products: List[str] = []

    def add_product(self, product_name: str) -> None:
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str) -> List[str]:
        return [p for p in self.products if p.startswith(first_letter)]

    def __repr__(self) -> str:
        result = f"Items in the {self.name} catalogue:\n"
        result += "\n".join([i for i in sorted(self.products)])
        return result

#   TEST CODE

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)

