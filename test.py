from parser.address_parser import AddressParser


if __name__ == "__main__":
    deconstructed = AddressParser(
            "2270026神奈川県横浜市青葉区青葉台1-9"
    )
    print(deconstructed.input_address)
    print(deconstructed.get_output_components())
