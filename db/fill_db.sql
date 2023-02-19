INSERT INTO users(login, name, email, status, skipped) VALUES ('user1', 'Ivan', 'ivan@gmail.com', 'block_poll', 0);
INSERT INTO users(login, name, email, status, skipped) VALUES ('user2', 'Petr', 'petr@gmail.com', 'poll', 0);
INSERT INTO users(login, name, email, status, skipped) VALUES ('user3', 'Andrew', 'andrew@gmail.com', 'poll', 2);
INSERT INTO users(login, name, email, status, skipped) VALUES ('user4', 'Alex', 'alex@gmail.com', 'poll', 1);
INSERT INTO users(login, name, email, status, skipped) VALUES ('user5', 'Kir', 'kir@gmail.com', 'poll', 0);
INSERT INTO users(login, name, email, status, skipped) VALUES ('user6', 'Sonya', 'sonya@gmail.com', 'poll', 1);
INSERT INTO users(login, name, email, status, skipped) VALUES ('user7', 'Ars', 'ars@gmail.com', 'block_poll', 0);

INSERT INTO polls(id, question, answer_correct, answer_incorrect_1, answer_incorrect_2, date, time, category)
VALUES (1, 'quest1?', 'answer11', 'answer12', 'answer13', '2023-11-10', '10:30', 'color');
INSERT INTO polls(id, question, answer_correct, answer_incorrect_1, answer_incorrect_2, date, time, category)
VALUES (2, 'quest2?', 'answer21', 'answer22', 'answer23', '2023-10-10', '11:30', 'color');
INSERT INTO polls(id, question, answer_correct, answer_incorrect_1, answer_incorrect_2, date, time, category)
VALUES (3, 'quest3?', 'answer31', 'answer32', 'answer33', '2023-11-10', '12:30', 'computer');

INSERT INTO answers(poll_id, user_login, date, time, answer, status)
VALUES (1, 'user1', '2023-11-10', '10:32', 2, 'incorrect');
INSERT INTO answers(poll_id, user_login, date, time, answer, status)
VALUES (1, 'user2', '2023-11-10', '10:33', 1, 'correct');
INSERT INTO answers(poll_id, user_login, date, time, answer, status)
VALUES (1, 'user3', '2023-11-10', '10:31', 0, 'skipped');
INSERT INTO answers(poll_id, user_login, date, time, answer, status)
VALUES (2, 'user4', '2023-10-10', '11:30', 1, 'correct');
INSERT INTO answers(poll_id, user_login, date, time, answer, status)
VALUES (2, 'user2', '2023-10-10', '11:31', 3, 'incorrect');
INSERT INTO answers(poll_id, user_login, date, time, answer, status)
VALUES (2, 'user5', '2023-10-10', '11:32', 1, 'correct');
INSERT INTO answers(poll_id, user_login, date, time, answer, status)
VALUES (3, 'user3', '2023-11-10', '12:31', 1, 'correct');
INSERT INTO answers(poll_id, user_login, date, time, answer, status)
VALUES (3, 'user6', '2023-11-10', '12:32', 0, 'skipped');
