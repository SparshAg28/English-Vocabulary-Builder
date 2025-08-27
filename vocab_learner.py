'''
Computer Science: Python Project
Made on: December 2024
English Vocabulary Builder
Author: Sparsh Agarwal
'''



#importing libraries
import nltk
from nltk.corpus import wordnet
import random
import time
import csv
import os



#Functions
def Start_User_Interface():
    menu='MENU \n\
1) Ask Meaning \n\
2) Get a random word\n\
3) Give synonym\n\
4) Give antonym\n\
5) Take revision test\n\
6) Show All the learned words\n\
7) Remove a learned word\n\
8) Remove all learned word\n\
9) Exit'
    print(menu)
    choice=input("Kindly enter your choice (1-9): ")
    print('\n')
    if choice=='1':
        Meaning()
    elif choice=='2':
        Randomword()
    elif choice=='3':
        Synonym()
    elif choice=='4':
        Antonym()
    elif choice=='5':
        revtest()
    elif choice=='6':
        Showall()
    elif choice=='7':
        remword()
    elif choice=='8':
        clearall()
    elif choice=='9':
        print("Exiting the program.")
        os._exit(0)
    else:
        print('INVALID CHOICE')
        print('Try AGAIN')
        print('\n\n')
        Start_User_Interface()
        

def Meaning():
    word=input('Kindly enter the word you want to know the meaning of: ')
    synsets = wordnet.synsets(word)
    if synsets:
        print('Meaning: ',synsets[0].definition())
        print('Part of Speech: ',posfetch(synsets[0].pos()))
        if synsets[0].examples():
            print('Examples:', synsets[0].examples())
        else:
            print('No examples found associated with the word "',word,'"',sep='')
        print('\n')
    
        ch=input('Want to save in database??(Y/N) \n')
        while ch not in ['Y','y','n','N']:
            print('INVALID CHOICE')
            print('Try AGAIN')
            ch=input('Want to save in database??(Y/N) \n')
        if ch=='Y' or ch=='y':
            F1=open('Database.csv','a+',newline='')
            F1.seek(0,0)
            state=0
            R_obj=csv.reader(F1)
            for i in R_obj:
                w=i[0]
                if w.lower()==word.lower():
                    state=1
                elif w.lower()!=word.lower():
                    state=0
                    
            if state==0:
                F1.seek(0,2)
                W_obj=csv.writer(F1)
                W_obj.writerow([word,0])
                print('Word Saved')
            elif state==1:
                print('Word is already saved in database')
            
            F1.close()
    else:
        print('Word not found')

         
    print('\n\n')
    Start_User_Interface()

        
def Randomword():
    try:
        from nltk.corpus import words
    except LookupError:
        nltk.download('words')
        from nltk.corpus import words

    word_list = words.words()
    random_word = random.choice(word_list)
    synsets = wordnet.synsets(random_word)
    if synsets:
        print("Random Word:", random_word)
        print('Meaning:', synsets[0].definition())
        print('Part of speech:', posfetch(synsets[0].pos()))
        if synsets[0].examples():
            print('Examples:', synsets[0].examples())
        else:
            print('No examples found associated with the word "',random_word,'"',sep='')
        print('\n')
    else:
        Randomword()

    ch=input('Want to save in database??(Y/N) \n')
    while ch not in ['Y','y','n','N']:
        print('INVALID CHOICE')
        print('Try AGAIN')
        ch=input('Want to save in database??(Y/N) \n')
    if ch=='Y' or ch=='y':
        F1=open('Database.csv','a+',newline='')
        F1.seek(0,0)
        state=0
        R_obj=csv.reader(F1)
        for i in R_obj:
            w=i[0]
            if w.lower()==random_word.lower():
                state=1
            elif w.lower()!=random_word.lower():
                state=0
                    
        if state==0:
            F1.seek(0,2)
            W_obj=csv.writer(F1)
            W_obj.writerow([random_word,0])
            print('Word Saved')
        elif state==1:
            print('Word is already saved in database')
            
        F1.close()

    print('\n\n')
    Start_User_Interface()

    
def posfetch(a):
    if a=='n':
        return 'Noun'
    elif a=='v':
        return 'Verb'
    elif a=='a':
        return 'Adjective'
    elif a=='r':
        return 'Adverb'
    elif a=='s':
        return 'Adjective Satellite'

    
def Showall():
    try:
        F1=open('Database.csv','r',newline='')
        R_obj=csv.reader(F1)

        if not any(F1):
            print('Database is EMPTY.')
            
        else:
            for w in R_obj:
                i=w[0]
                synsets = wordnet.synsets(i)
                if synsets:
                    print('word:', i)
                    print('Meaning:', synsets[0].definition())
                    print('Part of speech:', posfetch(synsets[0].pos()))
                    if synsets[0].examples():
                        print('Examples:', synsets[0].examples())
                    else:
                        print('No examples found associated with the word "',i,'"',sep='')
                    print('\n')
        F1.close()
    except FileNotFoundError:
        print('Database is EMPTY.')


    print('\n\n')
    Start_User_Interface()


def qsyn(word):
    synsets = wordnet.synsets(word)
    if synsets:
        synonyms = []
        for synset in wordnet.synsets(word):
            for lemma in synset.lemmas():
                synonyms.append(lemma.name())
        slst=[]
        for i in synonyms:
            if i!=word and i not in slst:
                slst=slst+[i]
        
    else:
        qdef()

    if synonyms:
        opt=[random.choice(synonyms),r]
        
        print('The synonym of',word,'is:')
        

