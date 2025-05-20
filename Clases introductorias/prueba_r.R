# generar una grafica simple
# Cargar la libreria ggplot2
library(ggplot2)
# Crear un data frame de ejemplo
data <- data.frame(
  x = c(1, 2, 3, 4, 5),
  y = c(2, 3, 5, 7, 11)
)
# Crear un gráfico de dispersión
ggplot(data, aes(x = x, y = y)) +
  geom_point() +
  labs(title = "Gráfico de dispersión", x = "Eje X", y = "Eje Y") +
  theme_minimal()
