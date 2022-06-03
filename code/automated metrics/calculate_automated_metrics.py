#!/usr/bin/env python
# coding: utf-8
import ftfy
import textstat
import readability
import pandas as pd
import semantic_similarity

def read_shortlist(filename):
    with open(filename,"r") as f:
        lines = f.read().splitlines() 
    return lines
shorts = read_shortlist("Final Shortlist.txt")
shorts = list(filter(None, shorts)) # fastest

def prepare_file(shorts):
    final_group = []
    for i in range(0,len(shorts),8):
        final_group.append([shorts[j] for j in range(i,i+7)])
    return final_group       

final_group = prepare_file(shorts)


standard = []
seq2seq = []
hred =[]
thred = []
context = []
source = []
for group in final_group:
    context.append(str(group[1].split(":")[1].strip()))
    source.append(str(group[2].split(":")[1].strip()))   
    standard.append(str(group[3].split(":")[1].strip()))
    seq2seq.append(str(group[4].split(":")[1].strip()))
    hred.append(str(group[5].split(":")[1].strip()))
    thred.append(str(group[6].split(":")[1].strip()))

standard_readability = readability.calculate_readability(standard,"fre")
seq2seq_readability = readability.calculate_readability(seq2seq,"fre")
hred_readability = readability.calculate_readability(hred,"fre")
thred_readability = readability.calculate_readability(thred,"fre")


new_group = []
max_batch = []
min_batch = []
mean_batch = []
median_batch = []
std_batch = []
for i in range(len(standard_readability)):
    max_batch.append(max([standard_readability[i],seq2seq_readability[i],hred_readability[i],thred_readability[i]]))
    min_batch.append(min([standard_readability[i],seq2seq_readability[i],hred_readability[i],thred_readability[i]]))
    mean_batch.append(st.mean([standard_readability[i],seq2seq_readability[i],hred_readability[i],thred_readability[i]]))
    median_batch.append(st.median([standard_readability[i],seq2seq_readability[i],hred_readability[i],thred_readability[i]]))
    std_batch.append(st.stdev([standard_readability[i],seq2seq_readability[i],hred_readability[i],thred_readability[i]]))
    

# Semantic Similarity

standard_coherence = semantic_similarity.produce_similarity("full",True,context,source,standard)

seq2seq_coherence = semantic_similarity.produce_similarity("full",True,context,source,seq2seq)

hred_coherence = semantic_similarity.produce_similarity("full",True,context,source,hred)

thred_coherence = semantic_similarity.produce_similarity("full",True,context,source,thred)


df = pd.DataFrame(index=range(len(standard)))

df["standard"] = pd.DataFrame(standard)
df["standard_R"] = pd.DataFrame(standard_readability)
df["standard_C"] = pd.DataFrame(standard_coherence)
df["seq2seq"] = pd.DataFrame(seq2seq)
df["seq2seq_R"] = pd.DataFrame(seq2seq_readability)
df["seq2seq_C"] = pd.DataFrame(seq2seq_coherence)
df["hred"] = pd.DataFrame(hred)
df["hred_R"] = pd.DataFrame(hred_readability)
df["hred_C"] = pd.DataFrame(hred_coherence)
df["thred"] = pd.DataFrame(thred)
df["thred_R"] = pd.DataFrame(thred_readability)
df["thred_C"] = pd.DataFrame(thred_coherence)


df.to_excel("final_shortlist_scores.xlsx",index=False)





