print('welcome! here are some questions about the capitals of countries and their names.')

def checkvalue(value,datalist): 
    if(value.casefold() in (input.casefold)):
        return True
    return False

United_Kingdom = input("1. What is the Capital of the UK? ")
France = input('2. What is the Capital of France? ')
Austria = input('3. what is the Capital of Austria? ')
Belgium = input('4. What is the Capital of Belgium? ')
Germany = input ('5. what is the Capital of Germany? ')
Italy = input('6. What is the Capital of Italy? ')
Ireland = input('7. WHat is the Capital od Ireland? ')
Finland = input('8. What is the Capital of Finland? ')
Belarus = input('9. What is the capital of Belarus? ')
Sweden = input('10. What is the Capital of Sweden? ')

if (United_Kingdom()== 'london'):
    print('Correct! The answer is london.')
else:
    print('Incorrect, the correct answer is London.')

if (France()== 'paris'):
    print('Correct! The answer is Paris.')
else:
    print('Incorrect, the correct answer is Paris.')

if (Austria()=='vienna'):
    print('Correct! The answer is Vienna.')
else: 
    print('Incorrect, the correct answer is Vienna')

if (Belgium()=='brussels'):
    print('Correct! The answer is Brussels.')
else:
    print('Incorrect, the correct answer is Brussels.')

if (Germany()=='berlin'):
    print('Correct! THe answer is Berlin.')
else: 
    print('Incorrect, the correct answer is Berlin.')

if (Italy()=='rome'):
    print('Correct! THe answer is Rome.')
else:
    print('Incorrect, The correct answer is Rome.')

if (Ireland()=='dublin'):
    print('Correct! The answer is Dublin.')
else:
    print('Incorrect, the correct answer is Dublin.')

if (Finland()=='helsinki'):
    print('Correct! The answer is Helsinki.')
else:
    print('Incorrect, the correct answer is Hesiniki.')

if (Belarus()=='minsk'):
    print('Correct! The answer is Minsk.')
else:
    print('Incorrect, the correct answer is Minsk. ')

if (Sweden()=='stockholm'):
    print('Correct! the answer is Stockholm.')
else: 
    print('Incorrect, the correct answer is Stockholm. ')

print('Thank you so much for answering the questions!')