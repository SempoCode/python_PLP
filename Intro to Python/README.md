# All About Python Variables 🧠💡


In programming, a variable is a container (storage area) to hold data. For example,

        number = 10

Here, the number is the variable storing the value 10.

## Assigning values to Variables in Python



As we can see from the above example, we use the assignment operator = to assign a value to a variable.

        site_name = "Power Learn Project"
        print(site_name)



In the above example, we assigned the value ``‘Power Learn Project’`` to the site_name variable. Then, we printed out the value assigned to ``site_name``.



**Note:** Python is a type-inferred language, so you don't have to explicitly define the variable type. It automatically knows that Power Learn Projects is a string and declares the site_name variable as a string.



### Changing the Value of a Variable in Python
        site_name = "Power Learn Project"
        print(site_name)

        #Assigning new value to site_name
        site_name = "I love coding 😊"
        print(site_name)

        # The output will be
        Power Learn Project
        I love coding 😊



Here, the value of site_name is changed from ‘Power Learn Project’ to 'I love coding 😊'.

### Example: Assigning multiple values to multiple variables



        a,b,c = 5, 7, "Hello world"
        print(a) # prints 5
        print(b) # prints 5
        print(c) # prints Hello World



## Rules for Naming Python Variables
 - Constant and variable names should have a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore (_). For example:



 - snake_case
 - MACRO_CASE
 - camelCase
 - CapsWords



 - Python is case-sensitive. So num and Num are different variables. For example,
        num = 55
        Num = 510
        print(num) #5
        print(Num) #510



 - Avoid using keywords like if, True, class, etc. as variable names.

More Resources:

   1. <https://realpython.com/python-variables/>
   2. <https://www.simplilearn.com/tutorials/python-tutorial/python-variables>
   3. <https://www.guru99.com/variables-in-python.html>
   4. <https://www.tutorialspoint.com/python/python_variables.htm>
