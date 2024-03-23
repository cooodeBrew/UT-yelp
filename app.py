import streamlit as st

st.header("Welcome to WingWing! ")
# Disliked
forbidden_list = set()

# favorite food
user_input_list = []

# Use a set to store additional elements
additional_elements = []

# key number
# key_number = 1


dietary_Restriction = st.radio(
    "What's your Dietary Restrictions?",
    [":rainbow[Vegetarian]", ":rainbow[Vegan]", ":rainbow[Halal]", ":rainbow[None]"])


forbidden = st.multiselect(
    "What you " + "***DON'T***" + " wanna have?",
    ['Beef', 'Egg', 'Fish', 'Milk', 'Peanuts', 'Pork', 'Shellfish', 'Soy', 'Tree Nut', 'Sesame Seeds', 'Other']
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
            for item in additional_elements:
                st.write(item)
            # st.write("You have successfully added: ", self_forbidden)
        col1, col2, col3 = st.columns(3)
        with col1:
            submit = st.form_submit_button(label="Submit")
        # with col2:
        #     ad = st.form_submit_button(label="Add", on_click=add)
        with col3:
            delete = st.form_submit_button(label="Delete", on_click=clear_form)
        if submit:
            pass
for item in additional_elements:
    forbidden_list.add(item)
forbidden_string = " ".join(forbidden_list)
# Display the concatenated string
st.write("You already chosen: ", forbidden_string)


title = st.text_area('Put your favorite food into the box! 👇 (use comma to separate)')
if title:
    # Split the text by lines and add each line to the user_input_list
    user_input_list.extend(title.split(','))
st.write("User Input List:", user_input_list)

