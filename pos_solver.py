###################################
# CS B551 Fall 2015, Assignment #5
#
# Your names and user ids:
#
# (Based on skeleton code by D. Crandall)
#
#
####
# Put your report here!!
####

import random
import math

# We've set up a suggested code structure, but feel free to change it. Just
# make sure your code still works with the label.py and pos_scorer.py code
# that we've supplied.
#
class Solver:

    # Calculate the log of the posterior probability of a given sentence
    #  with a given part-of-speech labeling
    def posterior(self, sentence, label):
        return 0

    # Do the training!
    #
    def train(self, data):
        global tag, word, probwgs,tags,words
        tag={}
        totaltag=0.0
        for i in data:
            for j in i[1]:
                totaltag+=1
                if j not in tag:
                    tag[j]=1
                else:
                    tag[j]+=1

        print tag
        print totaltag
        totalprobtag=0
        for key in tag:
            tag[key]=tag[key]/totaltag
            totalprobtag+=tag[key]
#        print tag

        print totalprobtag
        tags=tag.keys()
#        print tags

        word={}
        totalword=0.0
        for i in data:
            for j in i[0]:
                totalword+=1
                if j not in word:
                    word[j]=1
                else:
                    word[j]+=1

 #       print word
        print totalword
        totalprobword=0
        for key in word:
            word[key]=word[key]/totalword
            totalprobword+=word[key]
  #      print word

   #     print totalprobword
        words=word.keys()
    #    print words

        probwgs={}
        for i in words:
            for j in tags:
                probwgs[(i,j)] = 0.0;
     #   print probwgs

        for i in data:
            for j in i[0]:
                k=i[0].index(j)
                probwgs[(j,i[1][k])] += (1/(tag[i[1][k]]*totaltag));
      #  print probwgs

    # Functions for each algorithm.
    #
    def naive(self, sentence):
        global tag, word, probwgs,tags,words

        probsentence=[]
        for i in sentence:
            print i
            if i not in word:
                probsentence.append("noun")
            else:

                probtgw=[]


                for j in tags:
                    probtgw.append(probwgs[(i,j)]*tag[j]/word[i])
                maxprob=max(probtgw)
                maxprobindex=probtgw.index(maxprob)
                probsentence.append(tags[maxprobindex])
                print tags[maxprobindex]
                print probsentence
                print len(i),len(probsentence)
        return [ [probsentence], [] ]

    def mcmc(self, sentence, sample_count):
        return [ [ [ "noun" ] * len(sentence) ] * sample_count, [] ]

    def best(self, sentence):
        print  [ [ "noun" ] * len(sentence)]
        return [ [ [ "noun" ] * len(sentence)], [] ]

    def max_marginal(self, sentence):
        return [ [ [ "noun" ] * len(sentence)], [[0] * len(sentence),] ]

    def viterbi(self, sentence):
        return [ [ [ "noun" ] * len(sentence)], [] ]


    # This solve() method is called by label.py, so you should keep the interface the
    #  same, but you can change the code itself. 
    # It's supposed to return a list with two elements:
    #
    #  - The first element is a list of part-of-speech labelings of the sentence.
    #    Each of these is a list, one part of speech per word of the sentence.
    #    Most algorithms only return a single labeling per sentence, except for the
    #    mcmc sampler which is supposed to return 5.
    #
    #  - The second element is a list of probabilities, one per word. This is
    #    only needed for max_marginal() and is the marginal probabilities for each word.
    #
    def solve(self, algo, sentence):
        if algo == "Naive":
            return self.naive(sentence)
        elif algo == "Sampler":
            return self.mcmc(sentence, 5)
        elif algo == "Max marginal":
            return self.max_marginal(sentence)
        elif algo == "MAP":
            return self.viterbi(sentence)
        elif algo == "Best":
            return self.best(sentence)
        else:
            print "Unknown algo!"

