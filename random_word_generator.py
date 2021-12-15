import random
def pick_random_word():
     avengers=["Thor","Spider Man","Iron Man","Captain America","Bucky","Falcon","Hawkeye","Black Widow","Black Panther","Hulk","Ant Man","Vision","Wanda"]
     selected_word = random.randint(0,len(avengers)-1)
     return avengers[selected_word]