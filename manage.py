from app import create_app
from app.models import Quote
from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand


# Creating app instance
app = create_app('development')
manager = Manager(app)
manager.add_command('server',Server)


@manager.command
def tests():
  import unittest
  tests = unittest.TestLoader().discover('tests')
  unittest.TextTestRunner(verbosity = 2).run(tests)

@manager .shell
def make_shell_context():
  return dict(app = app,Quote=Quote )

migrate = Migrate(app)
manager.add_command('db',MigrateCommand)  



if __name__ == '__main__':
    manager.run()