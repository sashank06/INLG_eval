#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math
import re
import numpy as np
import pickle
import nlp
from scipy.spatial import distance
from random import randint
import torch
from InferSent.models import InferSent

model_version = 2 # Choose 1 if you want to use glove


MODEL_PATH = "InferSent/dataset/fastText/infersent%s.pkl" % model_version
params_model = {'bsize': 64, 'word_emb_dim': 300, 'enc_lstm_dim': 2048,
                'pool_type': 'max', 'dpout_model': 0.0, 'version': model_version}
model = InferSent(params_model)
model.load_state_dict(torch.load(MODEL_PATH))


# Keep it on CPU or put it on GPU
use_cuda = False
model = model.cuda() if use_cuda else model


# If infersent1 -> use GloVe embeddings. If infersent2 -> use InferSent embeddings.
W2V_PATH = '../dataset/GloVe/glove.840B.300d.txt' if model_version == 1 else 'InferSent/dataset/fastText/crawl-300d-2M-subword.vec'
model.set_w2v_path(W2V_PATH)

model.build_vocab_k_words(K=100000)

def read_dull_responses(filename):
    with open(filename,"r") as f:
        dr = f.read().splitlines() 
    return dr
_dull_responses = read_dull_responses("/home/ssantha1/Eval/THRED/Eval_scripts/dull_responses.txt")


def _calc_similarity(_boost_factor, response, v_response, v_ref):
    if _boost_factor:
        # number of non-stop words
        ns = len(nlp.omit_stopwords(response.split()))
        # number of words not in dull response pattern
        m = len(nlp.omit_stopwords(_find_interesting_segments(response,_dull_responses)))
        coef = 1.0 + math.log10((2.0 + m) / (2.0 + ns))
    else:
        coef = 1.0
        return distance.cosine(model.encode([v_ref]), model.encode([v_response]))
    return (distance.cosine(model.encode([v_ref]), model.encode([v_response]))) * coef



def _find_interesting_segments(response, dull_responses):
    matched_segment = []

    has_matched = False
    for dr in dull_responses:
        matched = re.match(dr, response)
        if not matched:
            continue

        has_matched = True
        segment = [w for g in matched.groups() for w in g.split()]
        if len(segment) < len(matched_segment) or not matched_segment:
            matched_segment = segment

    return matched_segment if has_matched else response.split()


def produce_similarity(type_,_boost_factor,context,source,target):
    assert len(context) == len(source) == len(target)
    print("Total number of similarity measures to be calculated: {}".format(len(context)))
    SS =[]
        
    if type_ == "full":
        print("Calculating full similarity")
        for i in range(len(context)):
            SS.append(_calc_similarity(_boost_factor,target[i],target[i],context[i] + source[i]))
            if i % 1000 == 0:
                print(i)
        return SS
    elif type_ == "recent":
        print("Calculating recent utterance similarity")
        for i in range(len(context)):
            SS.append(_calc_similarity(_boost_factor,target[i],target[i],source[i]))
            if i % 1000 == 0:
                print(i)
        return SS
    else:
        return "Please provide either full or recent as the type and try again."




