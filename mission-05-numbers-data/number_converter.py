"""Interactive decimal, binary, and hexadecimal number converter."""


def convert_number(value: str, source_base: int, target_base: int) -> str:
    """Convert a non-negative integer string between bases 2, 10, and 16."""
    number = int(value.strip(), source_base)
    if number < 0:
        raise ValueError("Please enter a non-negative integer.")
    if target_base == 2:
        return format(number, "b")
    if target_base == 10:
        return str(number)
    if target_base == 16:
        return format(number, "X")
    raise ValueError("Supported target bases are 2, 10, and 16.")


def main() -> None:
    print("Number Converter (binary / decimal / hexadecimal)")
    bases = {"2": 2, "binary": 2, "10": 10, "decimal": 10,
             "16": 16, "hex": 16, "hexadecimal": 16}

    try:
        source = input("Convert from (2/binary, 10/decimal, 16/hex): ").strip().lower()
        target = input("Convert to (2/binary, 10/decimal, 16/hex): ").strip().lower()
        if source not in bases or target not in bases:
            raise ValueError("Choose a supported source and target base.")

        value = input("Enter a non-negative integer: ")
        result = convert_number(value, bases[source], bases[target])
        print(f"Result: {result}")
    except ValueError as error:
        print(f"Input error: {error}")


if __name__ == "__main__":
    main()
