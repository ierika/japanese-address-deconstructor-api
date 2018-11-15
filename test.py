from parser.address_parser import AddressParser


if __name__ == "__main__":
    deconstructed = AddressParser(
            "121-9932北海道札幌市手稲区曙11条2丁目3番12号buiidididi123f"
    )
    print(deconstructed.input_address)
    print(deconstructed.get_output_components())
