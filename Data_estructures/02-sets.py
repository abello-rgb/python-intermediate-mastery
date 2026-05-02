"""


set1 = { 1,2,3,4}
set2 = { 3,4,5,6}

# Union of sets

union_result = set1.union(set2)

# Intersetion of sets

intersetion_result = set1.intersection(set2)

# Difference of sets

difference_result = set1.difference(set2)



print(union_result)
print(intersetion_result)
print(difference_result)

my_set = {1,2,3}


# add element to set
my_set.add(4)
print(my_set)

# remove element to set

my_set.remove(2)
print(my_set)



"""


my_fruits = {
    '🍎 apple',
    '🍌 banana',
    '🍊 orange'
}

friend_fruits = { '🍎 apple','🍇 grapes', '🍍 pineapple', '🥝 kiwi'}

combined_list = my_fruits.union(friend_fruits)
print(f'Combined list: {combined_list}')

intersection_set = my_fruits.intersection(friend_fruits)
print(f'Intersection: {intersection_set}')

my_different_fruit = my_fruits.difference(friend_fruits)
print(f'My Difference fruits: {my_different_fruit}')

your_different_fruit = friend_fruits.difference(my_fruits)
print(f'Your Difference fruits: {your_different_fruit}')