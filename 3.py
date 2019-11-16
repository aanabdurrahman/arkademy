import string 

def cek_kata(text):
    res = sum([i.strip(string.punctuation).isalpha() for i in text.split()])
    j = text.split()
    con = len(j)
    print (str(res) + "/" + str(con))
    
cek_kata("2 pasang sandal hilang")
