import random

# print(help(random))

def lottery_gen():
    
    random_number = random.sample(range(0,50), k=1)
    username = input("please input your name: ")
    ticket_number = (int(input("Please enter your number: ")))
    lucky_number = 30
    print (username)
    
    if ticket_number > 50
        print("syntax error, ticket number must be within the range of 0-50")
        enter = input()
        
    elif random_number == lucky_number and lucky_number == ticket_number:
        print('Congratulations' + username + "You choosed the lucky Number")
        
       
    else:
        print ("sorry, your Raffle Number: ", random_number,  "does not match the lucky number. Try again")


lottery_gen()
