#!/usr/bin/env python
# coding: utf-8

# In[14]:


import re
with open("Inverted_Index/Corpus.txt","r+") as a:#importing the corpus
    corpus=a.read()
with open("Inverted_Index/Stopwords.txt","r+") as b: #importing stopwords
    stopwords=b.read()


# In[15]:


def doc_ID(txt):
    if re.search("^Document.*\d$",txt): 
        return True
def number_check(txt):
    if re.search("\d",txt):
        return True
    else:
        return False

# In[16]:


doc_id=0
indexer=[]
for i in corpus.split(" "):
        if doc_ID(i):
            doc_id+=1             
        elif i in stopwords:
            pass
        elif i==" ":
            pass
        elif number_check(i):
            pass
        else:            
#           indexer.append([i,doc_id])
#           append(indexer,[i,doc_id])
#           print(doc_id)
#           print(i)
            indexer.append([i,doc_id])
            
# print(indexer)    
indexer_dict={key: value for (key,value) in indexer} #changing a list into a dictionary
# print(index_dict) #in this part we print out the token sequence
for i in sorted(indexer_dict):
    print([i,indexer_dict[i]])#in this part we print out the sorted token sequence


# In[18]:


x=str(input("please enter what youre looking for... "))
def search(x):
    word_freq=0
    docs=[]
    output=[]
    check=False
    for k,v in indexer_dict.items():
        if x==k:
            check=True
            docs.append(v)
            word_freq=word_freq+1
    #         print(docs)
    if check==True:
    #     print(x)
    #     print(docs)
    #     print(word_freq)
        output.append(x)
        output.append(word_freq)
        for i in docs:
            output.append(i)
        print(output)
    else:
        print("no match !!!")
for i in x.split(" "):
    search(i)


# In[ ]:




