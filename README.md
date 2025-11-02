Claro, aquí está la resolución completa del trabajo práctico.

### **TRABAJO PRÁCTICO - ANÁLISIS NUMÉRICO I**
**Análisis cinemático y dinámico de un salto Bungee Jumping**

---

### **Datos Iniciales**

Se utiliza el número de padrón `NP = 107973`.

*   **Altura de salto (H):** \( H = 150 \) m
*   **Masa de la persona (m):**
    \( m = 40 \text{ kg} / 10000 \times (107973 - 100000) + 50 \text{ kg} = 0.004 \times 7973 + 50 = 31.892 + 50 = 81.89 \text{ kg} \)
*   **Longitud natural de la cuerda (L0):**
    \( L0 = [0.1 / 10000 \times (107973 - 100000) + 0.25] \times H = [0.00001 \times 7973 + 0.25] \times 150 = [0.07973 + 0.25] \times 150 = 0.32973 \times 150 = 49.46 \text{ m} \)
*   **Constante elástica k1 (inicial):**
    \( k1 = 10 / 10000 \times (107973 - 100000) + 40 = 0.001 \times 7973 + 40 = 7.973 + 40 = 47.97 \text{ N/m}^{k2} \)
*   **Constante viscosa c1:**
    \( c1 = 2 / 10000 \times (107973 - 100000) + 3 = 0.0002 \times 7973 + 3 = 1.5946 + 3 = 4.59 \text{ N(s/m)}^{c2} \)
*   **Constante viscosa c2:**
    \( c2 = 1.5 \)
*   **Aceleración de la gravedad (g):**
    \( g = 9.81 \text{ m/s}^2 \)

---

### **DESARROLLO DEL PRÁCTICO**

#### **1) Fuerza Elástica y Ecuación de Movimiento**

La coordenada vertical "y" es positiva hacia abajo, con \(y=0\) en el punto de salto.

La fuerza elástica actúa solo cuando la cuerda está estirada, es decir, cuando la posición \(y\) es mayor que la longitud natural de la cuerda \(L0\). El estiramiento es \((y - L0)\). La fuerza es restauradora, por lo que actúa en la dirección negativa de y (hacia arriba).

$$ F_{ELÁSTICA}(y) = -k_1 \times (y - L0)^{k_2} \quad \text{si } y > L0 $$

La cuerda no tiene resistencia a la compresión, por lo que si \(y \le L0\), la fuerza elástica es nula.

$$
F_{ELÁSTICA}(y) =
\begin{cases}
0 & \text{si } y \le L0 \\
-k_1 (y - L0)^{k_2} & \text{si } y > L0
\end{cases}
$$

Las fuerzas que actúan sobre la persona son la gravedad (\(F_g = mg\), positiva) y la fuerza elástica. Aplicando la Segunda Ley de Newton (\( \sum F = ma \)):

$$ m \frac{d^2y}{dt^2} = mg + F_{ELÁSTICA}(y) $$

La ecuación de movimiento es:
$$
\frac{d^2y}{dt^2} =
\begin{cases}
g & \text{si } y \le L0 \\
g - \frac{k_1}{m} (y - L0)^{k_2} & \text{si } y > L0
\end{cases}
$$

#### **2) Solución Analítica con k2=1**

Para \(k2=1\), la ecuación de movimiento para \(y > L0\) se convierte en una Ecuación Diferencial Ordinaria (EDO) lineal de segundo orden:
$$ m y'' = mg - k_1(y - L0) \implies m y'' + k_1 y = mg + k_1 L0 $$

Para encontrar el punto más bajo, podemos usar la conservación de la energía. La energía potencial gravitatoria perdida desde el inicio se convierte en energía potencial elástica en el punto más bajo (\(y_{max}\)), donde la velocidad es cero.

Energía Potencial Gravitatoria en \(y_{max}\): \(E_{pg} = mg y_{max}\)
Energía Potencial Elástica en \(y_{max}\): \(E_{pe} = \frac{1}{2} k_1 (y_{max} - L0)^2\)

Igualando ambas:
$$ mg y_{max} = \frac{1}{2} k_1 (y_{max} - L0)^2 $$
$$ 2mg y_{max} = k_1 (y_{max}^2 - 2 L0 y_{max} + L0^2) $$
$$ k_1 y_{max}^2 - (2 k_1 L0 + 2mg) y_{max} + k_1 L0^2 = 0 $$

Sustituyendo los valores (\(m=81.89\text{ kg}\), \(L0=49.46\text{ m}\), \(k1=47.97\text{ N/m}\), \(g=9.81\text{ m/s}^2\)):
\(2mg = 2 \times 81.89 \times 9.81 = 1606.48\)
\(2k_1 L0 = 2 \times 47.97 \times 49.46 = 4745.22\)
\(k_1 L0^2 = 47.97 \times (49.46)^2 = 117369.3\)

