txt_first = "Hi"

big = txt_first.capitalize()

print(type(big))
print(big)

txt_second = "HeLLo, AnD WeLcome To My World! 123 "

low = txt_second.casefold()

print(low)

txt_third = "banana"

centre = txt_third.center(20)

print(centre)

txt_fourth = "I love apples, apple are my favorite fruit,аррle"

count = txt_fourth.count("apple")

print(count)

txt_fifth = "My name is Ståleпв"

decode = txt_fifth.encode()

print(decode)

txt_sixth = "Hello, welcome to my world...."

bool_form = txt_sixth.endswith(".....")

print(bool_form)

txt_seventh = "H\td\tdd\tsdd\ts\tldd\tddod"

space_bars = txt_seventh.expandtabs(3)

print(space_bars)

txt_eith = "Hello, welcomew to my world."

searcher = txt_eith.find("w")

print(searcher)

txt_neith = "For only {price:.2f} dollars! Only at {day:.2f} day"
print(txt_neith.format(price = 49, day = 2))

txt_ten = "Hello, welcome to my world."

also_searcher = txt_ten.index("w")

print(also_searcher)

txt_eleven = "Company12п."

alphanumeric_test = txt_eleven.isalnum()

print(alphanumeric_test)

txt_twelve = "CompanyX2"

letters_checker = txt_twelve.isalpha()

print(letters_checker)

txt_thierteen= "\u0211"

unicode_checker = txt_thierteen.isdecimal()

print(unicode_checker)

txt_fourteen = "5d0800"

number_test = txt_fourteen.isdigit()

print(number_test)

txt_fifeteen = "5d0800"

identify_cheacker = txt_fifeteen.isidentifier()

print(identify_cheacker)

txt_sixteen = "hello World!"

lower_checker = txt_sixteen.islower()

print(lower_checker)

txt_seventeen = "5655s43"

numeric_test_second = txt_seventeen.isnumeric()

print(numeric_test_second)

txt_eitheen = "Hello! Are you #1аыва.ю.э=-0фыё~!@?"

printable_test = txt_eitheen.isprintable()

print(printable_test)

txt_nineteen = "  s "

space_bars_checker = txt_nineteen.isspace()

print(space_bars_checker)

txt_twenty = "hello, And Welcome To My World!"

start_every_word_big = txt_twenty.istitle()

print(start_every_word_big)

txt_twenty_one = "ThIS IS NOW!"

letters_capital_checker = txt_twenty_one.isupper()

print(letters_capital_checker)

myTuple = ("John", '   ', "Peter", "Vicky")

fill_spaces = "/".join(myTuple)

print(fill_spaces)

txt_twenty_two = "banana"

words_longer = txt_twenty_two.ljust(-20)

print(words_longer, "is my favorite fruit.")

txt_twenty_three = "Hello my FRIENDS"

do_word_lower = txt_twenty_three.lower()

print(do_word_lower)

txt_twenty_four = "     banana     "

remove_space_right_sides = txt_twenty_four.lstrip()

print("of all fruits", remove_space_right_sides, "is my favorite")

txt_twenty_five = "Hello Sam!"
replace_letter = txt_twenty_five.maketrans("e", "g")
print(txt_twenty_five.translate(replace_letter))

txt_twenty_six = "I could eat bananas all day"

divides_words = txt_twenty_six.partition("bananas")

print(divides_words)

txt_twenty_seven = "I like bananas"

replace_words = txt_twenty_seven.replace("bananas", "bananas")

print(replace_words)

txt_twenty_eith = "Mi casa, su casa."

last_word_searcher = txt_twenty_eith.rfind("asa")

print(last_word_searcher)

txt_twenty_nine = "Mi casa, su casa."

same_like_last = txt_twenty_nine.rindex("asa")

print(same_like_last)

txt_thirty = "bananas"

make_words_longer_left = txt_thirty.rjust(20)

print(make_words_longer_left, "is my favorite fruit.")

txt_thirty_one = "I cousssssld eat bananas all day, bananas are my favorssssite fruit"

again_divides_words = txt_thirty_one.rpartition("bananas")

print(again_divides_words)

txt_thirty_two = "apple, banana, cherry"

split = txt_thirty_two.rsplit(", ")

print(split)

txt_thirty_three = " s    banana  s   "

remove_space_left_sides = txt_thirty_three.rstrip()

print("of all fruits", remove_space_left_sides, "is my favorite")

txt_thirty_four = "welcome s s to the jungle"

split_each_word = txt_thirty_four.split()

print(split_each_word)

txt_thirty_five = "Thank you \nfor the music\nWelcome to the\n jungle"

split_words_with_slashs = txt_thirty_five.splitlines()

print(split_words_with_slashs)

txt_thirty_six = "Hello, welcome to my world."

first_word_checker = txt_thirty_six.startswith("Hells")

print(first_word_checker)

txt_thirty_seven = "  s   banana   s  "

remove_space_both_sides = txt_thirty_seven.strip()

print("of all fruits", remove_space_both_sides, "is my favorite")

txt_thirty_eight = "Hello My Name Is PETER"

swap_capital_lower_letters = txt_thirty_eight.swapcase()

print(swap_capital_lower_letters)

txt_thirty_nine = "Welcome to my world"

make_first_letter_of_words_big = txt_thirty_nine.title()

print(make_first_letter_of_words_big)

replace_letter_ascii_code = {72: 48}
txt_fourtee = "Hello Sam!"
print(txt_fourtee.translate(replace_letter_ascii_code))

txt_fourtee_one = "HelGGGlo my friends"

every_letter_upper = txt_fourtee_one.upper()

print(every_letter_upper)

txt_fourtee_two = "50"

fill_with_zero = txt_fourtee_two.zfill(10)

print(x)