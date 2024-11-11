def int_division(x,y):
    """
    Task:
    - Perform integer division of 7 by 2.
    
    Return:
    - The result of the division (integer).

    """
   ans = 7 / 2
   return int(ans)
 


def float_multiplication(x,y):
    """
    Task:
    - Multiply 3.0 by 2.
    
    Return:
    - The result of the multiplication (float).
    """
    ans = 3.0 * 2
    return float(ans)
    
 


def combine_operations():
    """
    Task:
    - Add the result of integer division and multiplication.
    
    Return:
    - The combined result (float).
    """
    a = 4 / 2
    b =  2 * 4
    return sum(a,b)


def extract_word():
    """
    Task:
    - Extract the word 'awesome' from the string 'Python is awesome!'.
    
    Return:
    - The extracted word ('awesome').
    """
    string = 'Python is awesome!'
    return  string[2]
    


def to_lowercase():
    """
    Task:
    - Convert the string 'Python is awesome!' to lowercase.
    
    Return:
    - The lowercase version of the string.
    """
    string = 'Python is awesome!'
    return string.lower()


def count_o():
    """
    Task:
    - Count how many times the letter 'o' appears in the string 'Python is awesome!'.
    
    Return:
    - The count of the letter 'o'.
    """
    
    string = 'Python is awesome!'
    count = 0
    for i in string:
        if 'o' in string:
            count += 1
    return count        


def evaluate_boolean():
    """
    Task:
    - Evaluate the expression 'not (5 > 3) and (10 == 5 * 2)'.
    
    Return:
    - The boolean result of the expression.
    """
    
  
