# write your code here
favorite_animals = ['dog', 'cat', 'monkey', 'rabbit']
print(favorite_animals)

favorite_animals.remove('monkey')
favorite_animals.pop(2)
favorite_animals.append('hores')
print(favorite_animals)

for x in favorite_animals:
    print(f"love {x}")

numbers=[1,2,3,4,5]    
numbers_sum=0
for number in numbers:
    numbers_sum += number
print(numbers_sum)