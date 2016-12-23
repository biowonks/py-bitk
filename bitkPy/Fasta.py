# -*- coding: utf-8 -*-

class Fasta:
    """ Class to handle fasta files """
    def __init__(self, input):
        self.file = input

    def stream(self, bufsize=4096):
        """ Method to stream fasta files """
        def chunk2seqObject(chunk):
            """ Includes header and sequence in SeqObject """
            lines = chunk.split('\n')
            header = lines[0]
            del lines[0]
            sequence = ''.join(lines)
            seqObject = {'h': header, 's': sequence}
            return seqObject

        filein = open(self.file, 'r')
        delimiter = '\n>'
        buf = ''
        justStarted = True
        while True:
            newbuf = filein.read(bufsize)
            if not newbuf:
                yield chunk2seqObject(buf)
                return
            buf += newbuf
            sequenceChunks = buf.split(delimiter)
            for chunk in sequenceChunks[0:-1]:
                if justStarted and chunk.startswith('>'):
                    chunk = chunk[1:]
                    justStarted = False
                yield chunk2seqObject(chunk)
            buf = sequenceChunks[-1]

    def makeDictionary(self):
        """ Class method to make dictionary out of streaming """
        myDict = {}
        for seqObject in self.stream():
            myDict[seqObject['h']] = seqObject['s']
        return myDict