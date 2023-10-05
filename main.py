#
ENGLISH_TO_MORSE = {'A': '.-',
                    'B': '-...',
                    'C': '-.-.',
                    'D': '-..',
                    'E': '.', 
                    'F': '..-.',
                    'G': '--.',
                    'H': '....',
                    'I': '..', 
                    'J': '.---',
                    'K': '-.-',
                    'L': '.-..',
                    'M': '--',
                    'N': '-.',
                    'O': '---',
                    'P': '.--.',
                    'Q': '--.-',
                    'R': '.-.',
                    'S': '...',
                    'T': '-',
                    'U': '..-',
                    'V': '...-',
                    'W': '.--',
                    'X': '-..-',
                    'Y': '-.--',
                    'Z': '--..',
                    ' ': '   ' ,
                   }



def morse_code():

    user_text=(input('Please Enter Your Text:   ').upper()) 
    try:
       morse_code=[ENGLISH_TO_MORSE[char] for char in user_text]     
    except  KeyError:
        print('Sorry , The syntax is unvalid to be translated! Enter Just Letters')
        

    else:
        for code in morse_code:
           print(code)


condition=True
while condition is True :
  
    morse_code()
    question=input('do you want to translate again?').upper()
    if question =='NO':
      condition=False