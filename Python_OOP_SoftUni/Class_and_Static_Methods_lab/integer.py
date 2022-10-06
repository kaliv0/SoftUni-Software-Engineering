from math import floor


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(floor(float_value))

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str) or not isinstance(int(value), int):
            return "wrong type"
        return cls(int(value))

    @classmethod
    def from_roman(cls, value: str):
        if not isinstance(value, str):
            raise ValueError("Invalid input!")

        roman_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, }
        result = 0
        prev_num = 0
        for i in reversed(value):
            # curr_num = Integer.parse(i)
            curr_num = roman_nums[i]

            if prev_num > curr_num:
                result -= curr_num
            else:
                result += curr_num
            prev_num = curr_num
        return cls(result)

    # @staticmethod
    # def parse(c: str):
    #     match c:
    #         case "I":
    #             result = 1
    #         case "V":
    #             result = 5
    #         case "X":
    #             result = 10
    #         case "L":
    #             result = 50
    #         case "C":
    #             result = 100
    #         case "D":
    #             result = 500
    #         case "M":
    #             result = 1000
    #         case _:
    #             raise ValueError("Invalid numeral!")
    #     return result


if __name__ == "__main__":
    first_num = Integer(10)
    print(first_num.value)

    second_num = Integer.from_roman("IV")
    print(second_num.value)

    print(Integer.from_float("2.6"))
    print(Integer.from_string(2.6))

    print(Integer.from_roman("XIV").value)
    print(Integer.from_roman("LXIV").value)
    print(Integer.from_roman("CXX").value)
    print(Integer.from_roman("XL").value)
    print(Integer.from_roman("DXXXVI").value)
    print(Integer.from_roman("XIX").value)
    print(Integer.from_roman("IV").value)
    print(Integer.from_roman("XCIX").value)
