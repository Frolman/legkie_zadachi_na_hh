#Заданы 3 стороны прямоугольника в строку через пробел, нужно определить является ли он прямоугольным
def has_prymougol(text:str)->bool:
    new_text=''
    text=text+' '
    i=0
    storona=[0,0,0]
    a=0
    while i<len (text):
        if text [i] == ' ':    
            storona[a] = int(new_text)
            new_text=''
            a+=1
        else:
            new_text=new_text+text[i]
        i+=1
    return (storona[0] ** 2 + storona[1] ** 2) == storona[2] ** 2
text = "3 4 5"
print (has_prymougol(text))
    
        

         


