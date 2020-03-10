from urls import app
from flask_script import Manager

manager = Manager(app)


@manager.command
def run():
    app.run()


if __name__ == "__main__":
    manager.run()
