 
correctPassword="secret"
attemptsLefts=3
while attemptsLefts>0:
    userAttempts=input("ENTER PASSWORD:")
    if userAttempts == correctPassword:
        print("ACCESS GRANTED!")
        break
    else:
        attemptsLefts-=1 
        print(f"ACESS DENIED attemptsleft:{attemptsLefts}")
    if attemptsLefts == 0: 
        print("NO MORE ATTEMPTS")
        
 
