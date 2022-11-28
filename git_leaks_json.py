#! user/bin/python3
# cada comit es un diccionario
from git import Repo
import re,time,sys,signal,json



DIR = './skale/skale-manager'
search = ['git','credentials','password','test'] 

def salida_controlada(signal, frame):
    print("CRTL-C detected: Exiting.")
    sys.exit(0)

def extract(dir):

    repo = Repo(dir)
    commits = list(repo.iter_commits('develop'))

    return commits

def load():
    
    time.sleep(1)
    
if __name__ == '__main__':
    
    signal.signal(signal.SIGINT, salida_controlada)

    commits = extract(DIR)

    found_commits = dict()
    found_commits['leaks'] = []

    for commit in commits:
        found = False
        for word in search:
            matched = re.search(word, commit.message, re.I)
            if matched:
                found_commits['leaks'].append({
                    'commit':commit.hexsha,
                    'author':commit.committer.name,
                    'committed date': commit.committed_date,
                    'key word': word,
                    'end position in commit': matched.endpos})

    print(found_commits)
    with open('git_leaks.json','w') as file:
        json.dump(found_commits, file, indent=2)