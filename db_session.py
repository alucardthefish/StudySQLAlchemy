from contextlib import contextmanager
import db


@contextmanager
def db_session(autocommit=True):
    try:
        yield db.session
        if autocommit:
            db.session.commit()
    except Exception:
        db.session.rollback()
        raise
    finally:
        db.session.reset() # for flask-sqlalchemy db.session.remove()
