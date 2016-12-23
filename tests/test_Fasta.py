# -*- coding: utf-8 -*-

"""
test_bitkPy
----------------------------------

Tests for `bitkPy` module.
"""

import os

from bitkPy.Fasta import Fasta

myPath = os.getcwd()
dataPath = myPath + '/sampledata/'

def test_Fasta():
    sampleFile = dataPath + 'fasta.with.bitk.tags.fa'
    myDict = Fasta(sampleFile).makeDictionary()
    assert myDict == {
        'Org1|locus1|Acce1|B|C|D':'AAAAAAAAAAAAAKKKKKKKKKKKKKKKA',
        'Org2|locus2|Acce2|B|C|D':'AAAAAAAAAAAAAKKKKKKKKKKKKKKKK',
        'Org3|locus3|Acce3|A|C|D':'AAAAAAAAAAAAAKKKKKKKKKKKKKKKK',
        'Org4|locus4|Acce4|A|C|E':'AAAAAAAAAAAAAKKKKKKKKKKKKKKKK'
    }
    return None

def test_Fasta_smallChunks():
    sampleFile = dataPath + 'fasta.with.bitk.tags.fa'
    myDict = {}
    for seqObject in Fasta(sampleFile).stream(bufsize=3):
         myDict[seqObject['h']] = seqObject['s']
    assert myDict == {
        'Org1|locus1|Acce1|B|C|D':'AAAAAAAAAAAAAKKKKKKKKKKKKKKKA',
        'Org2|locus2|Acce2|B|C|D':'AAAAAAAAAAAAAKKKKKKKKKKKKKKKK',
        'Org3|locus3|Acce3|A|C|D':'AAAAAAAAAAAAAKKKKKKKKKKKKKKKK',
        'Org4|locus4|Acce4|A|C|E':'AAAAAAAAAAAAAKKKKKKKKKKKKKKKK'
    }
    return None