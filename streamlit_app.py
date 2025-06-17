import streamlit as st
import datetime as dt
st.session_state.pull_ups = []
st.session_state.rows = []
st.session_state.reps = []
st.session_state.pull_ups_reps = []
# Initialize workout data in session state
if "workout_data" not in st.session_state:
    st.session_state.workout_data = [[] for _ in range(5)]  # Adjust number of lists as needed

# Page title
ryg, bryst, random, arme = st.tabs(["Ryg", "Bryst", "Random", "Arme"])

# Ryg tab content
with ryg:

    # First row: Rows
    left, middle, right = st.columns([3, 3, 1],)
    with left:
        rows = st.text_input("Rows", value="", key="rows_input")
    with middle:
        reps = st.text_input("Reps", value="", key="reps_input")
    with right:
        st.markdown("<br>", unsafe_allow_html=True)  # Push button down to align with inputs
        if st.button("Submit", key="ryg_submit"):
            # Store the input data in the workout_data dictionary
            st.session_state.workout_data[2].append(dt.datetime.now().strftime("%Y-%m-%d"))

            st.session_state.workout_data[3].append(int(rows)*int(reps))
            st.success("Data submitted successfully!")

    # Second row: Pull ups
    left2, middle2, right2 = st.columns([3, 3, 1])
    with left2:
        pull_ups = st.text_input("Pull ups", value="", key="pull_ups_input")
    with middle2:
        pull_ups_reps = st.text_input("Reps", value="", key="pull_ups_reps_input")
    with right2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Submit", key="pull_ups_submit",use_container_width=True):
            # Store the input data in the workout_data dictionary
            st.session_state.workout_data[0].append(dt.datetime.now().strftime("%Y-%m-%d"))
            st.session_state.workout_data[1].append(pull_ups_reps*pull_ups)
            st.success("Data submitted successfully!")
    
    st.write("Workout Data:", st.session_state.workout_data)
    st.write(st.session_state.workout_data[0])
    

# # Bryst tab content
# with bryst:

#     left.text_input("Rows", value=None, key="bryst_rows_input")
#     middel.text_input("reps", value=None, key="bryst_reps_input")
#     if st.button("Submit", key="bryst_submit"):
#         st.write("Data submitted successfully!")

# # Random tab content
# with random:
#     left.text_input("Rows", value=None, key="random_rows_input")
#     middel.text_input("reps", value=None, key="random_reps_input")
#     if right.button("Submit", key="random_submit"):
#         st.write("Data submitted successfully!")


# # Arme tab content
# with arme:
#     left.text_input("Rows", value=None, key="arme_rows_input")
#     middel.text_input("reps", value=None, key="arme_reps_input")
#     if st.button("Submit", key="arme_submit"):
#         st.write("Data submitted successfully!")