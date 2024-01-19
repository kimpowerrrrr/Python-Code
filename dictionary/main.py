dictionary = {
    "Bug" : "An error in a program that prevents the program from running as expected.",
    "Function" : "A piece of code that you can easily call over and over again.",
    "Loop" : "The action of doing something over and over again"
}

#Adding new items to the dictionary
dictionary["Parameters"] = "A parameter is a special kind of variable used in a function or method to refer to one of the pieces of data provided as input to the function."

#empty dictionary
#dictionary = {}

#edit item in dictionary
dictionary["Bug"] = "A lady bug."

#Looping in dictionary
for key in dictionary:
    print(f"{key} : {dictionary[key]}")