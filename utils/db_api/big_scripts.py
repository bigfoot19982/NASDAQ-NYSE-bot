# preparing scripts for postgresql.py file

create_tab_companies = """
        CREATE TABLE IF NOT EXISTS companies (
        company_name varchar(30) NOT NULL PRIMARY KEY
        )
        """

create_tab_users = """
        CREATE TABLE IF NOT EXISTS users (
        user_id int NOT NULL,
        company_name varchar(30) REFERENCES companies(company_name),
        user_name varchar(200) NOT NULL,
        last_news text
        )
        """

add_comp = "INSERT INTO companies (company_name) VALUES ($1)"

add_user = "INSERT INTO users (user_id, company_name, user_name) VALUES ($1, $2, $3)"

check_if_exists = "SELECT COUNT(*) FROM users WHERE user_id = $1 AND company_name = ($2)"

unsubscribe = "DELETE FROM users WHERE user_id = $1 AND company_name = ($2)"

count_comps = "SELECT COUNT(*) FROM users WHERE company_name = ($1)"

delete = "DELETE FROM companies WHERE company_name = $1"

all_comps = "SELECT * FROM companies"

comp_subscribers = "SELECT user_id, last_news FROM users WHERE company_name = ($1)"

set_hash = "UPDATE users SET last_news = $1 WHERE user_id = $2 AND company_name = $3"