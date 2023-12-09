from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tables import Users, Base


# Create the database engine
engine = create_engine('sqlite:///todo.db', echo=True)  # 'echo=True' enables logging of SQL commands

# Create a base class for our class definitions



# Create the table in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add a new task
new_user = Users(user_name='Btest test')
session.add(new_user)
session.commit()

# Query the tasks
users = session.query(Users).all()
for user in users:
    print(user.user_id, user.user_name)

# # Update a task
# task_to_update = session.query(TodoItem).filter_by(task='Buy groceries').first()
# task_to_update.completed = True
# session.commit()

# # Delete a task
# task_to_delete = session.query(TodoItem).filter_by(task='Buy groceries').first()
# session.delete(task_to_delete)
# session.commit()

# Close the session when done
session.close()
