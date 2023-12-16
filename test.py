if __name__ == "__main__":

    from sqlalchemy.orm import sessionmaker

    from api.db_tools.tables import Users, engine

    Session = sessionmaker(bind=engine)
    session = Session()
    users = session.query(Users).all()
    for user in users:
        print('-------------')
        for column in Users.__table__.columns:
            print(column.name, ':',  getattr(user, column.name))
        
        # print(user.user_id, user.user_name, user.is_admin, user.telegram_id)