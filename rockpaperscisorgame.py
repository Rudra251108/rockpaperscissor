import random

computer=random.choice([-1,0,1])
print("""
                         ""Choose Any One""
Stone
paper
Scissor
      
      
""")
your_choice=input("Enter your choice:")
yourdict={"stone":1,"paper":0,"scissor":-1}
reverse_dict={1:"stone",0:"paper",-1:"scissor"}
you=yourdict[your_choice]

print(f"Computer choose {reverse_dict[computer]} and you choose {reverse_dict[you]}")

if(computer==you):
    print("Game is Draw")

else:
    if(computer==1 and you==0):
        print("You Win!")
    elif(computer==1 and you==-1):
        print("You lose!")
    elif(computer==0 and you==1):
        print("You Lose!")
    elif(computer==0 and you==-1):
        print("You Win!")
    elif(computer==-1 and you==1):
        print("You Win!")
    elif(computer==-1 and you==0):
        print("You lose!")
    else:
        print("""   Something went wrong
                    Check your choice""")