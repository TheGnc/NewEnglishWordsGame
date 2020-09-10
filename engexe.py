import random

file_words=open("EnglishWords1.txt", "r")
words_list=file_words.readlines()
file_words.close()
words_array=[[],[]]
for words in words_list:
    splitted_words=words.split("-")
    a=0
    for next_word in splitted_words:
        if a%2==0:
            words_array[0].append(next_word.strip("\n"))
            a+=1
        else:
            words_array[1].append(next_word.strip("\n"))
        
words_amount=len(words_array[0])
while True:
    random_word_num=random.randint(0,words_amount-1)
    print(words_array[0][random_word_num], "?")
    answer=input("Answer:")
    if answer=="":
        break
    elif answer.title()==words_array[1][random_word_num]:
        continue
    else:
        for i in range(2):
            answer=input("Wrong answer, try again.\nAnswer:")
            if answer.title()==words_array[1][random_word_num]:
                break
        print(words_array[1][random_word_num])