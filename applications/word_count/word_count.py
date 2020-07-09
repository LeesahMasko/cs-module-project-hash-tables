def word_count(s):
    # Your code here
    cache = {}
    string = s.lower()
    if "" == string:
        return cache
    ignor_char = "\":;,.-+=/\\|[]{}()*^&"
    char_whitespace = "\t\r\n"

    for char in ignor_char:
        string = string.replace(char,"")
    for char in char_whitespace:
        string = string.replace(char," ")

    list_ofwords = string.split(" ")

    for word in list_ofwords:
        if word != "":
            if word in cache:
                cache[word] += 1
            else:
                cache[word] = 1
    print(cache)
    return cache





if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
