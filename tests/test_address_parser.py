import unittest

from parser.address_parser import AddressParser


class TestAddressParser(unittest.TestCase):
    """Test Japanese address parser"""

    def test_should_convert_kanji_to_number_1(self):
        """It should convert kanji of 1 to numeric value"""
        result = AddressParser(
            "1210064 神奈川県横浜市青葉区青葉台一丁目9-2-406 ２階"
        )
        result = result.get_output_components()
        self.assertTrue("1-" in result["street_address"])

    def test_should_convert_kanji_to_number_2(self):
        """It should convert kanji of 2 to numeric value"""
        result = AddressParser(
            "1210064 神奈川県横浜市青葉区青葉台二丁目9-2-406 ２階"
        )
        result = result.get_output_components()
        self.assertTrue("2-" in result["street_address"])

    def test_should_convert_kanji_to_number_3(self):
        """It should convert kanji of 3 to numeric value"""
        result = AddressParser(
            "1310064 神奈川県横浜市青葉区青葉台三丁目9-3-406 ２階"
        )
        result = result.get_output_components()
        self.assertTrue("3-" in result["street_address"])

    def test_should_convert_kanji_to_number_4(self):
        """It should convert kanji of 4 to numeric value"""
        result = AddressParser(
            "1410064 神奈川県横浜市青葉区青葉台四丁目9-4-406 ２階"
        )
        result = result.get_output_components()
        self.assertTrue("4-" in result["street_address"])

    def test_should_convert_kanji_to_number_5(self):
        """It should convert kanji of 5 to numeric value"""
        result = AddressParser(
            "1510065 神奈川県横浜市青葉区青葉台五丁目9-5-506 ２階"
        )
        result = result.get_output_components()
        self.assertTrue("5-" in result["street_address"])

    def test_should_convert_kanji_to_number_6(self):
        """It should convert kanji of 6 to numeric value"""
        result = AddressParser(
            "1610066 神奈川県横浜市青葉区青葉台六丁目9-6-606 ２階"
        )
        result = result.get_output_components()
        self.assertTrue("6-" in result["street_address"])

    def test_should_convert_kanji_to_number_7(self):
        """It should convert kanji of 7 to numeric value"""
        result = AddressParser(
            "1710077 神奈川県横浜市青葉区青葉台七丁目9-7-707 ２階"
        )
        result = result.get_output_components()
        self.assertTrue("7-" in result["street_address"])

    def test_should_convert_kanji_to_number_8(self):
        """It should convert kanji of 8 to numeric value"""
        result = AddressParser(
            "181008 神奈川県横浜市青葉区青葉台八丁目9-8-808 ２階"
        )
        result = result.get_output_components()
        self.assertTrue("8-" in result["street_address"])

    def test_should_convert_kanji_to_number_9(self):
        """It should convert kanji of 9 to numeric value"""
        result = AddressParser(
            "191009 神奈川県横浜市青葉区青葉台九丁目9-9-909 ２階"
        )
        result = result.get_output_components()
        self.assertTrue("9-" in result["street_address"])

    def test_should_convert_kanji_floor_numbers_to_alphanum(self):
        """It should convert kanji floor numbers to alphanumeric"""
        result = AddressParser(
            "1310064 神奈川県横浜市青葉区青葉台三丁目9-3-406 ２階"
        )
        result = result.get_output_components()
        self.assertEqual("2F", result["floor_number"])

    def test_should_detect_postal_codes(self):
        """It should detect postal codes with 6 to 7 digits and should
        hyphenate it.
        """
        result = AddressParser(
            "1310064 神奈川県横浜市青葉区青葉台三丁目9-3-406 ２階"
        )
        result = result.get_output_components()
        self.assertEqual("131-0064", result["postal_code"])

    def test_should_detect_prefectures(self):
        """It should be able to detect prefectures

        eg. 東京都、神奈川県
        """
        result = AddressParser(
            "1310064 神奈川県横浜市青葉区青葉台三丁目9-3-406 ２階"
        )
        result = result.get_output_components()
        self.assertEqual("神奈川県", result["prefecture"])

    def test_should_detect_city_ward(self):
        """It should detect cities or wards

        After prefecture has been stripped. Cities should be detected by
        finding 区、市、群
        """
        result = AddressParser(
            "1310064 神奈川県横浜市青葉区青葉台三丁目9-3-406 ２階"
        )
        result = result.get_output_components()
        self.assertEqual("横浜市", result["city"])

    def test_should_detect_city_city(self):
        """It should detect cities or wards

        After prefecture has been stripped. Cities should be detected by
        finding 区、市、群
        """
        result = AddressParser(
            "1310064 神奈川県横浜区青葉区青葉台三丁目9-3-406 ２階"
        )
        result = result.get_output_components()
        self.assertEqual("横浜区", result["city"])

    def test_should_detect_city_gun(self):
        """It should detect cities or wards

        After prefecture has been stripped. Cities should be detected by
        finding 区、市、郡
        """
        result = AddressParser(
            "1310064 神奈川県横浜郡青葉区青葉台三丁目9-3-406 ２階"
        )
        result = result.get_output_components()
        self.assertEqual("横浜郡", result["city"])
