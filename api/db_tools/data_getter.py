from sqlalchemy.orm import sessionmaker

from tables import Users, engine

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add a new task
new_user = Users(user_name='Btest test', telegram_id='12')
session.add(new_user)
session.commit()

# Query the tasks
users = session.query(Users).all()
for user in users:
    print(user.user_id, user.user_name, user.telegram_id)

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
