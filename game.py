import random_word_generator


def change_current_word(selected_index,current_word,character):
    modified_word=""
    for i in range(len(selected_index)):
        if current_word[i]=="_" and selected_index[i]==character:
            modified_word+=character
        else:
            modified_word+=current_word[i]
    return modified_word        





def input_char_in_word(selected_index,input_char,current_word,attempts_remaining):
    if input_char in selected_index:
        current_word=change_current_word(selected_index,current_word,input_char)
    else:
        attempts_remaining-=1
    
    return current_word,attempts_remaining   





def print_current_status(current_word , attempts_remaining):
     print("Current State:" ,end=" ")
     for i in current_word:
         print(i,end=" ")
     print("\tAttempts Remaining: {}".format(attempts_remaining))





def check_game_status(selected_index,current_word,attempts_remaining):
    if current_word==selected_index:
        print("Congrats!!! You WON :D")
        return True
    if attempts_remaining<=0 :
        print("Whoops!!! You Lost Try Again")
        print("Word was : {}".format(selected_index))    
        return True
    return False    

    
def startgame(attempts=5):
    selected_index = random_word_generator.pick_random_word()
    current_word=""
    for i in range(len(selected_index)):
        if(selected_index[i]=='a' or selected_index[i]=='e' or selected_index[i]=='i' or selected_index[i]=='o' or selected_index[i]=='u'):
            current_word+= selected_index[i]
        else:
            current_word+="_"
    attempts_remaining = attempts    
    print_current_status(current_word , attempts) 
    while True:
        input_char = input("Guess The Character: ")
        print("")
        current_word,attempts_remaining = input_char_in_word(selected_index,input_char,current_word,attempts_remaining)
        print_current_status(current_word , attempts_remaining)
        game_ended = check_game_status(selected_index,current_word,attempts_remaining)
        if game_ended:
            break
if __name__=="__main__":
    startgame()
        


    