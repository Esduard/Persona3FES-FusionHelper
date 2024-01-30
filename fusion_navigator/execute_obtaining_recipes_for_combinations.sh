#!/bin/bash

# Loop from 0 to 12
for i in {0..12}
do
    # Execute the script with the current value of i as an argument
    /bin/python3 obtaining_recipes_for_combinations.py $i
done