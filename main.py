# Q2 Skills Test: Periodic Table Information Finder
from pyscript import display, document


non_metals = {
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.003),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.07),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.9),
    "Se": ("Selenium", 34, 78.96),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I": ("Iodine", 53, 126.905),
    "Xe": ("Xenon", 54, 131.293),
    "Rn": ("Radon", 86, 222),
}

def get_element (e):
    document.getElementById('result').innerHTML = " " # Clears previous answer

    element = document.getElementById('element_symbol').value.title().strip() # Allows user input not to be case sensitive

    result = non_metals.get( # Uses .get() to find element
    element, ("Element not found", "-", "-")
    )

    # Displays information
    document.getElementById('result').innerHTML = f""" 
    <b>Chemical Symbol:</b> {element}<br>
    <b>Element Name:</b> {result[0]}<br>
    <b>Atomic Number:</b> {result[1]}<br>
    <b>Atomic Mass:</b> {result[2]}
    """