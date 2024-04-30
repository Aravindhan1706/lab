import streamlit as st

# Title of the web app
st.title('Simple Calculator')

# Function to perform addition
def add(a, b):
    return a + b

# Function to perform subtraction
def subtract(a, b):
    return a - b

# Function to perform multiplication
def multiply(a, b):
    return a * b

# Function to perform division
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    else:
        return a / b

# Sidebar to get user input
st.sidebar.header('Enter Values')
a = st.sidebar.number_input("Enter the first number:")
b = st.sidebar.number_input("Enter the second number:")
operation = st.sidebar.selectbox("Select Operation", ("Addition", "Subtraction", "Multiplication", "Division"))

# Perform the selected operation
if operation == "Addition":
    result = add(a, b)
elif operation == "Subtraction":
    result = subtract(a, b)
elif operation == "Multiplication":
    result = multiply(a, b)
elif operation == "Division":
    result = divide(a, b)

# Display the result
st.write(f"Result: {result}")

