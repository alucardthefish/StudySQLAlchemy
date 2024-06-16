from models import Program, Section, Class
import db


def select_table(table_name):
    check = {
        "program": Program,
        "section": Section,
        "class": Class
    }
    table = check.get(table_name, None)
    if table:
        result = db.session.query(table).all()
        for res in result:
            print(res)
    else:
        print("Inserted value is not a table")

if __name__ == "__main__":
    while (selected_table := input("Insert table name: ")) != "exit":
        select_table(selected_table)
