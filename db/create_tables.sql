CREATE TABLE IF NOT EXISTS users (
    login varchar(255) unique not null primary key,
    name varchar(255),
    email varchar(255),
    status varchar(255),
    skipped int
);

CREATE TABLE IF NOT EXISTS polls (
    id            int unique not null primary key,
    question           varchar(255),
    answer_correct     varchar(255),
    answer_incorrect_1 varchar(255),
    answer_incorrect_2 varchar(255),
    date               date,
    time               time,
    category           varchar(255)
);

CREATE TABLE IF NOT EXISTS answers (
    poll_id int,
    user_login varchar(255),
    date date,
    time time,
    answer int,
    status varchar(255),
    FOREIGN KEY (poll_id) REFERENCES polls(id),
    FOREIGN KEY (user_login) REFERENCES users(login)
);