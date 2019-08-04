import time
import merge
import os
import shutil

merge_result = """CREATE TABLE IF NOT EXISTS users (
    id bigserial PRIMARY KEY,
    first_name varchar(255),
    last_name varchar(255),
    dob timestamptz
);

CREATE TABLE IF NOT EXISTS schools (
    id bigserial PRIMARY KEY,
    name varchar(255),
    level varchar(10)
);

CREATE TABLE IF NOT EXISTS user_schools (
    user_id bigint,
    school_id bigint,
    joined timestamptz,
    left timestamptz,
    PRIMARY key(user_id, school_id)
);
"""

def create_dummies():
    if os.path.exists('sqls'):
        shutil.rmtree('sqls')
    os.makedirs('sqls')
    users = os.path.join('sqls', 'users_' + str(time.time()) + '.sql')
    schools = os.path.join('sqls', 'schools_' + str(time.time()) + '.sql')
    with open(users, 'w+') as f:
        with open('users.sql', 'r') as f2:
            f.write(f2.read())
    with open(schools, 'w+') as f:
        with open('schools.sql', 'r') as f2:
            f.write(f2.read())

def test_merge():
    create_dummies()
    merge.merge()
    with open("merged.sql", "r") as f:
        assert f.read() == merge_result

