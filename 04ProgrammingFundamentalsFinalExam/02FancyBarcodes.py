import re

barcodes_count = int(input())
pattern = r"@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+"
valid_barcodes = []

for _ in range(barcodes_count):
    barcode = input()
    result = re.search(pattern, barcode)
    if result:
        product_group = ""
        for char in result.group(0):
            if char.isdigit():
                product_group += char
        if product_group == "":
            print("Product group: 00")
        else:
            print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