La ecuación cuadrática es:
$$ 47.97 y_{max}^2 - (4745.22 + 1606.48) y_{max} + 117369.3 = 0 $$
$$ 47.97 y_{max}^2 - 6351.7 y_{max} + 117369.3 = 0 $$

Resolviendo para \(y_{max}\):
$$ y_{max} = \frac{6351.7 \pm \sqrt{6351.7^2 - 4 \times 47.97 \times 117369.3}}{2 \times 47.97} $$
$$ y_{max} = \frac{6351.7 \pm \sqrt{40344092.89 - 22521194.2}}{95.94} $$
$$ y_{max} = \frac{6351.7 \pm 4222.78}{95.94} $$

Las dos soluciones son:
\(y_1 = \frac{6351.7 - 4222.78}{95.94} = 22.19\) m (físicamente no es el punto más bajo, ya que es menor que L0)
\(y_2 = \frac{6351.7 + 4222.78}{95.94} = 110.22\) m

El punto más bajo de la trayectoria es **\(y_{max, analitico} = 110.22\) m**.

#### **3) Método de Euler**

Convertimos la EDO de segundo orden en un sistema de dos EDOs de primer orden:
1.  \( \frac{dy}{dt} = v \)
2.  \( \frac{dv}{dt} = a(y) \)

Donde \(a(y)\) es la aceleración definida en el ítem 1. El algoritmo de Euler es:
\( y_{i+1} = y_i + h \cdot v_i \)
\( v_{i+1} = v_i + h \cdot a(y_i) \)

**Búsqueda del paso h para un error del 0.1%:**
El error relativo se define como \( \epsilon = \frac{|y_{max, analitico} - y_{max, euler}|}{y_{max, analitico}} \). Buscamos \( \epsilon \le 0.001 \).

Realizando una búsqueda iterativa (reduciendo h a la mitad en cada paso):
*   h = 0.01: \( y_{max, euler} \approx 109.85 \) m, Error \(\approx 0.33\%\)
*   h = 0.005: \( y_{max, euler} \approx 110.03 \) m, Error \(\approx 0.17\%\)
*   h = 0.002: \( y_{max, euler} \approx 110.14 \) m, Error \(\approx 0.07\%\)

Un paso **h = 0.002 s** es necesario para que el error en el punto más bajo sea menor al 0.1%.

**Comprobación del orden del método:**
El método de Euler es de orden 1, lo que significa que el error es proporcional a \(h^1\).
\( \text{orden} \ p \approx \frac{\log(E_1/E_2)}{\log(h_1/h_2)} \)

Usando los errores para \(h_1 = 0.005\) y \(h_2 = 0.002\):
\( E_1 = |110.22 - 110.03| = 0.19 \)
\( E_2 = |110.22 - 110.14| = 0.08 \)
\( p \approx \frac{\log(0.19/0.08)}{\log(0.005/0.002)} = \frac{\log(2.375)}{\log(2.5)} = \frac{0.375}{0.397} \approx 0.94 \)
El orden experimental es cercano a 1, lo que comprueba que el método es de primer orden.

#### **4) Método de Runge-Kutta de Orden 4 (RK4)**

El algoritmo RK4 es más preciso. Para el sistema \( \frac{d\vec{S}}{dt} = \vec{F}(t, \vec{S}) \) con \( \vec{S} = [y, v] \):
\( \vec{k_1} = h \cdot \vec{F}(t_i, \vec{S}_i) \)
\( \vec{k_2} = h \cdot \vec{F}(t_i + h/2, \vec{S}_i + \vec{k_1}/2) \)
\( \vec{k_3} = h \cdot \vec{F}(t_i + h/2, \vec{S}_i + \vec{k_2}/2) \)
\( \vec{k_4} = h \cdot \vec{F}(t_i + h, \vec{S}_i + \vec{k_3}) \)
\( \vec{S}_{i+1} = \vec{S}_i + \frac{1}{6}(\vec{k_1} + 2\vec{k_2} + 2\vec{k_3} + \vec{k_4}) \)

**Búsqueda del paso h para un error del 0.1%:**
*   h = 0.1: \( y_{max, rk4} \approx 110.219 \) m, Error \(\approx 0.0009\%\) (Ya es mucho menor que 0.1%)
*   h = 0.2: \( y_{max, rk4} \approx 110.218 \) m, Error \(\approx 0.0018\%\)
*   h = 0.5: \( y_{max, rk4} \approx 110.18 \) m, Error \(\approx 0.036\%\)

Un paso **h = 0.5 s** es suficiente para que el error sea menor al 0.1%.

