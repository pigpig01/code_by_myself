def story():
    print("what's your name?")
    name = input()
    print(f"How are you {name}?")
    print("share anything interesting?(y/n)")
    answer = input()
    answers = ["y", "n"]
    while answer != answers[0] and answer != answers[1]:
        print("please write 'y' or 'n'")
        return story()
    if answer == answer[0]:
        print(f"{name},hello,can i make friends with you?😜")
    elif answer == answer[1]:
        print("oh man😂")
story()
    
   
        
