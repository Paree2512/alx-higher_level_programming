#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    list_divide = []

    for i in range(list_length):
        divide = 0

        try:
            divide = my_list_1[i] / my_list_2[i]
        except (ValueError, ZeroDivisionError):
            print("division by 0")
            divide = 0
        except (TypeError):
            print("wrong type")
            divide = 0
        except (IndexError):
            print("out of range")
            divide = 0

        finally:
            list_divide.append(div)

    return list_divide
