import merge
import os.path

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

def test_merge():
    merge.merge()
    assert os.path.exists("merged.sql")
    assert os.path.isfile("merged.sql")
    with open("merged.sql", "r") as f:
        assert f.read() == merge_result

