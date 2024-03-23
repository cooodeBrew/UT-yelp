import streamlit as st

st.header("Welcome to WingWing! ")
forbidden_list = set()
# Use a set to store additional elements
additional_elements = set()

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
        self_forbidden = st.text_input(
            "Can't find what you want? Write below!",
            key="1"
        )
        if self_forbidden:
            additional_elements.add(self_forbidden)
            st.write("You have successfully added: ", self_forbidden)
        col1, col2 = st.columns(2)
        with col1:
            submit = st.form_submit_button(label="Submit")
        with col2:
            clear = st.form_submit_button(label="Clear", on_click=clear_form)

        forbidden_list.remove('Other')
for item in additional_elements:
    forbidden_list.add(item)
forbidden_string = " ".join(forbidden_list)
# Display the concatenated string
st.write("You already chosen: ", forbidden_string)


title = st.text_area('Put your favorite food into the box! 👇 (use comma to separate)')
user_input_list = []
if title:
    # Split the text by lines and add each line to the user_input_list
    user_input_list.extend(title.split(','))
st.write("User Input List:", user_input_list)

