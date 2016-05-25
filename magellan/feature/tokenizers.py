# coding=utf-8
import pandas as pd

import magellan.externals.py_stringmatching.tokenizers as tok
from magellan.utils.generic_helper import remove_non_ascii

_global_tokenizers = pd.DataFrame({'function_name': ['tok_qgram', 'tok_delim', 'tok_wspce'],
                                   'short_name': ['qgm', 'dlm', 'wsp']})


# Get a list of tokenizers that can be called with just input string as the argument

def get_tokenizers_for_blocking(q=[2, 3], dlm_char=[' ']):
    return get_single_arg_tokenizers(q, dlm_char)


def get_tokenizers_for_matching(q=[2, 3], dlm_char=[' ']):
    return get_single_arg_tokenizers(q, dlm_char)


def get_single_arg_tokenizers(q=[2, 3], dlm_char=[' ']):
    # return function specific to given q and dlm_char
    qgm_fn_list = [make_tok_qgram(k) for k in q]
    dlm_fn_list = [make_tok_delim(k) for k in dlm_char]

    qgm_names = ['qgm_' + str(x) for x in q]
    dlm_names = ['dlm_dc' + str(i) for i in range(len(dlm_char))]
    names = []
    names.extend(qgm_names)
    names.extend(dlm_names)

    fns = []
    fns.extend(qgm_fn_list)
    fns.extend(dlm_fn_list)

    return dict(zip(names, fns))


# return a delimiter-based tokenizer with a fixed delimiter
def make_tok_delim(d):
    def tok_delim(s):
        # check if the input is of type base string
        if pd.isnull(s):
            return s
        s = remove_non_ascii(s)
        return s.split(d)

    return tok_delim


# return a qgram-based tokenizer with a fixed q
def make_tok_qgram(q):
    def tok_qgram(s):
        # check if the input is of type base string
        if pd.isnull(s):
            return s
        return tok.qgram(s, q)

    return tok_qgram


# q-gram tokenizer
def tok_qgram(s, q):
    if pd.isnull(s):
        return s
    return tok.qgram(s, q)


def tok_delim(s, d):
    if pd.isnull(s):
        return s
    tok.delimiter(s, d)
