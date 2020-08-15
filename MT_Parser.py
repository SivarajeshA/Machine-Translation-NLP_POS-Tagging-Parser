ART = ["a", "an", "the"]
N = ["boy","telescope","football","jam","book","saw","play"]
PRON = ["i","we","you","they"]
V = ["saw","play","eat","study","jam"]
P = ["with","for"]

indx = [0]
res_parsing = ["",""]

def NP(s,pp): 
    length = len(s)
    if(length == 0): 
        return 1
    np = "( NP "
    if(s[indx[0]].casefold() in N):
        np += "( N \""+s[indx[0]]+"\" ))"
        return np
    elif(s[indx[0]].casefold() in PRON):
        np += "( PRON \""+s[indx[0]]+"\" ))"
        return np
    elif(s[indx[0]].casefold() in ART):
        indx[0] += 1
        if(length > indx[0]):
            if(s[indx[0]].casefold() in N):
                np += "( ART \""+s[indx[0]-1]+"\" )"
                np += "( N \""+s[indx[0]]+"\" )"
            else:
                return 1
            if(pp and ("with" in s or "for" in s)):
                indx[0] += 1
                if(length > indx[0]):
                    if(s[indx[0]].casefold() in P):
                        np += "( PP (P \""+s[indx[0]]+"\" ) "
                        indx[0] += 1
                        t = NP(s,pp)
                        if(t != 1):
                            np += t+")"  # PP ending
                        else:
                            return 1
                    else:
                        return 1
            return np+")" # NP ending
        else:
            return 1
    else:
        return 1
    
def VP(s):
    length = len(s)
    res_parsing[0] = 1
    if(length == 0):        
        return res_parsing    
    vp = "( VP "  
    if(s[indx[0]].casefold() in V):
        vp += "( V \""+s[indx[0]]+"\" )"
        parse_bkp = vp
    else:
        return res_parsing 
    if("with" in s or "for" in s): #PP 2 parsing case
        indx[0] += 1
        pos_t = indx[0] # Backup position to handle PP in VP
        t = NP(s,1)#Process pp in NP
        if(t == 1):            
            return res_parsing
        vp += t +")" # VP Ending
        
        indx[0] = pos_t
        t = NP(s,0)#Don't process pp in NP
        if(t == 1):            
            return res_parsing
            
        vp2 = parse_bkp + t
        indx[0] += 1
        if(s[indx[0]].casefold() in P): # Process pp in VP
            vp2 +="( PP (P \""+s[indx[0]]+"\" ) "
            indx[0] += 1
            if((s.count("with") + s.count("for")) > 1):#more than 1 with/for
                t = NP(s,1)                
            else:
                t = NP(s,0)                
            if(t != 1):
                vp2 += t+")" # PP ending
                vp2 += ")" # VP ending
                res_parsing[0] = vp # Handled in NP
                res_parsing[1] = vp2 # Handled in VP
                return res_parsing
            else:
                return res_parsing
        else:
            return res_parsing
        
    indx[0] += 1 # Flow comes here only when PP is not in sentence
    t = NP(s,1)
    if(t == 1):            
        return res_parsing        
    res_parsing[0] = parse_bkp+ t+")" # VP ending
    return res_parsing
    

file_read = open("input.txt","r") 
file_write = open("output.txt","w") 

lines = file_read.readlines()
for i in lines: 
    indx[0] = 0
    strWords = i.replace("\n","").split(' ')   
    res_NP = NP(strWords,1)
    #print("NP: ",res_NP)
    if( res_NP == 1 ):
        file_write.write("Not Parsable\n")
    else:
        strWords = strWords[(1 + indx[0]):] # To remove NP parsed words
        indx[0] = 0
        res_VP = VP(strWords)        
        #print("VP: ",res_VP)
        if( res_VP[0] == 1):
            file_write.write("Not Parsable\n")
        elif("with" in strWords or "for" in strWords):
            file_write.write("( S "+ res_NP + res_VP[0] +")\n")
            file_write.write("( S "+ res_NP + res_VP[1] +")\n")   
        else:
            file_write.write("( S "+ res_NP + res_VP[0] +")\n")
            
file_read.close() 
file_write.close()
print("Parsing Completed, check output.txt")
