from mailjet_rest import Client

def send_order_email(customer_email, customer_name, order_id):
    mailjet = Client(
        auth=("39b85ca32926568000ff0fbb453408c4", "c9fa2f323063a6ff87dbcc59ae3e80d9"),
        version="v3.1"
    )

    data = {
        "Messages": [
            {
                "From": {
                    "Email": "urbancartmart@protonmail.com",
                    "Name": "UrbanCart"
                },
                "To": [
                    {
                        "Email": customer_email,
                        "Name": customer_name
                    }
                ],
                "Subject": "Order Confirmation",
                "HTMLPart": f"""
                <h3>Thank you for your purchase!</h3>
                <p>Order ID: #{order_id}</p>
                <a href="https://urbancart.duckdns.org/order/{order_id}">
                    View Order
                </a>
                """
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print("Status:", result.status_code)
    print(result.json())    