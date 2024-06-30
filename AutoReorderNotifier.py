import yagmail

# Inventory data
inventory = {
    "Beer": 100,
    "Snacks": 50,
    "Foods": 20
}

# Reorder thresholds
reorder_thresholds = {
    "Beer": 20,
    "Snacks": 10,
    "Foods": 50
}

# Email settings
email_from_username = "anandnavsanya"
email_to = "navsanyanand@gmail.com"
email_subject = "Reorder Notification"
email_password = "opfd qrpr vrgl vybu"  # Store password securely in a separate file or environment variable

def check_inventory():
    low_inventory_products = [product for product, quantity in inventory.items() if quantity <= reorder_thresholds[product]]
    if low_inventory_products:
        send_notification(low_inventory_products)

def send_notification(products):
    msg = f"Reorder the following products: {', '.join(products)}"

    yag = yagmail.SMTP(email_from_username, email_password)
    yag.send(email_to, email_subject, msg)

check_inventory()