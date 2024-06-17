from sqlalchemy import update
from datetime import datetime
from models import Program, Section, Class
import db
from db_session import db_session


def update_program_dates(program_id, new_start_date, new_end_date):
    try:
        # Update the Program dates
        db.session.execute(
            update(Program)
            .where(Program.id == program_id)
            .values(start_date=new_start_date, end_date=new_end_date)
        )

        # Adjust Section dates within the new Program date range
        db.session.execute(
            update(Section)
            .where(Section.program_id == program_id)
            .where(Section.start_date < new_start_date)
            .values(start_date=new_start_date)
        )
        db.session.execute(
            update(Section)
            .where(Section.program_id == program_id)
            .where(Section.end_date > new_end_date)
            .values(end_date=new_end_date)
        )

        # Adjust Class dates within the adjusted Section date range
        db.session.execute(
            update(Class)
            .where(Class.section_id.in_(
                db.session.query(Section.id).filter(Section.program_id == program_id)
            ))
            .where(Class.start_date < new_start_date)
            .values(start_date=new_start_date)
        )
        db.session.execute(
            update(Class)
            .where(Class.section_id.in_(
                db.session.query(Section.id).filter(Section.program_id == program_id)
            ))
            .where(Class.end_date > new_end_date)
            .values(end_date=new_end_date)
        )

        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Error: {e}")
    finally:
        db.session.close()


def show_changes_for_program(program_id):
    # Verify the changes
    try:
        updated_program = db.session.query(Program).filter_by(id=program_id).one()
        print(f"Program: {updated_program.name}, Start Date: {updated_program.start_date}, End Date: {updated_program.end_date}")
        for section in updated_program.sections:
            print(f"  Section: {section.name}, Start Date: {section.start_date}, End Date: {section.end_date}")
            for cls in section.classes:
                print(f"      Class: {cls.name}, Start Date: {cls.start_date}, End Date: {cls.end_date}")
    except Exception:
        print(f"No program found with that id.")


def update_class_name(class_id, name):
    with db_session():
        my_class = db.session.query(Class).filter(Class.id == class_id).first()
        if my_class:
            my_class.name = name
        else:
            print("No class found with that id")



if __name__ == "__main__":
    print("---Visualizer-for-dates-under-programs---")
    # Update program dates and adjust section and class dates
    update_program_dates(program_id=1, new_start_date=datetime(2022, 1, 15), new_end_date=datetime(2025, 5, 6))

    show_changes_for_program(1)
