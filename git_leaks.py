#! user/bin/python3
# cada comit es un diccionario
from git import Repo
import re,time,sys,signal

DIR = './skale/skale-manager'

def salida_controlada(signal, frame):
    print("\n-----------------------------      CRTL-C detected: Exiting.         ---------------------------------")
    sys.exit(0)

def extract(dir):

    repo = Repo(dir)
    commits = list(repo.iter_commits('develop'))

    return commits
    
if __name__ == '__main__':

    signal.signal(signal.SIGINT, salida_controlada)

    words = input('Introduce key words (comma as separator): ')
    if words != '':
        
        search = words.split(',')
        commits = extract(DIR)

        found_commits = dict()
        found_commits['leaks'] = []

        for commit in commits:
            for word in search:
                word = word.strip()
                matched = re.search(word, commit.message, re.I)
                if matched:
                    found_commits['leaks'].append({
                        'commit':commit.hexsha,
                        'author':commit.committer.name,
                        'committed date': commit.committed_date,
                        'key word': word,
                        'position in commit': matched})
        if found_commits['leaks'] == []:
            print('No matches found.')
        else:
            print(found_commits)
    
    else:
        print('Search is empty. Exiting.')
