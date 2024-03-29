# import os 
from app import create_app,db
from flask_script import Manager, Shell,Server
from app.models import User
from flask_migrate import Migrate,MigrateCommand



app = create_app('test')
app = create_app('production')
app = create_app('development')


manager = Manager(app)

migrate = Migrate(app,db)

manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    '''
    Run the unit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict( app=app, db=db, User=User)

app.config['SECRET_KEY'] ='samm'

if __name__ == '__main__':
    manager.run()