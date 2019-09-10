import time
import merge
import os
import shutil

scripts = ["""INSERT INTO users VALUES(1, 'wildan', 'syahidillah', '27-11-1995');
SELECT first_name FROM users WHERE last_name = 'syahidillah';
""", """UPDATE users SET first_name = 'charlie' WHERE first_name = 'wildan';
SELECT first_name FROM users WHERE last_name = 'syahidillah';
INSERT INTO users VALUES(2, "alexander", "syahidillah", "27-11-1995");
""", """SELECT first_name FROM users WHERE last_name = 'syahidillah';
""", """SELECT first_name FROM users WHERE last_name = 'syahidillah';
DELETE FROM users WHERE first_name = 'charlie';
"""]

merge_result = """INSERT INTO users VALUES(1, 'wildan', 'syahidillah', '27-11-1995');
UPDATE users SET first_name = 'charlie' WHERE first_name = 'wildan';
INSERT INTO users VALUES(2, "alexander", "syahidillah", "27-11-1995");
DELETE FROM users WHERE first_name = 'charlie';
"""

def create_dummies():
    if os.path.exists('sqls'):
        shutil.rmtree('sqls')
    os.makedirs('sqls')
    for index, script in enumerate(scripts):
        with open(os.path.join("sqls", str(index) + ".sql"), "w+") as f:
            f.write(script)

def test_merge():
    create_dummies()
    merge.merge()
    with open("merged.sql", "r") as f:
        assert f.read() == merge_result

