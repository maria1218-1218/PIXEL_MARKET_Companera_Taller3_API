-- ARCHIVO DIDACTICO: el SQL se explica paso a paso en la guia.
-- Datos ficticios para insertar desde DBeaver en una base vacia.
-- Ejecutar despues de iniciar la API una vez para crear las tablas.
-- Correos de ejemplo, sin informacion de personas reales.
INSERT INTO usuario (nombre, correo, fecha_registro) VALUES
('Valeria Torres', 'valeria.demo@example.com', CURRENT_TIMESTAMP),
('Mateo Rios', 'mateo.demo@example.com', CURRENT_TIMESTAMP),
('Daniela Vega', 'daniela.demo@example.com', CURRENT_TIMESTAMP),
('Sebastian Mora', 'sebastian.demo@example.com', CURRENT_TIMESTAMP),
('Camila Soto', 'camila.demo@example.com', CURRENT_TIMESTAMP);

-- Catalogo inventado. Los titulos no corresponden a licencias reales.
INSERT INTO juego (titulo, desarrollador, plataforma, genero, precio, anio_lanzamiento, descripcion, disponible, fecha_creacion) VALUES
('Nebula Rift', 'Pixel Forge', 'PC', 'RPG', 89000, 2025, 'Aventura espacial cooperativa', 1, CURRENT_TIMESTAMP),
('Circuit Rush', 'Volt Studio', 'Xbox', 'Carreras', 56000, 2024, 'Competencia futurista en pistas neon', 1, CURRENT_TIMESTAMP),
('Frost Kingdom', 'North Byte', 'PC', 'Estrategia', 79000, 2023, 'Construye un reino entre montanas heladas', 1, CURRENT_TIMESTAMP),
('Titan Protocol', 'Argon Games', 'Xbox', 'Accion', 110000, 2025, 'Combate tactico con robots gigantes', 1, CURRENT_TIMESTAMP),
('Echoes of Terra', 'Wild Pixel', 'PC', 'Aventura', 65000, 2022, 'Explora ecosistemas desconocidos', 1, CURRENT_TIMESTAMP),
('Shadow Circuit', 'Neon Works', 'PC', 'Sigilo', 44000, 2024, 'Infiltracion en una metropoli cibernetica', 1, CURRENT_TIMESTAMP),
('Ocean Legends', 'Blue Wave', 'Xbox', 'RPG', 93000, 2021, 'Viaje fantastico bajo el oceano', 1, CURRENT_TIMESTAMP),
('Skyline Architect', 'Urban Lab', 'PC', 'Simulacion', 33000, 2020, 'Disena la ciudad del futuro', 1, CURRENT_TIMESTAMP),
('Iron Arena', 'Steel Dev', 'Xbox', 'Deportes', 48000, 2023, 'Torneo competitivo de robots', 1, CURRENT_TIMESTAMP),
('Moon Garden', 'Lunar Indie', 'PC', 'Indie', 24000, 2025, 'Construye un jardin en la luna', 1, CURRENT_TIMESTAMP);
