import random

changer = False

target_list = []

reptiles = ['adder', 'alligator', 'anaconda', 'angonoka', 'anole', 'asp', 'basilisk', 'black caiman', 'black racer', 'boaconstrictor', 'box turtle', 'bull snake', 'caiman', 'cobra', 'collared lizard', 'copperhead', 'cottonmouth', 'crocodile', 'desert tortoise', 'frilled lizard', 'gaboon viper', 'garter snake', 'gavial', 'gecko', 'gila monster', 'glass lizard', 'gopher snake', 'green iguana', 'ground skink', 'horned lizard', 'iguana', 'indigo snake']

mammals = ['Bat', 'Bear', 'Beaver', 'Cat', 'Cow', 'Coyote', 'Deer', 'Dog', 'Dolphin', 'Elephant', 'Fox', 'Gibbon', 'Giraffe', 'Goat', 'Goat', 'Gopher', 'Hedgehog', 'Hippopotamus', 'Horse', 'Horse', 'Jaguar', 'Kangaroo', 'Koala', 'Leopard', 'Lion', 'Llama', 'Lynx', 'Mole', 'Monkey', 'Mouse', 'Narwhal', 'Orangutan', 'Orca', 'Otter', 'Ox', 'Panda', 'Pig', 'Polar bear', 'Puma', 'Rabbit', 'Raccoon', 'Rat', 'Rhinoceros', 'Sheep', 'Squirrel', 'Tiger', 'Walrus', 'Weasel', 'Wolf', 'Zebra']

colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple']

#random.shuffle(mammals)

if changer == True: 
    target_list.extend(mammals)
if changer == False: 
    target_list.extend(reptiles)    
    
print(target_list)    
    
list_length = len(target_list)
list_length_colors = len(colors)

questionLength = 5

rRightList = random.sample(target_list,questionLength)
rRightColors = random.sample(colors,questionLength)
rRightLogic = []
for i in range(0,questionLength):
    rRightLogic.append(True)

rWrongList = random.sample(target_list,1)
rWrongColors = random.sample(colors,1)
rWrongLogic = [False]

right_List = list(zip(rRightList,rRightColors,rRightLogic))
wrong_List = list(zip(rWrongList,rWrongColors,rWrongLogic))

answer_list = random.sample(right_List,3)
answer_list.append(wrong_List)
random.shuffle(answer_list)


print(right_List)
print(answer_list)


