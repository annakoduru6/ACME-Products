# ACME-Products
The intent for this school assignment was to test my coding skills and demonstrate competency in writing my own Python modules, object-oriented programming, code style, and testing. I was given instructions to create an ACME inventory and was able to choose any tools and references I needed to complete the assignment. 
This was a "mock" situation as an employee of Acme Corporation looking for ways to better organize the vast quantities and variety of goods the company manages and sells:

PART ONE INSTRUCTIONS:
Everything Acme sells is considered a "Product", and must have the following attributes (variables that live "inside" the class):

 -name (string with no default)
 -price (integer with default value 10)
 -weight (integer with default value 20)
 -flammability (float with default value 0.5)
 -identifier (integer – a randomly generated number from a uniform distribution ranging from 1000000 to 9999999.)

I wrote a Python class to model the above data, precise in field names and types. My class also had an _init_ constructor
method. This all was tested in a Python REPL and saved in the acme.py file.

PART TWO INSTRUCTIONS:
Create methods in your class as follows:
-stealability(self) - calculates the price divided by the weight, and then returns a message:
 if the ratio is less than 0.5 return "Not so stealable..."
 if it is greater or equal to 0.5 but less than 1.0 return "Kinda stealable."
 otherwise return "Very stealable!"
-explode(self) - calculates the flammability times the weight, and then returns a message:
 if the product (result of the multiplication operation) is less than 10 return "...fizzle."
 if it is greater or equal to 10 but less than 50 return "...boom!"
 and otherwise return "...BABOOM!!"

PART THREE INSTRUCTIONS:
Make a child class called BoxingGlove that inherits from Product named BoxingGlove and does the following:

Change the default weight to 10 (but leave other defaults unchanged)
Override the explode method to always return "...it's a glove."
Add a punch method that returns:
"That tickles." if the weight is below 5
"Hey that hurt!" if the weight is greater or equal to 5 but less than 15
"OUCH!" otherwise

PART FOUR INSTRUCTIONS:
Use the Product and BoxingGlove classes to write an acme_report.py module to generate random products and print a summary of them. For the purposes of these functions we will only use the Product class.
Your module should include two functions:

-generate_products(num_products=30) should randomly generate a given number of products (default 30), and return them as a list
-inventory_report(product_list) takes a list of products, and returns a tuple that holds some basic statistics about the list of products

For the purposes of generation, "random" means uniform - all possible values should vary uniformly (have the same likelihood of being chosen) across the following possibilities:

-name should consist of a random adjective from the list: ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved'] followed by a space and then a random noun from the list: ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???'], e.g. 'Awesome Anvil' and 'Portable Catapult' are both potential names that could be generated
-price and weight should both be random integers from 5 to 100 (inclusive)
-flammability should be a float ranging from 0.0 to 2.5 (inclusive)

I used the random module from the Python standard library and also imported my Product class from the acme.py file. After generating a set of random values, I then passed those values as parameters to the Product() class constructor function. This function returns back a new product object that you can append to a list, reiterating with a for loop as many times as required. For the inventory_report(), I calculated the following values in regards to the product list generated by my generate_products() function:

-Number of unique product names in the product list
-Average (mean) price
-Average (mean) weight
-Average (mean) flammability

Finally, I created an acme_test.py file to assert that everything works as it should. The functions test the following about the Product class:
-Test the product's default attributes (see the example code)
-Test the stealability() and explode() methods to ensure that they return the correct values
-Test the default generate_products() function to ensure that it returns a list with 30 items in it
