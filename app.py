import streamlit as st
import json
with open('./data/03232024.json') as file:
    data = json.load(file)

# Extracting the dish names
breakfast = data.get("Breakfast", {})
lunch = data.get("Lunch", {})
dinner = data.get("Dinner", {})

# Names of all dishes, will change according to user's choice
all_dishes = []

st.header("Welcome to WingWing! 🧚‍")
# Disliked
forbidden_list = set()

# favorite food
user_input_list = []

# Use a set to store additional elements
additional_elements = []


dietary_Restriction = st.radio(
    "What's your Dietary Restrictions?",
    ["Veggie", "Vegan", "Halal", "None"])
if dietary_Restriction != "None":
    dr_type = dietary_Restriction
    for menu in (breakfast, lunch, dinner):
        for item in menu.values():
            for dish_name, dietary_restrictions in item.items():
                if dr_type in dietary_restrictions:
                    # Add the dish name to the set
                    all_dishes.append(dish_name)
else:
    for menu in (breakfast, lunch, dinner):
        for item in menu.values():
            for dish_name, dietary_restrictions in item.items():
                # Add the dish name to the set
                all_dishes.append(dish_name)
# for item in all_dishes:
#     st.write(item)

forbidden = st.multiselect(
    "What you " + "***DON'T***" + " wanna have?",
    ['Beef', 'Egg', 'Fish', 'Milk', 'Peanuts', 'Pork', 'Shellfish', 'Soy',
     'Wheat', 'Tree Nut', 'Sesame', 'Other']
)
for item in forbidden:
    forbidden_list.add(item)


def clear_form():
    st.session_state["1"] = ""


with st.form("myForm"):
    if 'Other' in forbidden:
        forbidden_list.remove('Other')
        self_forbidden = st.text_input(
            "Can't find what you want? Write below!",
            key="1"
        )
        if self_forbidden:
            additional_elements = additional_elements + [str(self_forbidden)]
        col1, col2 = st.columns(2)
        with col1:
            submit = st.form_submit_button(label="Submit")
        with col2:
            delete = st.form_submit_button(label="Delete", on_click=clear_form)
for item in additional_elements:
    forbidden_list.add(item)
forbidden_string = " ".join(forbidden_list)
# Display the concatenated string

st.write("You already chosen: ", forbidden_string)
filtered_dishes = all_dishes.copy()
for dish in all_dishes:
    for forbidden_item in forbidden_list:
        if forbidden_item.lower() in dish.lower():
            filtered_dishes.remove(dish)
all_dishes = filtered_dishes
# for item in all_dishes:
#     st.write(item)


title = st.text_area('Put your ' + '***favorite***' + ' food into the box! 👇 (use comma to separate)')
if title:
    # Split the text by lines and add each line to the user_input_list
    user_input_list.extend(title.split(','))

    res_dishes = []
    added_names = set()
    for dish in all_dishes:
        for liked_dishes in user_input_list:
            if liked_dishes.lower() in dish.lower() and str(dish) not in added_names:
                res_dishes.append(dish)
                added_names.add(str(dish))
    # for item in res_dishes:
    #     st.write(item)
    # Output result
    if not res_dishes:
        st.header(":rainbow[Oops! J2 doesn't have your favorite foods today]"+"😢")
    else:
        st.balloons()
        st.header(":rainbow[We found them!]" + "🎊")
        for dish_name in res_dishes:
            details = set()
            for meal, meal_data in data.items():
                if meal != "date":
                    for bar, bar_data in meal_data.items():
                        if dish_name in bar_data:
                            details.add((meal, bar))
            st.write("You can find " + ":rainbow[" + dish_name + "]" + " at: ")
            for item in details:
                st.write(item)

