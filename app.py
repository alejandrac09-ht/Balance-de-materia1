import streamlit as st

def calcular_azucar(masa_inicial, brix_inicial, brix_final):
    """
    Calcula la cantidad de azúcar necesaria para ajustar los grados Brix.
    """
    # Convertir los grados Brix a porcentaje decimal
    brix_inicial_decimal = brix_inicial / 100.0
    brix_final_decimal = brix_final / 100.0

    # Calcular la masa de sólidos disueltos (azúcar) inicial
    masa_azucar_inicial = masa_inicial * brix_inicial_decimal

    # Calcular la masa total final requerida
    masa_total_final = masa_azucar_inicial / brix_final_decimal

    # Calcular la masa de agua que se debe agregar (en este caso, es azúcar, por lo que la masa de agua es 0)
    # Por lo tanto, la masa de azúcar a agregar es la diferencia entre la masa final y la masa inicial
    azucar_a_agregar = masa_total_final - masa_inicial

    return azucar_a_agregar

# Configuración de la página de Streamlit
st.set_page_config(page_title="Calculadora de Balance de Masa", layout="centered")

# Título de la aplicación
st.title("Calculadora de Balance de Masa")

# Descripción del problema
st.markdown("""
Esta aplicación resuelve un problema de balance de masa para ajustar los grados Brix de una pulpa de fruta.
""")

# Mostrar la imagen del problema
st.image("https://i.ibb.co/6P83jS6/image-10ee94.png", caption="Problema de Balance de Masa", use_column_width=True)

st.header("Parámetros del Problema")

# Entradas del usuario
masa_inicial = st.number_input("Masa inicial de la pulpa (kg)", min_value=0.0, value=50.0, step=0.1)
brix_inicial = st.number_input("Grados Brix iniciales (%)", min_value=0.0, value=7.0, step=0.1)
brix_final = st.number_input("Grados Brix finales deseados (%)", min_value=0.0, value=10.0, step=0.1)

# Botón para calcular
if st.button("Calcular cantidad de azúcar"):
    if brix_final <= brix_inicial:
        st.error("Los grados Brix finales deben ser mayores que los iniciales para agregar azúcar.")
    else:
        # Realizar el cálculo
        azucar_necesaria = calcular_azucar(masa_inicial, brix_inicial, brix_final)
        
        # Mostrar el resultado
        st.success(f"Para ajustar la pulpa de {brix_inicial}% a {brix_final}% Brix, debes agregar **{azucar_necesaria:.2f} kg** de azúcar.")
        st.info("Este cálculo asume que el azúcar agregado es 100% puro.")

# Explicación del proceso
st.markdown("---")
st.markdown("### Explicación del Cálculo")
st.markdown("""
El cálculo se basa en el principio de conservación de la masa. La masa de sólidos disueltos (azúcar) en la pulpa antes y después de la adición de azúcar debe ser igual, pero distribuida en una masa total mayor.

1. **Masa inicial de azúcar:** Se calcula multiplicando la masa inicial de la pulpa por su porcentaje de Brix inicial.
   $M_{azucar\_inicial} = M_{pulpa\_inicial} \times \frac{°Brix_{inicial}}{100}$
   
2. **Masa total final:** La masa de azúcar inicial se mantiene, pero ahora representa un porcentaje menor (los Brix finales) de la nueva masa total.
   $M_{pulpa\_final} = \frac{M_{azucar\_inicial}}{\frac{°Brix_{final}}{100}}$

3. **Azúcar a agregar:** La cantidad de azúcar a agregar es simplemente la diferencia entre la masa total final y la masa inicial de la pulpa.
   $M_{azucar\_agregar} = M_{pulpa\_final} - M_{pulpa\_inicial}$
""")
