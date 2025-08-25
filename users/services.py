import stripe
from config.settings import STRIPE_SECRET_KEY
from forex_python.converter import CurrencyRates

stripe.api_key = STRIPE_SECRET_KEY

def convert_rub_to_dollar(amount):
    c = CurrencyRates()
    rate = c.get_rate('RUB', 'USD')
    return int(amount * rate)

def create_stripe_product(name):
    product = stripe.Product.create(name=name)
    return product


def create_stripe_price(product, amount):
    price = stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product=product,
    )
    return price


def create_stripe_session(price):
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")


def retrieve_session(session_id):
    return stripe.checkout.Session.retrieve(session_id)