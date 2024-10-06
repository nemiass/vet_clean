import click
from app.core.database import SessionLocal 
from app.models import User
from app.core.security import get_password_hash 

db = SessionLocal()

@click.command()
@click.option('--username', prompt=True, help='El nombre de usuario del root')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='La contraseña del root')
def create_root(username: str, password: str):
    """Comando para crear un usuario root (superusuario)"""
    user = db.query(User).filter(User.username == username).first()
    if user:
        click.echo('Error: El usuario ya existe.')
        return

    hashed_password = get_password_hash(password)
    new_root = User(username=username, password=hashed_password, is_root=True)
    db.add(new_root)
    db.commit()
    db.refresh(new_root)
    click.echo(f'Usuario root creado exitosamente: {username}')

if __name__ == '__main__':
    create_root()
