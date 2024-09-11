from datetime import datetime

DATABASE_NAME = 'webstore.db'

def get_prices_table():
    return [
                (1, datetime(2020, 6, 14, 00, 00, 00), datetime(2020, 12, 31, 23, 59, 59), 1, 35455, 0, 32.5, 'USD'),
                (1, datetime(2020, 6, 14, 15, 00, 00), datetime(2020, 6, 14, 18, 30, 00), 2, 35455, 1, 25.45, 'USD'),
                (1, datetime(2020, 6, 15, 00, 00, 00), datetime(2020, 6, 15, 11, 00, 00), 3, 35455, 1, 30.5, 'USD'),
                (1, datetime(2020, 6, 15, 16, 00, 00), datetime(2020, 12, 31, 23, 59, 59), 4, 35455, 1, 38.95, 'USD')
            ]