def revtest():
    print('CAREFULLY READ THE FOLLOWING RULES FOR THE TEST: ')
    print('1) You will be given atmost 10 Multiple Choice Questions from the saved words in the database.\n\
2) For each question you will get 5 seconds to answer the question.\n\
3) Make sure you answer in capital letters, A,B,C,D only otherwise your response will not me recorded\n\
4) If the answer is not provided within the time limit the system will automatically move to the next question.\n\
5) Your score for each word will be recorded for future appearance in the revision test.\n\
6) Questions will on the basis of synonyms, antonyms and definitions will be given.\n\
7) Each correct response will get you 2 marks.\n\
8) Each incorrect response will make you LOSE 1 mark.\n\
9) No marks will be awarded for an unattemted question.\n\
10) Your score and mistakes will be shown at the end of the test.\n')
    print('Best of LUCK!! :-)')
    ch=input('Have you carefully read and understood all the rules and ready to take the test??(Y/N):\n')
    while ch not in ['Y','y','n','N']:
        print('INVALID CHOICE')
        print('Try AGAIN')
        ch=input('Have you carefully read and understood all the rules and ready to take the test??(Y/N):\n')

        
    if ch=='Y' or ch=='y':    
        with open('Database.csv', 'r', newline='') as F1:
            R_obj=csv.reader(F1)
            lst=[]
            for i in R_obj:
                lst+=[i]
            print(lst)
            sorted_lst = sorted(lst, key=lambda x: x[1])
            new_lst=sorted_lst[:min(10, len(sorted_lst))]

            score_lst=[]
            
            for i in new_lst:
                q_type=random.randint(1,3)
                
                if q_type==1:
                    score=qsyn(i[0])
                    score_lst+=score
                elif q_type==2:
                    score=qant(i[0])
                    score_lst+=score
                elif q_type==3:
                    score=qdef(i[0])
                    score_lst+=score
            marks=0
            incorrectq=[]
            unattemptedq=[]
            for i in score_lst:
                if i[1]==i[2]:
                    marks+=2
                elif i[2]==None:
                    unattemtedq+=[i]
                elif i[1]!=i[2]:
                    marks-=1
                    incorrectq+=[i]

            if score>=(1.5*(len(new_lst))):
                print('CONGRATULATIONS!!, You scored',marks,'marks','with',len(incorrectq),'incorrect questions and',len(unattemtedq),'unattemted questions')
            else:
                print('Your score is',marks,'marks','with',len(incorrectq),'incorrect questions and',len(unattemtedq),'unattemted questions')
            print('\n\n')
            
            if incorrectq:
                print('INCORRECT QUESTIONS:\n\n')
                for i in incorrectq:
                    print('Question:')
                    print(i[0])
                    print('Your answer: ', i[2])
                    print('Correct answer: ', i[1])
                    print('\n')
                print('\n\n')
            else:
                print('You have no incorrect questions')
                print('\n\n')

            if unattemtedq:
                print('UNATTEMTED QUESTIONS:\n\n')
                for i in unattemtedq:
                    print('Question:')
                    print(i[0])
                    print('Answer: ', i[1])
                    print('\n')
            else:
                print('You attemted all the questions')


            print('\n\n')
            Start_User_Interface()

    else:
        print('\n\n')
        Start_User_Interface()


def Synonym():
    word=input("Kindly enter the word which you need the synonym of:")
    synsets = wordnet.synsets(word)
    if synsets:
        synonyms = []
        for synset in wordnet.synsets(word):
            for lemma in synset.lemmas():
                synonyms.append(lemma.name())
        slst=[]
        for i in synonyms:
            if i!=word and i not in slst:
                slst=slst+[i]
        print('Synonyms: ', slst)    
    else:
        print('Word not found')
    
    print('\n\n')
    Start_User_Interface()

            
def Antonym():
    word=input("Kindly enter the word which you need the antonym of:")
    antonyms = []
    synsets = wordnet.synsets(word)
    if synsets:
        for synset in wordnet.synsets(word):
            for lemma in synset.lemmas():
                if lemma.antonyms():
                    antonyms.append(lemma.antonyms()[0].name())
        print('Antonyms:', antonyms)
    
    else:
        print('Word not found')
        
    print('\n\n')
    Start_User_Interface()


def remword():
    word=input('Kindly enter the word you need to be removed from the database: ')
    with open('Database.csv', 'r', newline='') as F1, open('Database_NEW.csv', 'w', newline='') as F2:
        R_obj = csv.reader(F1)
        W_obj = csv.writer(F2)
        state=0
        for w in R_obj:
            if w and w[0].lower() != word.lower():
                W_obj.writerow(w)
            elif w and w[0].lower()==word.lower():
                state=1

    os.remove('Database.csv')
    os.rename('Database_NEW.csv', 'Database.csv')
    if state==1:
        print('Word removed from database')
    elif state==0:
        print('"',word,'" was not found in the database.',sep='')


    print('\n\n')
    Start_User_Interface()


def clearall():
    i=input('Are you sure you want to CLEAR the database?? (Y/N) \n')
    while i not in ['Y','y','n','N']:
        print('INVALID CHOICE')
        print('Try AGAIN')
        i=input('Want to save in database??(Y/N) \n')
        
    if i=='Y' or i=='y':
        with open('Database.csv', 'w') as F1:
            print('Database Cleared')
            pass
            
    print('\n\n')
    Start_User_Interface()



#MAIN

print("\t\t\t\t\t Welcome to the Vocabulary Learner by Sparsh Agarwal")    
Start_User_Interface()

