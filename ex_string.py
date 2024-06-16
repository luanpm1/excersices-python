if __name__ == '__main__':
    str1 = "This is a string "
    str2 = "Hello python"
    print(str1.title(), str2.lower())

    name = "minh luan"
    string = "my name is {}, from {}".format(name, "viet nam")
    print(string.capitalize())



    # def myString(string, k):
    #     result = string[:k] + string[k + 1:]
    #     return result
    #
    #
    # myF = myString(str1, 5)
    # print(myF)
    #
    # from string import punctuation
    #
    # print(punctuation)
    #
    #
    # def remove_punctuations(str):
    #     for i in punctuation:
    #         return str.replace(i, "")
    #     return str
    #
    #
    # print(remove_punctuations("fdkfdkfjd!djkfj#fdjfj45J#$3fdkdjk"))
