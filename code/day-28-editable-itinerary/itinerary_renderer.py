from utils.airport_renderer import render_airport_transfer
from utils.daily_itinerary_renderer import render_daily_itinerary


def render_itinerary(data):
    render_airport_transfer(data)
    render_daily_itinerary(data)
