def is_prime(number):
    if number < 2:
        return False

    for index in range(1, 100):
        if number % index == 0:
            return False


    return True


is_prime(1)
