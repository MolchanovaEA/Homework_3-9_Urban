calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    count_calls()
    return(len(string), string.upper(), string.lower())


def is_contains(string, list_to_search):
    string_lower = string.lower()
    is_contains = any(string_lower == item.lower() for item in list_to_search)
    count_calls()
    return is_contains

print(string_info('Fam'))
print(string_info('Колбаска'))
print(is_contains('mama',['haha','papa','mama']))
print(is_contains('mama',['haha','papa','maman']))
print(is_contains('mama',['haha','papa','MaMa']))
print(calls)