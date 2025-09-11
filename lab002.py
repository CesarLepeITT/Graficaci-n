from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import colorsys

# Cargar imagen y asegurar RGB
img = Image.open("/workspaces/Graficaci-n/img/frieren.jpg").convert("RGB")

# --- Conversión a HSV (Pillow lo soporta directamente) ---
img_hsv = img.convert("HSV")

# --- Conversión a HSL usando colorsys ---
def rgb_to_hsl(img):
    arr = np.array(img) / 255.0
    hsl_arr = np.zeros_like(arr)
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            r, g, b = arr[i, j]
            h, l, s = colorsys.rgb_to_hls(r, g, b)  # Ojo: colorsys usa HLS
            hsl_arr[i, j] = [h, s, l]               # Reordenamos a HSL
    return Image.fromarray((hsl_arr * 255).astype("uint8"))

img_hsl = rgb_to_hsl(img)

# --- Conversión a CMY ---
img_array = np.array(img) / 255.0
cmy_array = 1 - img_array   # C = 1-R, M = 1-G, Y = 1-B
img_cmy = Image.fromarray((cmy_array * 255).astype("uint8"))

# --- Mostrar resultados ---
fig, axs = plt.subplots(1, 4, figsize=(15, 5))

axs[0].imshow(img)
axs[0].set_title("RGB")
axs[0].axis("off")

axs[1].imshow(img_hsv)
axs[1].set_title("HSV")
axs[1].axis("off")

axs[2].imshow(img_hsl)
axs[2].set_title("HSL")
axs[2].axis("off")

axs[3].imshow(img_cmy)
axs[3].set_title("CMY")
axs[3].axis("off")

plt.show()
