# min 2 funkcje
# Fn outer zwraca deklaracje fn inner
# Fn inner musi uzywac identyfikatora (zmienne , fn , cls ) z fn outer

# Pros
# stateful - persystentna ( trwaly )

# cons
# possible memory leak



def sentence(name):
    ax = 42
    def inner(city):
        return f'My name is {name}{ax} and i come from {city}'

    return inner

# full_sentence = sentence('Jaro')
# print(full_sentence.__closure__[0].cell_contents)
# print(full_sentence.__closure__[1].cell_contents)
# print([x.cell_contents for x in full_sentence.__closure__])
# sent = full_sentence('Warsaw')
# sent2 = full_sentence('Krakow')
# print(sent)
# print(sent2)

# Factory function

def power_10(n):
    return n ** 10

def power_11(n):
    return n ** 11

def factory_power(exponent):
    def inner(n):
        return n ** exponent

    return inner


power_2 = factory_power(2)
power_3 = factory_power(3)

# for number in range(1, 10):
#     exec(f'power_{number} = factory_power(number)')










