
from database import setup_database
from models import Category, Drug

def add_category(session):
    name = input("Enter category name: ")
    if session.query(Category).filter_by(name=name).first():
        print("Category already exists.")
        return

    category = Category(name=name)
    session.add(category)
    session.commit()
    print(f"Category '{name}' added successfully.")

def add_drug(session):
    categories = session.query(Category).all()
    if not categories:
        print("No categories available. Please add a category first.")
        return

    print("Available categories:")
    for cat in categories:
        print(f"{cat.id}. {cat.name}")

    category_id = int(input("Select category ID: "))
    category = session.query(Category).filter_by(id=category_id).first()
    if not category:
        print("Invalid category ID.")
        return

    name = input("Enter drug name: ")
    quantity = int(input("Enter drug quantity: "))
    expiration_date = input("Enter expiration date (YYYY-MM-DD): ")

    drug = Drug(name=name, quantity=quantity, expiration_date=expiration_date, category=category)
    session.add(drug)
    session.commit()
    print(f"Drug '{name}' added successfully.")

def view_drugs(session):
    drugs = session.query(Drug).all()
    if not drugs:
        print("No drugs available.")
        return

    for drug in drugs:
        print(f"ID: {drug.id}, Name: {drug.name}, Quantity: {drug.quantity}, Expiration Date: {drug.expiration_date}, Category: {drug.category.name}")

def update_drug(session):
    drug_id = int(input("Enter drug ID to update: "))
    drug = session.query(Drug).filter_by(id=drug_id).first()

    if not drug:
        print("Drug not found.")
        return

    print(f"Current details: Name: {drug.name}, Quantity: {drug.quantity}, Expiration Date: {drug.expiration_date}")
    new_name = input("Enter new drug name (leave blank to keep current): ") or drug.name
    new_quantity = input("Enter new quantity (leave blank to keep current): ")
    new_expiration_date = input("Enter new expiration date (YYYY-MM-DD, leave blank to keep current): ")

    if new_quantity:
        drug.quantity = int(new_quantity)
    drug.name = new_name
    drug.expiration_date = new_expiration_date or drug.expiration_date

    session.commit()
    print(f"Drug '{drug.name}' updated successfully.")

def delete_drug(session):
    drug_id = int(input("Enter drug ID to delete: "))
    drug = session.query(Drug).filter_by(id=drug_id).first()
    if not drug:
        print("Drug not found.")
        return

    drug_name = drug.name
    session.delete(drug)
    session.commit()
    print(f"Drug '{drug_name}' deleted successfully.")

def main():
    session = setup_database()

    while True:
        print("\nPharmacist Drug Management System")
        print("1. Add Category")
        print("2. Add Drug")
        print("3. View Drugs")
        print("4. Update Drug")  # New update option
        print("5. Delete Drug")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            add_category(session)
        elif choice == '2':
            add_drug(session)
        elif choice == '3':
            view_drugs(session)
        elif choice == '4':
            update_drug(session)  # Call the update function
        elif choice == '5':
            delete_drug(session)
        elif choice == '6':
            print("Exiting application.")
            break
        else:
            print("Invalid option. Please select a valid option.")

    session.close()

if __name__ == "__main__":
    main()
