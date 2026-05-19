import streamlit as st
from Bank_Mgmt import Bank

# --- Streamlit App ---

st.set_page_config(page_title="Bank App", layout="centered")
st.title("🏦 Simple Bank Application")

menu = st.sidebar.radio("Choose an option", [
    "Create Account",
    "Deposit Money",
    "Withdraw Money",
    "View Account Details",
    "Update Details",
    "Delete Account"
])

if menu == "Create Account":
    st.header("🧾 Create New Bank Account")
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=0, max_value=120)
    email = st.text_input("Enter your email")
    pin = st.text_input("Set a 4-digit PIN", type="password")

    if st.button("Create Account"):
        if not pin.isdigit() or len(pin) != 4:
            st.error("PIN must be 4 digits.")
        else:
            result = Bank.create_account(name, age, email, int(pin))
            if result["success"]:
                st.success("Account Created Successfully!")
                st.write("Your Account Number:", result["account"]["accountNo"])
            else:
                st.error(result["message"])

elif menu == "Deposit Money":
    st.header("💰 Deposit")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount to Deposit", min_value=1)

    if st.button("Deposit"):
        result = Bank.deposit(acc, int(pin), amount)
        st.success(result["message"]) if result["success"] else st.error(result["message"])

elif menu == "Withdraw Money":
    st.header("🏧 Withdraw")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount to Withdraw", min_value=1)

    if st.button("Withdraw"):
        result = Bank.withdraw(acc, int(pin), amount)
        st.success(result["message"]) if result["success"] else st.error(result["message"])

elif menu == "View Account Details":
    st.header("📄 View Details")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("View"):
        result = Bank.get_details(acc, int(pin))
        if result["success"]:
            st.json(result["details"])
        else:
            st.error(result["message"])

elif menu == "Update Details":
    st.header("✏️ Update Info")
    acc = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")
    name = st.text_input("New Name (optional)")
    email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New 4-digit PIN (optional)")

    if st.button("Update"):
        result = Bank.update_details(acc, int(pin), name, email, int(new_pin) if new_pin else None)
        st.success(result["message"]) if result["success"] else st.error(result["message"])

elif menu == "Delete Account":
    st.header("🗑️ Delete Account")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete Account"):
        result = Bank.delete_account(acc, int(pin))
        st.success(result["message"]) if result["success"] else st.error(result["message"])
