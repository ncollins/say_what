import sqlite3
import config

if __name__ == '__main__':
    conn = sqlite3.connect(config.DATABASE)
    c = conn.cursor()
    c.execute("""
              CREATE TABLE bills (
              congress INTEGER NOT NULL,
              chamber STRING NOT NULL,
              billNo INTEGER NOT NULL,
              introDate STRING,
              sponsorId STRING,
              title STRING,
              file STRING,
              PRIMARY KEY (congress, chamber, billNo)
              );
              """)
    conn.commit()
    c.close()

