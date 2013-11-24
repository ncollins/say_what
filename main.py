import sqlite3
import datetime

import config

from bill_search import count_matches, words, title_phrases
from wordsearch import count_phrase_for_legislator 

TODAY = datetime.date.today().isoformat()

def main():
    conn = sqlite3.connect(config.DATABASE)
    c = conn.cursor()
    c.execute("""
              SELECT * FROM bills;
              """)
    bills = c.fetchmany(200)
    for (congress, chamber, number, introduced_on, sponsor, title, file_path) in bills:
        check_date = datetime.datetime.strptime(introduced_on, '%Y-%m-%d') - datetime.timedelta(90)
        with open(file_path) as f:
            phrases = list(title_phrases(title)) + ['obamacare', 'clinton', 'war', 'jobs', 'budget', 'weapon', 'syria', 'military']
            print(file_path)
            print('{0}: {1}'.format(number, title))
            print('{0}: {1} other docs'.format(number, count_matches(words, f.read())))
            #print('{0}: sponsored by {1}'.format(number, sponsor))
            for p in phrases:
                    n, c = count_phrase_for_legislator(p, sponsor, check_date, TODAY)
                    print('{0}: {1} mentioned {2} {3} times'.format(number, n, p, str(c)))
            print('\n')


if __name__ == '__main__':
    main()
