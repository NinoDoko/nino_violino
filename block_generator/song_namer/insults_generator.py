import sys, random, os

insults_dir = os.path.dirname(os.path.realpath(__file__))
print insults_dir

def main(no_insults):
    nouns = []
    all_words = ''
    
    with open(insults_dir + '/mobyposi.i') as f: 
        all_words = f.read()
    
    all_words = [x.split('|') for x in all_words.replace('\xd7','|').split('\r') if x]
    nouns = [x[0] for x in all_words if x[1] == 'N']
    gerunds = [x[0] for x in all_words if x[0][-3:] == 'ing' and x[1] != 'N']

    for i in range(no_insults):
        print 'You ' + random.choice(gerunds) + ' ' + random.choice(nouns) + '-' + random.choice(nouns)

if __name__ == '__main__' : 
    no_insults = 1
    if len(sys.argv) > 1: 
        no_insults = int(sys.argv[1])
    main(no_insults)
