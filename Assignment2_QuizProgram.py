print("=================<<< Quiz Program >>>==================")
print("<< Today You have a quiz that is Quiz: 1 >>")
print("=======================================================")
print(">>> Select Your Quiz Name With help of Optional numbers.\n~~Quiz 1 of php press : 1. \n~~Quiz 1 of phython press : 2")
print("=======================================================")
quizName = int(input(">>> Enter the subject that has a quiz: "))

# Here list of PHP Quiz Questions Start.
PHP_Quiz1_List = [["Q1. Which function is used for determining the location of syntax error?",
                   "a. error() \nb. syn_error() \nc. die() \nd. find()", "c"],

                  ["Q2. PHP stands for?",
                   "a. Hypertext Preprocessor \nb. Pretext Hypertext Preprocessor \nc. Personal Home Processor \nd. None of the above", "a"],

                  ["Q3. Who is known as the father of PHP?",
                   "a. Drek Kolkevi \nb. List Barely \nc. Rasmus Lerdrof \nd. None of the above", "c"],

                  ["Q4. Variable name in PHP starts with ?",
                   "a. ! (Exclamation) \nb. $ (Dollar) \nc. & (Ampersand) \nd. # (Hash)", "b"],

                  ["Q5. Which of the following is the default file extension of PHP?",
                   "a. .php \nb. .hphp \nc. .xml \nd. .html", "a"],

                  ["Q6. Which of the following is not a variable scope in PHP?",
                   "a. Extern \nb. Local \nc. Static \nd. Global", "a"],

                  ["Q7. Which of the following is correct to add a comment in php?",
                   "a. & …… & \nb. // …… \nc. /* …… */ \nd. Both (b) and (c)", "d"],

                  ["Q8. Which of the following is used to display the output in PHP?",
                   "a. echo \nb. write \nc. print \nd. Both (a) and (c)", "d"],

                  ["Q9. Which of the following is used for concatenation in PHP?",
                   "a. + (plus) \nb. * (Asterisk) \nc. . (dot) \nd. append()", "c"],

                  ["Q10. Which of the following starts with __ (double underscore) in PHP?",
                   "a. Inbuilt constants \nb. User-defined constants \nc. Magic constants \nd. Default constants", "c"],

                  ["Q11. Which of the following is the correct way to create a function in PHP?",
                   "a. Create myFunction() \nb. function myFunction() \nc.New_function myFunction()  \nd. None of the above", "b"],

                  ["Q12. Which of the following PHP function is used to generate unique id?",
                   "a. id() \nb. uniqueid() \nc. mdid() \nd. None of the above", "b"],

                  ["Q13. Which of the following function displays the information about PHP and its configuration?",
                   "a. phpinfo() \nb. php_info() \nc. info() \nd. None of the above", "a"],

                  ["Q14. Which of the following function is used to find files in PHP?",
                   "a. glob() \nb. fold() \nc. file() \nd. None of the above", "a"],

                  ["Q15. Which of the following function is used to get the ASCII value of a character in PHP?",
                   "a. val() \nb. asc() \nc. ascii() \nd. chr()", "d"],
                  ]
# Here list of PHP Quiz Questions end.

# Here list of python Quiz Questions Start.
py_Quiz_List = [['Q1. Which of the following is the correct extension of the Python file?',
                 "a. .python \nb. .py \nc. .htp \nd. .p", 'b'],

                ['Q2. Is Python case sensitive when dealing with identifiers?',
                 "a. no \nb. yes \nc. machine dependent \nd. none of the mentioned", 'b'],

                ['Q3. All keywords in Python are in _________?',
                 "a. Capitalized \nb. lower case \nc. UPPER CASE \nd. None of the mentioned", 'd'],

                ['Q4. 10. Which of the following character is used to give single-line comments in Python?',
                 "a. // \nb. # \nc. ! \nd. /*", 'b'],

                ['Q5. Which keyword is used for function in Python language?',
                 "a. Function \nb. def \nc. Fun \nd. Define", 'b'],

                ['Q6. Python supports the creation of anonymous functions at runtime, using a construct called __________?',
                 "a. pi \nb. anonymous \nc. lambda \nd. none of the mentioned", 'c'],

                ['Q7. What mean by x=10 and y=5 if 10 > 5 ?',
                 "a. x greaterthan y \nb. x lessthan y \nc. (a) and (b) both \nd. None of these  ", 'a'],

                ['Q8. The built-in function in Python is?',
                 "a. Seed() \nb. print() \nc. Sqrt() \nd. Factorial()", 'b'],

                ['Q9. Which of the following is not a keyword used in Python language?',
                 "a. Pass \nb. Eval \nc. Assert \nd. Nonlocal", 'b'],

                ['Q10. Amongst which of the following is / are the Numeric Types of Data Types?',
                 "a. int \nb. float \nc. complex \nd. All of the mentioned above", 'd'],

                ['Q11. list, tuple, and range are the ___ of Data Types?',
                 "a. Sequence Types \nb. Binary Types \nc. Boolean Types \nd. None of the mentioned above", 'a'],

                ['Q12. Binary data type is a fixed-width string of length bytes?',
                 "a. True \nb. False \nc. both a and b \nd. None of the mentioned above", 'a'],

                ['Q13. Amongst which of the following is / are the logical operators in Python?',
                 "a. and \n b. or \nc. not \nd. All of the mentioned above", 'd'],

                ['Q14. What is the name of the operator ** in Python?',
                 "a. Exponentiation \nb. Modulus \nc. Floor division \nd. None of the mentioned above", 'a'],

                ['Q15. Amongst which of the following is / are the conditional statement in Python code?',
                 "a. if (a => 200) \nb. if (a >= 10) \nc. if a<=100:  \nd. None of the mentioned above", 'c'],
                ]
# Here list of python Quiz Questions End.


if quizName == 1:
     select_Questions_op = int(input("Enter your Question between 1 to 15: "))
     quizlist = PHP_Quiz1_List
elif quizName == 2:
     quizlist = py_Quiz_List
     select_Questions_op = int(input("Enter your Question between 1 to 15: "))
else:
    print("Invalid option, Let's try again.")
    exit()


for i in range(select_Questions_op):
       # Whole list store in index variable, that will help to find needed index value in list.
          index = quizlist[i]
          print(index[0])  # Index of Question.
          print(index[1])  # Index of Answers.
          options_op = input("Select The right option:")
          # Answer is correct after Run this condition.
          # Index of correct answer in list if user enter correct than run if condition otherwise run else condition.
          if options_op == index[2]:
            print(" Correct")
            print("---------")
           # Answer is Wrong after Run this condition.
          else:
            print(" Wrong")
            print("--------")



