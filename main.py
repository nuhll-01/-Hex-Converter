# Developer: ToastyyX
# A python script that converts a positive or zero decimal value into its hexadecimal representation.


class HexadecimalConverter:
    default_value = 0

    # A default constructor which instantiates an empty list when the object is created.
    def __init__(this):
        # Create the list.
        this.__my_list = []
        pass

    # The starting point of the script - prompt the user for the value and check for any exceptions.
    # Call the converter to convert the decimal into a hexadecimal value.
    def start(this):
        print('Enter a (non-negative) decimal value: ')
        try:
            decimal_value = int(input())
            this.__convert_to_hexadecimal(decimal_value)
        except Exception:
            raise ValueError('Invalid Value.')

    # When given a decimal that is greater than or equal to 0,
    # add the remainder onto the list and display its contents.
    # If the given decimal value is less than 0, exit the function.

    # 'value' - The (non-negative) decimal value.
    def __convert_to_hexadecimal(this, decimal_value):
        if decimal_value < 0 or not isinstance(decimal_value, int):
            raise ValueError('Invalid Value.')
        if decimal_value == 0:
            print(this.default_value)

        original_value = decimal_value
        dividend = decimal_value
        divisor = 16
        hex_letter_mapping = {
            10: 'A',
            11: 'B',
            12: 'C',
            13: 'D',
            14: 'E',
            15: 'F'
        }

        while dividend > 0:
            # Calculate the remainder of the current dividend value.
            remainder = dividend % divisor
            # Update the dividend.
            dividend //= divisor

            # Check for the case when you're dealing with a value greater than or equal to 10.
            if remainder >= 10:
                # If the condition is met, the remainder is assigned its letter value representation (A-F).
                remainder = hex_letter_mapping[remainder]
            # Add the remainder onto the list.
            this.__my_list.append(remainder)
            # A special case, if the dividend is equal to '0', add '0' to the list along with the 'x' notation.
            if dividend == 0:
                this.__my_list.append('x')
                this.__my_list.append(dividend)
        this.__my_list.reverse()
        this.__print_hexadecimal(original_value)

    # Display the contents of the list formatted in a hexadecimal fashion.
    def __print_hexadecimal(this, x):
        print('\n--------------')
        print('Decimal Value: ', x)
        for i in range(len(this.__my_list)):
            if this.__my_list[i] is this.__my_list[0]:
                print('Hexadecimal Value:', this.__my_list[i], end='')
            else:
                print(this.__my_list[i], end='')

    # Magic Method (Don't even know what this is doing to my program, might be irrelevant?).
    def __gt__(this, other):
        return this.__my_list > other.__my_array


if __name__ == '__main__':
    converter = HexadecimalConverter()
    converter.start()
