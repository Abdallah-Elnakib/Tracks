
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# squared_evens = list(map(lambda x: x * x, even_numbers))


# def recursive_sum(lst):
#     if not lst:
#         return 0
#     return lst[0] + recursive_sum(lst[1:])


# result = recursive_sum(squared_evens)


# print("Even numbers:", even_numbers)
# print("Squared evens:", squared_evens)
# print("Sum of squared evens:", result)



# *****************************************************************************



# sentence = "Python is a powerful and beautiful programming language"

# words = sentence.split()

# long_words = list(filter(lambda word: len(word) > 5, words))

# upper_words = list(map(lambda word: word.upper(), long_words))

# def print_words_recursively(word_list):
#     if not word_list:
#         return
#     print(word_list[0])
#     print_words_recursively(word_list[1:])

# print_words_recursively(upper_words)
