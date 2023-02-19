import psycopg2


class DbCon:
    def __init__(self):
        self.con = self._connect_to_db()

    @staticmethod
    def _connect_to_db():
        try:
            con = psycopg2.connect(
                database="postgres",
                user="postgres",
                password="1234",
                host="localhost",
                port="5432"
            )
        except Exception:
            raise ConnectionError("Failed to connect db")

        return con

    def __del__(self):
        self.con.close()


class DbAdmin(DbCon):
    def __init__(self):
        super(DbAdmin, self).__init__()

    def _get_max_poll_id(self):
        # TODO check 0 polls
        cur = self.con.cursor()
        cur.execute("""
        SELECT MAX(id) FROM polls;
        """)

        max_id = cur.fetchone()[0]
        cur.close()

        return max_id

    def add_poll(self, question: str, answer_correct: str, answer_incorrect_1: str,
                 answer_incorrect_2: str, date: str, time: str, category: str):
        # date format (YYYY-MM-DD) time format (HH:MM)
        cur = self.con.cursor()
        poll_id = self._get_max_poll_id() + 1

        sql = """
        INSERT INTO polls(id, question, answer_correct, answer_incorrect_1, answer_incorrect_2, date, time, category)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """
        cur.execute(sql, (poll_id, question, answer_correct, answer_incorrect_1,
                    answer_incorrect_2, date, time, category))

        self.con.commit()

    def del_poll(self, poll_id: int):
        cur = self.con.cursor()
        sql = """
        DELETE FROM polls
        WHERE id = %s;
        """

        cur.execute(sql, (poll_id, ))
        self.con.commit()

    def edit_poll(self, poll_id: int, field: str, value: any):
        # edit one field TODO all fields (mb by dict)
        field = "{}".format(field)
        cur = self.con.cursor()
        sql = """
        UPDATE polls 
        SET %s = %s
        WHERE id = %s;
        """

        cur.execute(sql, (psycopg2.extensions.AsIs(field), value, poll_id))
        self.con.commit()

    def edit_user_status(self, user_login: str, status: str):
        cur = self.con.cursor()
        sql = """
        UPDATE users
        SET status = %s
        WHERE login = %s;
        """

        cur.execute(sql, (status, user_login))
        self.con.commit()

    def get_all_answers(self) -> list:
        cur = self.con.cursor()
        sql = """
        SELECT *
        FROM answers;
        """
        cur.execute(sql)
        res = [item for item in cur]

        return res

    def get_answers_by_field(self, field: str, value: any) -> list:
        cur = self.con.cursor()
        sql = """
        SELECT * 
        FROM answers
        WHERE %s = %s;
        """

        cur.execute(sql, (psycopg2.extensions.AsIs(field), value))
        cur.execute(sql)
        res = [item for item in cur]

        return res

    def get_all_polls(self) -> list:
        cur = self.con.cursor()
        sql = """
        SELECT *
        FROM polls;
        """
        cur.execute(sql)
        res = [item for item in cur]

        return res

    def get_polls_by_field(self, field: str, value: any) -> list:
        cur = self.con.cursor()
        sql = """
        SELECT * 
        FROM polls
        WHERE %s = %s;
        """

        cur.execute(sql, (psycopg2.extensions.AsIs(field), value))
        cur.execute(sql)
        res = [item for item in cur]

        return res


class DbUser(DbCon):
    def __init__(self):
        super(DbUser, self).__init__()

    def is_user_exists(self, login: str) -> int:
        cur = self.con.cursor()
        sql = """
        SELECT COUNT(1)
        FROM users
        WHERE login = %s;
        """

        cur.execute(sql, (login, ))
        amount = cur.fetchone()[0]

        return amount

    def add_user(self, login: str, name: str, email: str, status: str):
        cur = self.con.cursor()
        sql = """
        INSERT INTO users(login, name, email, status, skipped)
        VALUES (%s, %s, %s, %s, %s);
        """

        cur.execute(sql, (login, name, email, status, 0))
        self.con.commit()

    def add_answer(self, poll_id: int, login: str, date: str, time: str, answer: int, status: str):
        # date format (YYYY-MM-DD) time format (HH:MM)
        cur = self.con.cursor()
        sql = """
        INSERT INTO answers(poll_id, user_login, date, time, answer, status) 
        VALUES (%s, %s, %s, %s, %s, %s);
        """
        cur.execute(sql, (poll_id, login, date, time, answer, status))
        self.con.commit()

    def add_answer_skipped(self, poll_id: int, login: str, date: str, time: str):
        cur = self.con.cursor()
        sql = """
        INSERT INTO answers(poll_id, user_login, date, time, answer, status) 
        VALUES (%s, %s, %s, %s, %s, %s);
        """
        cur.execute(sql, (poll_id, login, date, time, 0, 'skipped'))
        self.con.commit()

    def get_skipped(self, login):
        cur = self.con.cursor()
        sql = """
        SELECT skipped 
        FROM users
        WHERE login = %s;
        """

        cur.execute(sql, (login, ))
        amount = cur.fetchone()[0]

        return amount

    def get_user_status(self, login):
        cur = self.con.cursor()
        sql = """
        SELECT status 
        FROM users
        WHERE login = %s;
        """

        cur.execute(sql, (login,))
        status = cur.fetchone()[0]

        return status
