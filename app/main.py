from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(movie: str,
                 customers: list,
                 hall_number: int,
                 cleaner: str) -> None:
    customers_ = []
    for customer in customers:
        customers_.append(Customer(customer["name"], customer["food"]))
    for customer in customers_:
        CinemaBar.sell_product(customer, customer.food)
    cleaner_staff = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customers_, cleaner_staff)
