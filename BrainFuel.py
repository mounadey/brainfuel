import streamlit as st

st.title("BrainFuel")
st.subheader("Calculateur de fonctions mathématiques") 

with st.form("search_form"):
    st.write("Entrez une fonction de x. Exemple : x**2 + 3*x + 2")
    search_query = st.text_input("Entrez votre fonction de x :")

    submitted = st.form_submit_button("Plotter")
    if submitted:
        import sympy as sp
        import matplotlib.pyplot as plt
        import numpy as np
        
        try:
            x = sp.symbols('x')
            f_x = sp.simplify(search_query)
            f_x_derivative = sp.diff(f_x, x)
            f_x_primitive = sp.integrate(f_x, x)
            f_x_solution = sp.solve(f_x, x)
            # Print the result in a mathematical format
            st.latex(f"Fonction f(x) = {sp.latex(f_x)}")
            st.latex(f"Dérivée f'(x) = {sp.latex(f_x_derivative)}")
            st.latex(f"Primitive \\int f(x) dx = {sp.latex(f_x_primitive)}")
            st.latex(f"Solutions: {sp.latex(f_x_solution)}")
            
            plt_x = np.linspace(-10, 10, 100)
            plt_y = [f_x.subs(x, val) for val in plt_x]
            
            plt.plot(plt_x, plt_y)
            plt.title(f"Graphique de la fonction {f_x}")
            plt.xlabel("x")
            plt.ylabel("f(x)")
            plt.grid()
            st.pyplot(plt)
        except Exception as e:
            st.error(f"La fonction est un peu trop compliquée pour moi. Essaie d'entrer une fonction plus simple. Erreur : {e}")
    
    delete_plot = st.form_submit_button("Supprimer le graphique")
    if delete_plot:
        plt.clf()
        st.pyplot(plt)