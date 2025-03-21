def solution(phone_book):
    phone_dict = {}

    for number in phone_book:
        phone_dict[number] = True

    for number in phone_book:
        temp = ""
        for digit in number[:-1]:
            temp += digit
            if temp in phone_dict:
                return False

    return True