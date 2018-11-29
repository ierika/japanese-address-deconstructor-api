from parser.address_parser import AddressParser


if __name__ == "__main__":
    addresses = (
        "107-0062東京都港区南青山5丁目12-3",
        "港区南麻布3-2-13",
        "余市郡赤井川村常盤128-1",
        "渋谷区神宮前4-13-10",
        "中央区湊3-8-1",
        "大阪市住之江区南港東8丁目",
        "常滑市セントレア4丁目",
        "千代田区三崎町2-42-6",
        "世田谷区奥沢6丁目",
        "新宿区西新宿7-7-19",
        "港区南麻布3-5-19",
        "江東区豊洲3-6-5",
    )

    for i in addresses:
        print("-" * 40)
        address = AddressParser(i)
        print(address.input_address)
        print(address.get_output_components())
