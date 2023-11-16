class Catalogue:
    def __init__(self, name=str):
        self.name = name
        self.products = []

    def add_product(self, product_name=str):
        # self.product_name = product_name
        self.products.append(product_name)

    def get_by_letter(self, first_letter=str):
        list_by_letter = [product for product in self.products if product[0] == first_letter]
        # list_by_letter = []
        # for product in self.products:
        #   if product[0] == first_letter:
        #     list_by_letter.append(product_name)

        return list_by_letter

    def __repr__(self):
        sorted_list = sorted(self.products)
        result = "\n".join(sorted_list)
        return f"Items in the {self.name} catalogue:\n{result}"