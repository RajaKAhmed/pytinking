from flask import Flask, render_template, request

app = Flask(__name__)

# Menu items
menu_items = [
    'Student',
    'Doctor',
    'Mathematician',
    'Engineer',
    'Banker',
    'Musician',
    'Silly Person'
]

# Home page with menu
@app.route('/')
def home():
    return render_template('menu.html', menu_items=menu_items)

# Route for handling item selection
@app.route('/select', methods=['POST'])
def select():
    selected_item = request.form['item']
    
    # Call corresponding function based on selected item
    if selected_item == 'Student':
        return item1_function()
    elif selected_item == 'Doctor':
        return item2_function()
    elif selected_item == 'Mathematician':
        return item3_function()
    elif selected_item == 'Engineer':
        return item4_function()
    elif selected_item == 'Banker':
        return item5_function()
    elif selected_item == 'Musician':
        return item6_function()
    elif selected_item == 'Silly Person':
        return item7_function()
    else:
        return 'Invalid selection'

# Functions for each menu item
def item1_function():
    
    return 'You selected Student'

def item2_function():
    return 'You selected Doctor'

def item3_function():
    return 'You selected Mathematician'

def item4_function():
    return 'You selected Engineer'

def item5_function():
    return 'You selected Banker'

def item6_function():
    return 'You selected Musician'

def item7_function():
    return 'You selected Silly Person'

if __name__ == '__main__':
    app.run()
