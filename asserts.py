# def count_upper_case(message):
# 	count = 0
# 	for c in message:
# 		if c.isupper():
# 			count += 1
# 	return count


def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])


assert count_upper_case("") == 0, "Empty String should return 0"
assert count_upper_case("A") == 1, "'A' Should return 1"
assert count_upper_case("aaa") == 0, "Lowercase should return 0"
assert count_upper_case("!$%^@&") == 0, "Special characters should return 0"
assert count_upper_case("TYU") == 3, "Should return count of upper case letters"
assert count_upper_case("   ") == 0, "Spaces should return 0"

print("ALL TESTS PASS")





