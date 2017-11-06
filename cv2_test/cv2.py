def filter_numbers (list):
    return [x for x in list if isinstance(x, int) and not isinstance(x, bool)]


def average_length(list):
    avg_len = 0
    for i in list:
        avg_len += len(i)
    return avg_len / len(list)

def palindrome(string):
    rev_str = string[::-1]
    if string == rev_str:
        return True
    else:
        return False

def overlapping(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

def number_of_letters(string):
    dic = {}
    for i in string:
        if i in dic:
            noa = dic[i]
            dic[i] = noa + 1
        else:
            dic[i] = 1
    return dic
    
        

print(filter_numbers([1.2, "sdas", 4, 8, 3.4, "12", -3, True, 5, 8]))
print(average_length(["olomouc", "liberec", "ostrava", "praha", "brno"]))
print(palindrome("radar"))
print(palindrome("radek"))
print(overlapping([1,2,3], [4,5,6]))
print(overlapping([1,2,3], [3,4,5]))
print(number_of_letters("ababdacabbdabc"))
