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

    # La ecuación de balance de masa es:
    # (masa_inicial + masa_azucar_a_agregar) * brix_final_decimal = masa_azucar_inicial + masa_azucar_a_agregar
    # Resolviendo para masa_azucar_a_agregar:
    # masa_inicial * brix_final_decimal + masa_azucar_a_agregar * brix_final_decimal = masa_azucar_inicial + masa_azucar_a_agregar
    # masa_azucar_a_agregar * (1 - brix_final_decimal) = masa_inicial * brix_final_decimal - masa_azucar_inicial
    # azucar_a_agregar = (masa_inicial * brix_final_decimal - masa_azucar_inicial) / (1 - brix_final_decimal)
    
    azucar_a_agregar = (masa_inicial * brix_final_decimal - masa_azucar_inicial) / (1 - brix_final_decimal)
    
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
st.image("https://i.ibb.co/L5T1M6B/image-1067ac.png", caption="Problema de Balance de Masa", use_column_width=True)

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
El cálculo se basa en un **balance de masa para un proceso de enriquecimiento**. A diferencia de la dilución, en este caso la masa de sólidos disueltos (azúcar) en la pulpa antes y después de la adición de azúcar cambia.

La ecuación se puede expresar de la siguiente manera:

$$(M_{inicial} + M_{azúcar\_agregado}) \times °Brix_{final} = (M_{inicial} \times °Brix_{inicial}) + M_{azúcar\_agregado}$$

Resolviendo para $M_{azúcar\_agregado}$, obtenemos la fórmula implementada en el código:

$$M_{azúcar\_agregado} = \\frac{(M_{inicial} \times °Brix_{final}) - (M_{inicial} \times °Brix_{inicial})}{1 - °Brix_{final}}$$

**Masa inicial de la pulpa:** 50 kg
**Grados Brix iniciales:** 7%
**Grados Brix finales:** 10%
**Masa de azúcar a agregar:** $$\\frac{(50 \times 0.10) - (50 \times 0.07)}{1 - 0.10} = \\frac{5 - 3.5}{0.9} = \\frac{1.5}{0.9} \\approx 1.67$$ kg

""")

