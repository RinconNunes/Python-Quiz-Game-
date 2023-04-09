print ("Welcome to the greatest quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print ("Okay! Let's play:)")
score = 0 

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!') 
    score += 1
else:
    print("Incorrect!")
    
answer = input("what does AWS stand for? ")
if answer.lower() == "amazon web services":
    print('Correct!') 
    score += 1
else:
    print("Incorrect!")

answer = input("what does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!') 
    score += 1
else:
    print("Incorrect!")

answer = input("what does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!') 
    score += 1
else:
    print("Incorrect!")

print("you got " +  str(score)  +  " questions correct!")
print("you got " +  str((score / 4) *100) + "%.")


    