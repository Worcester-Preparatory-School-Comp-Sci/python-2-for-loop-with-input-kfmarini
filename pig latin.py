#Kathryn Marini 2/27/19
def pigLatin():
    word = input('What would you like to say in pig latin?')
    vowelList = ['a','e','i','o','u']
    if( word[0:1] in vowelList):
        newWord = word[0:] + 'yay'
    else:
        newWord = word[1:] + word[0] +'ay'
    print(newWord)

pigLatin()   # remember to call your code
