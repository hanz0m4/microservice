def function(s1, strings):
    return [x for x in strings if s1(x)]


a = lambda x: ' ' not in x
b = lambda x: not x.startswith('a')
c = lambda x: len(x) >= 5


m1 = ["polytech", "banan", "lampa", "Darth Vader", "ananas", " ", "star wars", "samolet"]


filtered_strings = function(a, m1)
print("Строки без пробелов:", filtered_strings)


filtered_strings = function(b, m1)
print("Строки, не начинающиеся с 'a':", filtered_strings)


filtered_strings = function(c, m1)
print("Строки длиной не менее 5 символов:", filtered_strings)
