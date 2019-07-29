CREATE TABLE IF NOT EXISTS users (
    id bigserial PRIMARY KEY,
    first_name varchar(255),
    last_name varchar(255),
    dob timestamptz
);
