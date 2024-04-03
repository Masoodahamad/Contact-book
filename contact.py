import tkinter as tk

contacts = {}

def add_contact(name, phone, email, address):
    contacts[name] = {'phone': phone, 'email': email, 'address': address}

def view_contacts():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name}: {details['phone']}")

def search_contact(keyword):
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        if keyword.lower() in name.lower() or keyword in details['phone']:
            contact_list.insert(tk.END, f"{name}: {details['phone']}")

def update_contact(name, phone, email, address):
    if name in contacts:
        contacts[name] = {'phone': phone, 'email': email, 'address': address}

def delete_contact(name):
    if name in contacts:
        del contacts[name]

def add_contact_window():
    add_window = tk.Toplevel(window)
    add_window.title("Add Contact")

    tk.Label(add_window, text="Name:").grid(row=0, column=0)
    tk.Label(add_window, text="Phone:").grid(row=1, column=0)
    tk.Label(add_window, text="Email:").grid(row=2, column=0)
    tk.Label(add_window, text="Address:").grid(row=3, column=0)

    name_entry = tk.Entry(add_window)
    phone_entry = tk.Entry(add_window)
    email_entry = tk.Entry(add_window)
    address_entry = tk.Entry(add_window)

    name_entry.grid(row=0, column=1)
    phone_entry.grid(row=1, column=1)
    email_entry.grid(row=2, column=1)
    address_entry.grid(row=3, column=1)

    def add_and_close():
        add_contact(name_entry.get(), phone_entry.get(), email_entry.get(), address_entry.get())
        view_contacts()
        add_window.destroy()

    tk.Button(add_window, text="Add Contact", command=add_and_close).grid(row=4, columnspan=2)

def search_contact_window():
    search_window = tk.Toplevel(window)
    search_window.title("Search Contact")

    tk.Label(search_window, text="Search:").grid(row=0, column=0)
    search_entry = tk.Entry(search_window)
    search_entry.grid(row=0, column=1)

    def search():
        search_contact(search_entry.get())
        search_window.destroy()

    tk.Button(search_window, text="Search", command=search).grid(row=1, columnspan=2)

def update_contact_window():
    update_window = tk.Toplevel(window)
    update_window.title("Update Contact")

    tk.Label(update_window, text="Name:").grid(row=0, column=0)
    tk.Label(update_window, text="Phone:").grid(row=1, column=0)
    tk.Label(update_window, text="Email:").grid(row=2, column=0)
    tk.Label(update_window, text="Address:").grid(row=3, column=0)

    name_entry = tk.Entry(update_window)
    phone_entry = tk.Entry(update_window)
    email_entry = tk.Entry(update_window)
    address_entry = tk.Entry(update_window)

    name_entry.grid(row=0, column=1)
    phone_entry.grid(row=1, column=1)
    email_entry.grid(row=2, column=1)
    address_entry.grid(row=3, column=1)

    def update_and_close():
        update_contact(name_entry.get(), phone_entry.get(), email_entry.get(), address_entry.get())
        view_contacts()
        update_window.destroy()

    tk.Button(update_window, text="Update Contact", command=update_and_close).grid(row=4, columnspan=2)

def delete_contact_window():
    delete_window = tk.Toplevel(window)
    delete_window.title("Delete Contact")

    tk.Label(delete_window, text="Name:").grid(row=0, column=0)
    name_entry = tk.Entry(delete_window)
    name_entry.grid(row=0, column=1)

    def delete_and_close():
        delete_contact(name_entry.get())
        view_contacts()
        delete_window.destroy()

    tk.Button(delete_window, text="Delete Contact", command=delete_and_close).grid(row=1, columnspan=2)

# Create main window
window = tk.Tk()
window.title("Contact Management System")

# Create buttons
add_button = tk.Button(window, text="Add Contact", command=add_contact_window)
add_button.grid(row=0, column=0, padx=5, pady=5)

search_button = tk.Button(window, text="Search Contact", command=search_contact_window)
search_button.grid(row=0, column=1, padx=5, pady=5)

update_button = tk.Button(window, text="Update Contact", command=update_contact_window)
update_button.grid(row=0, column=2, padx=5, pady=5)

delete_button = tk.Button(window, text="Delete Contact", command=delete_contact_window)
delete_button.grid(row=0, column=3, padx=5, pady=5)

# Create contact list
contact_list = tk.Listbox(window, width=50)
contact_list.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Run the application
window.mainloop()