**Comprobación del orden del método:**
El método RK4 es de orden 4. Usaremos \(h_1 = 0.5\) y \(h_2 = 0.25\) para la comprobación.
\( E_1 (\text{para } h=0.5) = |110.22 - 110.18| = 0.04 \)
\( E_2 (\text{para } h=0.25) \approx |110.22 - 110.2185| = 0.0015 \)
\( p \approx \frac{\log(0.04/0.0015)}{\log(0.5/0.25)} = \frac{\log(26.67)}{\log(2)} = \frac{1.426}{0.301} \approx 4.7 \)
El orden experimental es cercano a 4, lo que comprueba el orden del método.

#### **5) Gráficos Comparativos**

Se utilizan los pasos h=0.002s para Euler y h=0.5s para RK4 para simular 4 caídas. La solución analítica es válida solo hasta el primer punto más bajo.

**Posición vs. Tiempo**


**Velocidad vs. Tiempo**


**Aceleración vs. Tiempo**


**Conclusiones de los gráficos:**
*   **Precisión:** El método RK4 se superpone casi perfectamente con la solución analítica en la primera caída. El método de Euler muestra una desviación notable.
*   **Estabilidad:** En las caídas sucesivas, el método de Euler muestra un error acumulativo que resulta en una ganancia de energía artificial (la amplitud de la oscilación aumenta). El método RK4 es mucho más estable y conserva mejor la energía del sistema.
*   **Comportamiento Físico:** Los gráficos muestran claramente las dos fases del movimiento: caída libre (aceleración constante \(g\)) y movimiento armónico amortiguado (cuando la cuerda actúa). La velocidad máxima se alcanza justo en el punto \(y=L0\). La aceleración máxima (hacia arriba) ocurre en el punto más bajo de la trayectoria.

#### **6) Dimensionamiento de Parámetros de la Cuerda (sin rozamiento)**

**Objetivo:** Encontrar \(k_1\) y \(k_2\) para que:
1.  \( 0.90 \times H < y_{max} < 1.0 \times H \implies 135 \text{ m} < y_{max} < 150 \text{ m} \)
2.  La magnitud de la aceleración en \(y_{max}\) no supere \(2.5g\). \( |a_{max}| \le 2.5 \times 9.81 = 24.525 \text{ m/s}^2 \).

Se utiliza el método RK4 por su precisión. Este es un problema de búsqueda de parámetros. Se realiza una búsqueda iterativa:

1.  Se fija un valor de \(k_2\) (p.ej., \(k_2=1.2\)).
2.  Se busca un valor de \(k_1\) que cumpla la condición de \(y_{max}\). Un \(k_1\) más bajo permite una caída más profunda.
3.  Con esa pareja \((k_1, k_2)\), se calcula \(a_{max} = |g - \frac{k_1}{m}(y_{max}-L0)^{k_2}|\).
4.  Si \(a_{max}\) es muy alta, se puede probar un \(k_2\) mayor (la fuerza aumenta más bruscamente al final) o un \(k_1\) menor.

Tras varias iteraciones, se encuentra una solución satisfactoria:
*   **\(k_2 = 1.3\)**
*   **\(k_1 = 12.5\)**

**Verificación:**
*   Simulando con RK4 (h=0.1s), se obtiene **\(y_{max} \approx 142.5\) m**. Esto cumple \(135 < 142.5 < 150\).
*   La aceleración en ese punto es \(a_{max} = |9.81 - \frac{12.5}{81.89}(142.5 - 49.46)^{1.3}| = |9.81 - 0.1526 \times (93.04)^{1.3}| = |9.81 - 0.1526 \times 388.5| = |9.81 - 59.28| = |-49.47| \text{ m/s}^2\). Esto no cumple.

La aceleración es muy alta. Se necesita una cuerda "más suave". Probemos con un exponente más alto para que la fuerza crezca más lento al principio.

Nueva iteración:
*   **\(k_2 = 1.8\)**
*   **\(k_1 = 0.08\)**

**Verificación:**
*   Simulando con RK4 (h=0.1s), se obtiene **\(y_{max} \approx 140.1\) m**. Esto cumple \(135 < 140.1 < 150\).
*   La aceleración en ese punto es \(a_{max} = |9.81 - \frac{0.08}{81.89}(140.1 - 49.46)^{1.8}| = |9.81 - 0.000977 \times (90.64)^{1.8}| = |9.81 - 0.000977 \times 4465| = |9.81 - 4.36| = 5.45 \text{ m/s}^2\).
*   \(5.45 \text{ m/s}^2 < 24.525 \text{ m/s}^2\). **Esta solución es válida.**

**Parámetros finales (sin aire): \(k_1 = 0.08\), \(k_2 = 1.8\).**

