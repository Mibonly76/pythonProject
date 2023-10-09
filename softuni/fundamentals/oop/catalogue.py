class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.prodict_list = []

    def add_product(self, product_name: str):
        self.prodict_list.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [product for product in self.prodict_list if first_letter == product[0]]

    def __repr__(self):
        returning_string = f"Items in the {self.name} catalogue:\n"
        returning_string += "\n".join(sorted(self.prodict_list))
        return returning_string


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
