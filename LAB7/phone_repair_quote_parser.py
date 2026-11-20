def mask_imei(imei):
    """Mask a 15-digit IMEI or return an empty string for invalid input."""
    if not isinstance(imei, str):
        return ""
    digits = "".join(imei.split()).replace("-", "")
    if len(digits) != 15 or not digits.isascii() or not digits.isdecimal():
        return ""
    return "*" * 11 + digits[-4:]


def parse_parts_order(text):
    """Parse PART xQTY items or return an empty dictionary for an invalid order."""
    if not isinstance(text, str):
        return {}

    order = {}
    for item in text.split(";"):
        part, separator, quantity = item.rpartition("x")
        part, quantity = part.strip(), quantity.strip()
        if not separator or not part or not quantity.isascii() or not quantity.isdecimal():
            return {}
        try:
            count = int(quantity)
        except ValueError:
            return {}
        if count == 0:
            return {}
        order[part] = count
    return order


def parse_model(text):
    """Return (brand, model) or a pair of empty strings for invalid input."""
    if not isinstance(text, str):
        return "", ""
    fields = text.split(maxsplit=1)
    if len(fields) != 2:
        return "", ""
    brand, model = fields
    return brand.title(), model.strip()


def main():
    print("==== Running mask_imei ====")
    value = input("Enter an IMEI number (e.g. 35-209900-176148-1): ")
    masked = mask_imei(value)
    print("Masked IMEI:", masked or "Invalid IMEI")

    print("\n==== Running parse_parts_order ====")
    value = input("Enter parts and quantities as PART xQTY separated by ; (e.g. screen x1; battery x2): ")
    order = parse_parts_order(value)
    print("Parts order:", order or "Invalid parts order")

    print("\n==== Running parse_model ====")
    value = input("Enter the phone brand and model (e.g. Samsung Galaxy S23): ")
    brand, model = parse_model(value)
    print("Brand and model:", (brand, model) if brand else "Enter both brand and model")

if __name__ == "__main__":
    main()
