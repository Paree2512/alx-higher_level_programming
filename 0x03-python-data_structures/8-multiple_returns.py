#!/usr/bin/python3

def multiple_returns(sentence):
    s_length = len(sentence)
    if s_length == 0:
        return (0, None)
    else:
        present = (s_length, sentence[0])
        return present
