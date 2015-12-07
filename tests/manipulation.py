# NUMBERS

# create function that returns True if even


def is_even(x):
    return x % 2 == 0


# create function returns True if int. include if decimal part .0 e.g. 7.0


def is_int(x):
    return int(x) == x


# return sum of digits. Assume int parameter only


def digits_sum(x):
    total = 0
    for num in str(x):
        total += int(num)
    return total


# return factorial

def factorial(x):
    total = 1
    for i in range(1, x + 1):
        total *= i
    return total

# return true if prime number


def is_prime(x):
    if x <= -1:
        return False
    for n in range(2, x):
        if x % n == 0:
            return False
    return True


# STRINGS
# reverse a word without using reverse
def reverse(word):
    output = ''
    for char in word:
        output = char + output
    return output


def reverse2(word):
    output = ''
    for char in word[::-1]:
        output += char
    return output


# remove vowels from a text string. remove upper and lower case


def anti_vowel(word):
    output = ''
    for char in word:
        if char.lower() not in 'aeiou':
            output += char
    return output


# get scabble score for given word using dictionary. Forget about double or triple scores
scrabble_score = {'a': 1, 'c': 3, 'b': 3, 'e': 1, 'd': 2, 'g': 2,
                  'f': 4, 'i': 1, 'h': 4, 'k': 5, 'j': 8, 'm': 3,
                  'l': 1, 'o': 1, 'n': 1, 'q': 10, 'p': 3, 's': 1,
                  'r': 1, 'u': 1, 't': 1, 'w': 4, 'v': 4, 'y': 4,
                  'x': 8, 'z': 10}


def scrabble(word):
    total = 0
    for char in word.lower():
        total += scrabble_score[char]
    return total


def scrabble2(word):
    return sum(scrabble_score[letter] for letter in word.lower())

# censor the first string with the 2nd string. censor with stars


def censor(words, censor_word):
    return words.replace(censor_word, '*' * len(censor_word))

# LISTS
# count occurence of an item in a list
def occurence(sequence, item):
    count = 0
    for s in sequence:
        if s == item:
            count += 1
    return count


# take a list of numbers and remove odd numbers
def remove_odd(sequence):
    out = []
    for item in sequence:
        if item % 2 == 0:
            out.append(item)
    return out


# take list of numbers and return product
def product(sequence):
    total = 1
    for item in sequence:
        total *= item
    return total


def remove_duplicates(sequence):
    distinct = set(sequence)
    return list(distinct)


def remove_duplicates2(sequence):
    out = []
    for item in sequence:
        if item not in out:
            out.append(item)
    return out


# return median value from numeric sequence


def median(sequence):
    if len(sequence) == 1:
        return sequence[0]
    else:
        sort_seq = sorted(sequence)
        len_seq = len(sequence)
        if len_seq % 2 != 0:
            return sort_seq[len_seq / 2]
        else:
            return (sort_seq[len_seq / 2 -1] + sort_seq[len_seq / 2]) / 2.0