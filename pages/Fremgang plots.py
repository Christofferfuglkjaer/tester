import streamlit as st
import matplotlib.pyplot as plt

# Page title
st.title("Fremgang Plots")
# Create tabs for different plots
ryg, bryst, random, arme = st.tabs(["Ryg", "Bryst", "Random", "Arme"])

with ryg:
    st.write(st.session_state.workout_data)
    # Check if workout data exists in session state
    if "workout_data" in st.session_state:
        workout_data = st.session_state.workout_data
        # Create a plot for Rows and Reps
        fig, ax = plt.subplots(2, 1, figsize=(10, 8))
        ax[0].scatter(workout_data[2][0], workout_data[3][0], label="Rows")

        ax[0].set_xlabel("Rows")
        ax[0].set_ylabel("Reps")
        ax[0].set_title("Rows vs Reps")
        ax[0].legend()
        #st.pyplot(fig)
        ax[1].scatter(workout_data[1][0],workout_data[2][0], label="Pull Ups", color='orange')
        ax[1].set_xlabel("Pull Ups")
        ax[1].set_ylabel("Reps")
        ax[1].set_title("Pull Ups vs Reps")
        ax[1].legend()
        st.pyplot(fig)

    else:
        st.write("No workout data available.")