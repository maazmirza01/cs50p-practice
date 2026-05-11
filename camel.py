
def main():
    name = input("Enter a Variable's Name: ")
    name_list = list(name)
    sep_namelist = str_separator(name_list)
    final = joiner(sep_namelist, name_list)
    print(final)


def str_separator(list):
    n = word_counter(list)
    i = 0
    

    namelist = []
    for num in range(n):
        namelist.append("")

        while True and i < letter_count(list):
            if str(list[i]).islower():
                namelist[num] = namelist[num] + list[i]
                i += 1
            else:
                list[i] = str(list[i]).lower()

                break
            
    return namelist

def word_counter(list):
    c = 1
    n = 0
    for _ in list:
        if str(list[n]).isupper():
            c = c + 1
        n += 1
    return c



def letter_count(list):
    i = 0
    for item in list:
        i += 1
    return i

def joiner(wordlist, letterlist):
    n = word_counter(letterlist)
    i = 0
    word_complete = ""
    for c in wordlist:
        word_complete = word_complete + c
        i += 1
        if i <= n:
            word_complete = word_complete + "_"
        
    
    return word_complete








main()


















