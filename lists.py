if __name__ == '__main__':
      e=  int(input())
      ls= list(input())
      c=len(ls)
      for i in ls[e]:
            if(ls[0]=="insert"):
                 print(ls.insert(i,e))
            elif(ls[0]=="print"):
                print(ls[i])
            elif(ls[0]=="remove"):
                print(ls.remove(e))     
            elif(ls[0]=="append"):
                print(ls.append(e)) 
            elif(ls[0]=="sort"):
                print(ls.sort())
            elif(ls[0]=="pop"):
                if(i==c-1):
                     print(ls.pop(i)) 
            if(ls[0]=="reverse"):
                print(ls.reverse()) 