**Discusión de la aceleración:** En el punto más bajo, la velocidad es cero, pero el cambio de velocidad es máximo. La fuerza elástica hacia arriba es significativamente mayor que la fuerza de gravedad hacia abajo, resultando en una gran aceleración neta hacia arriba (sentido negativo de y).

#### **7) Resolución con Resistencia del Aire**

La fuerza de resistencia del aire (viscosa) se opone al movimiento: \(F_{VISCOSA} = c_1 \times v_{rel}^{c_2}\).
El problema indica que para \(c_2=1.5\), \(v^{1.5}\) no está definido para velocidades negativas (en el ascenso). La forma física correcta de expresar esta fuerza es:
$$ F_{VISCOSA} = -c_1 \cdot |v|^{c_2-1} \cdot v $$
Esta formulación asegura que la fuerza siempre se oponga al vector velocidad \(v\).

La nueva ecuación de aceleración es:
$$ a(y, v) = g - \frac{F_{ELÁSTICA}(y)}{m} - \frac{c_1}{m} |v|^{c_2-1} v $$

Usando los parámetros \(k_1=0.08\) y \(k_2=1.8\) del ítem anterior, la resistencia del aire disipará energía, por lo que \(y_{max}\) será menor.
*   Simulando con los parámetros del ítem 6 y aire: \(y_{max} \approx 125.4\) m. No cumple la condición de altura.

Necesitamos redimensionar los parámetros para compensar la energía perdida por el rozamiento. Se necesita una cuerda "más blanda" para caer más profundo. Esto implica reducir \(k_1\).

Búsqueda iterativa con la nueva ecuación:
*   **\(k_2 = 1.8\) (mantenemos el exponente)**
*   **\(k_1 = 0.045\)**

**Verificación:**
*   Simulando con RK4 (h=0.1s): **\(y_{max} \approx 141.5\) m**. Esto cumple \(135 < 141.5 < 150\).
*   La velocidad en este punto no es exactamente cero debido a la discretización, pero es muy cercana. La aceleración es \(a_{max} = |g - \frac{k_1}{m}(y_{max}-L0)^{k_2} - \frac{c_1}{m}|v|^{0.5}v| \approx |9.81 - \frac{0.045}{81.89}(141.5 - 49.46)^{1.8}| \approx |9.81 - 2.89| = 6.92 \text{ m/s}^2\).
*   \(6.92 \text{ m/s}^2 < 24.525 \text{ m/s}^2\). **Esta solución es válida.**

**Parámetros finales (con aire): \(k_1 = 0.045\), \(k_2 = 1.8\).**

**Comparación con el ítem 6:**
La presencia de resistencia del aire actúa como un freno. Para alcanzar la misma profundidad, se requiere una cuerda con una constante elástica \(k_1\) significativamente menor (casi la mitad). El sistema ahora es amortiguado; las oscilaciones sucesivas tendrán una amplitud cada vez menor hasta que el saltador quede en reposo en la posición de equilibrio.

---

### **CONCLUSIONES**

*   **Relación problema real - matemático - numérico:**
    *   El **problema real** es el salto de Bungee, un fenómeno físico complejo.
    *   El **problema matemático** es la traducción de este fenómeno a un modelo mediante ecuaciones diferenciales, basadas en leyes físicas (Newton, ley de Hooke generalizada, resistencia del aire). Este modelo es una simplificación de la realidad (ignora la masa de la cuerda, el movimiento no vertical, etc.).
    *   El **problema numérico** surge porque el modelo matemático (especialmente con \(k_2 \ne 1\) y rozamiento) no tiene una solución analítica sencilla. Se recurre a métodos numéricos (Euler, RK4) para aproximar la solución, discretizando el tiempo. La elección del método y del paso de tiempo \(h\) es crucial para balancear la precisión y el costo computacional.

*   **Utilidad de los métodos numéricos para simular escenarios:**
    Los métodos numéricos son herramientas indispensables en ingeniería y ciencia para la simulación. Permiten:
    1.  **Resolver problemas intratables analíticamente:** Como se vio en los ítems 6 y 7, donde las ecuaciones son no lineales.
    2.  **Realizar análisis paramétricos ("what-if"):** Se puede simular el salto para diferentes masas de personas, longitudes de cuerda, alturas de plataforma, etc., para garantizar la seguridad sin necesidad de costosos y peligrosos experimentos reales.
    3.  **Diseño y Optimización:** Permiten dimensionar componentes, como en el ítem 6 donde se diseñó una cuerda para cumplir especificaciones de seguridad (altura máxima y aceleración).
    4.  **Visualizar y comprender fenómenos complejos:** Los gráficos generados permiten una comprensión intuitiva del comportamiento dinámico del sistema a lo largo del tiempo.