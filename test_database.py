from datetime import date

from app import create_app
from app.extensions import db
from app.models import User, Service, Appointment


app = create_app()


with app.app_context():

    user = User(
        name="Rajvi",
        email="rajvi@2test.com",
        password_hash="test-password"
    )

    service = Service(
        name="Haircut",
        description="Basic haircut",
        duration=30
    )

    db.session.add(user)
    db.session.add(service)

    db.session.commit()

    appointment1 = Appointment(
        user_id=user.id,
        service_id=service.id,
        appointment_date=date.today(),
        token_number=1,
        status="Waiting"
    )

    appointment2 = Appointment(
        user_id=user.id,
        service_id=service.id,
        appointment_date=date.today(),
        token_number=2,
        status="Waiting"
    )

    db.session.add(appointment1)
    db.session.add(appointment2)

    db.session.commit()

    print("Customer:", user.name)

    print(
        "Number of appointments:",
        len(user.appointments)
    )

    for appointment in user.appointments:
        print(
            "Token:",
            appointment.token_number
        )

    # Cleanup

    db.session.delete(appointment1)
    db.session.delete(appointment2)
    db.session.delete(service)
    db.session.delete(user)

    db.session.commit()

    print("Test data deleted.")
