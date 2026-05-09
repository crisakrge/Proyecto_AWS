from app import create_app, db
from app.models import User

app = create_app()

def seed():
    with app.app_context():
        # Verificar si el usuario ya existe
        if not User.query.filter_by(email='cristopher.estrada@seidormexico.com').first():
            user = User(
                username='admin_cristopher',
                email='cristopher.estrada@seidormexico.com'
            )
            user.set_password('tu_password_segura') # Cambia esto
            db.session.add(user)
            db.session.commit()
            print("Usuario administrador creado exitosamente.")
        else:
            print("El usuario ya existe.")

if __name__ == "__main__":
    seed()