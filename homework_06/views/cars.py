import logging

from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.exc import DatabaseError, IntegrityError
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError

from models import db, Car

cars_app = Blueprint("cars_app", __name__)


@cars_app.route("/", endpoint="list")
def list_cars():
    cars = Car.query.order_by(Car.id).all()
    return render_template(
        "cars/list.html",
        cars=cars,
    )


def get_car_name_from_form():
    car_name = request.form.get("car-name")
    if name := (car_name and car_name.strip()):
        return name


def get_car_is_new_from_form():
    is_new = request.form.get("is_new")
    return bool(is_new)


def save_car(car_name):
    try:
        db.session.commit()
    except IntegrityError as ex:
        logging.warning("got integrity error with text %s", ex)
        raise BadRequest(f"Could not save car {car_name}, probably name is not unique")
    except DatabaseError:
        db.session.rollback()
        logging.exception("got db error!")
        raise InternalServerError(f"could not save car with name {car_name}!")


@cars_app.route("/<int:car_id>/", methods=["GET", "POST"], endpoint="details")
def get_car_by_id(car_id: int):
    car = Car.query.get(car_id)
    if car is None:
        raise NotFound(f"Car with id #{car_id} not found!")

    if request.method == "GET":
        return render_template(
            "cars/details.html",
            car=car,
        )

    car_name = get_car_name_from_form()
    if Car.name == car_name:
        raise BadRequest(f"this car is already named {car_name}")
    if Car.query.filter_by(name=car_name).count():
        raise BadRequest(f"car with name {car_name!r} already exists!")

    Car.name = car_name
    Car.is_new = get_car_is_new_from_form()

    save_car(car_name)
    return redirect(url_for("cars_app.details", car_id=car.id))


@cars_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_car():
    if request.method == "GET":
        return render_template("cars/add.html")

    car_name = get_car_name_from_form()
    is_new = get_car_is_new_from_form()
    car = Car(name=car_name, is_new=is_new)
    db.session.add(car)
    save_car(car.name)
    return redirect(url_for("cars_app.details", car_id=car.id))