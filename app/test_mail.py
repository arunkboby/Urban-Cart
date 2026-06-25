from app.email_utils import send_order_email

send_order_email(
    customer_email="playergamesthere@gmail.com",
    customer_name="A",
    order_id=123
)