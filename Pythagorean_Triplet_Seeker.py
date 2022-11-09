"""
Author: Logan Maupin
Date: 10/08/2022

Description:
This program fins all possible Pythagorean Triples from 0-500
a Pythagorean Triple is a mathematical phenomenon using the
Pythagorean Theorem in which all triangle sides are whole numbers.
In a right triangle, you can use P. Theorem to find the side lengths.
a^2 + b^2 = c^2 -- where a and b are sides and c is the longest side.
So 3^2 + 4^2 = 5^2 ---> 9 + 16 = 25 ---> 25 = 25 :)

##
One way to improve this code would be to find a way to make it not repeat itself.
Even though it doesn't print sets like [3, 4, 5] and [4, 3, 5], that doesn't mean
it's not still doing that operation. It's just that if statement prevents it from being
printed or added to the 2d list. So just a note if you ever want to make this code run
even faster & more efficient than before. This change might be necessary for extremely
large data sets.
"""

import math


def pythagorean_triplet_seeker(int_max):
    """
    This function finds the triples and appends them to a list.

    :param int_max: This is the range you want the function to iterate through.
    so if you put "pythagorean_triplet_seeker(500)" it will find all pairs from 1 to 500.

    :returns: 2d list of triples for use cases if you need it in another function.
    """

    list_1 = range(1, int_max+1)
    list_2 = range(1, int_max+1)

    pythagorean_triples = []

    for a in list_1:
        for b in list_2:
            c_squared = (a**2) + (b**2)
            c = math.sqrt(c_squared)
            c_floor = math.floor(c)
            c_as_an_int_test = c_floor - c
            current_number_set = [a, b, c_floor]
            if c_as_an_int_test == 0.0:
                if [b, a, c_floor] not in pythagorean_triples:
                    pythagorean_triples.append(current_number_set)
                    print(a, b, c_floor)
    return pythagorean_triples


def main():
    pythagorean_triplet_seeker(500)


if __name__ == '__main__':
    main()
