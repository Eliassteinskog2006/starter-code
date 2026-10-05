# To Do List

In today's lab, we will create a simple to do list. We will use multiple functions to segment our in class into sizable portions, with each function solving one specific problem.

## Instructions

1. Start by handling the user input in the main function. After the user is shown the menu, take in the numeric input by calling `num_input` with the prompt of `"Enter your choice: "`. Check what the user chose to do with conditional statements.
2. Once you have each condition checked for and each function initially called, begin implementing the code for each function. 
3. Begin by implementing the `print_list` function. This function takes in a list and prints out each item one after the other.
4. Next, implement the `add` function. This function takes in an item and adds that item to the list using the `append` function from the list.
5. Once the `add` function is complete, implement the `remove` function. This function takes in an item and deletes it from the list. This can be done using the list `remove` function or the `pop` function. However, if the list `remove` function is used, the item must be spelt correctly and match the item in the list perfectly. If the `pop` function is used, a search for the index must be done first to find the index. 
6. In order to find the index, the next step may be to implement the `index_of_item` function. This function takes the original list and the item to find. If the list contains the item, the index of the item should be returned. If the item is not in the list, return -1 as the index.
7. After completing the `index_of_item` function, move onto implementing the `update_item` function. This should take the list, the original item, and the new item. It should find the index of the original item and replace that value in the list. If the item is not in the list, it should print out an error message stating that the item is not in the list.
8. The `item_found_in_list` function is an optional function to write as it simply checks if the item is found in the list. This could be replaced with the `index_of_item` function, but this item can also be used to check if an item is in the list without having to go through all of the items.
9. If these are all done correctly, the main function should execute correctly, and you should have a functional to do list.
10. Once all of this is done, it may be good to include the `while` loop to ensure this program repeats itself until the user wants the program to quit.

## Hint 

1. Look at Lab 4 for how to setup the main function.

## Functions written for you

As you may have noticed, there are a couple of functions already written for you. These functions are: 

- `num_input`: As we've seen already, this function takes in a prompt, asks the user to input a number, and keeps asking the user to enter a number until the user successfully enters a number. 
- `menu`: This function prints out the menu of options for the user. It doesn't take in any input or return any value, nor does the user input any value in the function either. 

## Functions to implement 

These are the functions you must implement: 

- `print_list`: This function prints out all of the items in the list. 
- `add`: This functions takes in the list and a specific item, then adds the item to the list 
- `remove`: This function takes in the list and a specific item. It then removes the item from the list. If the item is not in the list, the program should inform the user that the item is not in the list and nothing should happen. 
- `item_found_in_list`: This function takes in the list itself and an item, then checks if the item is in the list. If the item is in the list, it should return `True`. If the item is not in the list, it should return `False`.
- `index_of_item`: This function should take in the list and an item, returning the index of where that item is found in the list. If the item is not in the list, this should return `-1`.
- `update_item`: This function should take in the list, the original item, and the new item. This function should get the index of the original item using the `index_of_item` function, then change the value of the item to the new item.
- `main`: This function is our main function. It gives the user what option they want to choose, then it should handle the user's input. Once the user chooses what they want, the main should execute that choice. Multiple inputs should happen here. The user should only be asked to input a value here in this main function and nowhere else (outside of the `num_input` function).

