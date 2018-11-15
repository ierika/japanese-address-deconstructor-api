import re

from parser.japanese_parser import zen2han, kan2num
from parser.prefectures import PREFECTURES


class AddressParser:
    """Parse address into components"""
    postal_code = ""
    prefecture = ""
    city = ""
    street_address = ""
    floor_number = ""
    unit_number = ""

    def __init__(self, input_address):
        """Take input address"""
        self.input_address = input_address
        self.parse()

    def parse(self):
        """Deconstruct Japanese address"""
        value = self.input_address

        # Convert Kanji numerals to digits
        kanji_number_match = re.findall(r"[ー二三四五六七八九十〇]", value)
        for match in kanji_number_match:
            value = value.replace(match, kan2num(match))

        # Convert full-on kanji block-lot numbers
        value = re.sub(r"(\d+)丁目(\d+)番(\d+)号", r"\1-\2-\3", value)

        # Convert chome kanji to hyphen
        value = re.sub(r"(\d+)丁目", r"\1-", value)

        # Converts all full-width digits to half-width
        full_width_match = re.findall(r"[０-９−ー]", value)
        for match in full_width_match:
            value = value.replace(match, zen2han(match))
        value = value.replace("−", "-")

        # Get postal code and strip
        post_code_match = re.search(r"\d{3}-?\d{4}", value)
        if post_code_match:
            self.postal_code = post_code_match.group(0)
            value = value.replace(self.postal_code, "")

        # Get prefecture and strip
        def get_prefecture(x):
            for pref in PREFECTURES:
                re_match = re.search(r"{}".format(pref), x)
                if re_match:
                    return pref
            return None

        prefecture = get_prefecture(value)
        if prefecture:
            value = value.replace(prefecture, "")
            self.prefecture = prefecture

        # Get the city and strip
        city_match = re.search(r"(.+?[区市郡])(.+)", value)
        if city_match:
            city, remainder = city_match.groups()
            self.city = city.strip()
            value = remainder.strip()

        # Get floor and strip
        floor_match = re.search(r"(\d+)\s?[階Ff]", value)
        if floor_match:
            self.floor_number = floor_match.group(1) + 'F'
            value = value.replace(floor_match.group(0), "").strip()

        # Remainder as the street address
        self.street_address = re.sub(r"\s", "", value)

    def get_output_components(self):
        """Output cleaned address components into a dictionary"""
        return {
            "postal_code": self.postal_code,
            "prefecture": self.prefecture,
            "city": self.city,
            "street_address": self.street_address,
            "floor_number": self.floor_number,
        }

    def get_clean_address(self):
        """Concatenate output components into a string"""
        address = "{postal_code}{prefecture}{city}{street_address}".format(
            postal_code=self.postal_code,
            prefecture=self.prefecture,
            city=self.city,
            street_address=self.street_address,
        )
        address += self.floor_number

        return address
