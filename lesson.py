def is_prime(n:int) -> bool:
    if n < 2:
        return False
    for i in range(2, int((n ** 0.5)+1)):
        if n%i == 0:
            return False
    print(n)
    return True

def is_palindrom(word:str) -> bool:
    
    length = len(word)-1
    for i in range(len(word)):
        if word[i] == word[length]:
            length -= 1
        else:
            return False
    return True


def main():
    name = "otto"
    car = "audi"
    #print(is_palindrom(name))
    #print(is_palindrom(car))
    my_list = [1,2,4]
    my_list.reverse()
    print(my_list)
   

if __name__ == "__main__":
    main()
    

