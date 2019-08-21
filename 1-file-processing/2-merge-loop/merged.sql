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

CREATE TABLE IF NOT EXISTS users (
    id bigserial PRIMARY KEY,
    first_name varchar(255),
    last_name varchar(255),
    dob timestamptz
);

