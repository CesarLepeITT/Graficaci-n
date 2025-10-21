# Métodos de transformación

def dibujar(ax, figura, color, etiqueta):
    # figura: array 3xN con puntos [x, y, 1]
    x = figura[0, :]
    y = figura[1, :]
    
    # Cerramos la figura para que el polígono sea completo
    x = np.append(x, x[0])
    y = np.append(y, y[0])
    
    ax.plot(x, y, color=color, label=etiqueta)
    ax.legend()

def transformar(figura, matriz_transformacion):
    return matriz_transformacion @ figura

def traslacion(tx, ty):
    return np.array([[1, 0, tx],
                     [0, 1, ty],
                     [0, 0, 1]])
def escalamiento(sx, sy):
    return np.array([[sx, 0, 0],
                     [0, sy, 0],
                     [0, 0, 1]])

def rotacion(angulo):
    rad = np.radians(angulo)
    return np.array([[np.cos(rad), -np.sin(rad), 0],
                     [np.sin(rad), np.cos(rad), 0],
                     [0, 0, 1]])

def rotacion_punto(angulo, px, py):
    return traslacion(px, py) @ rotacion(angulo) @ traslacion(-px, -py)

def reflejo_x():
    return np.array([[1, 0, 0],
                     [0, -1, 0],
                     [0, 0, 1]])

def reflejo_y():
    return np.array([[-1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 1]])


# Figura (cuadrado)

figura = np.array([
    [0, 0, 1, 1],  # x
    [0, 1, 1, 0],  # y
    [1, 1, 1, 1]   # homogénea
])

# Plot

fig, ax = plt.subplots(figsize = (6,6))
#ax.set_aspect('equals')
ax.grid(True, linestyle = '--', alpha = 0.5)
ax.set_xlim(-5,10)
ax.set_ylim(-5,10)

# Dibujar fig original
dibujar(ax, figura, 'black', 'Original')

# Aplicar Transformaciones 
fig_tras = transformar(figura, traslacion(4,1))
dibujar(ax, fig_tras, 'blue', 'Traslación')

fig_esc = transformar(figura, escalamiento(2, 0.5))
dibujar(ax, fig_esc, 'green', 'Escalamiento')

fig_rot = transformar(figura, rotacion(45))
dibujar(ax, fig_rot, 'red', 'Rotación de Origen')

fig_ref_x = transformar(figura, reflejo_x())
dibujar(ax, fig_ref_x, 'purple', 'Reflejo X')

fig_ref_y = transformar(figura, reflejo_y())
dibujar(ax, fig_ref_y, 'orange', 'Reflejo Y')

fig_rot_punto = transformar(figura, rotacion_punto(45, 4,1))
dibujar(ax, fig_rot_punto, 'cyan', 'Rotacion Punto')

