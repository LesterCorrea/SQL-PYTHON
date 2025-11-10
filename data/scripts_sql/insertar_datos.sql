INSERT INTO DOCENTES VALUES (1, 'Dr. Ramirez Lopez', 'Programacion', 'ramirez@uni.edu');
INSERT INTO DOCENTES VALUES (2, 'Ing. Valverde Soto', 'Bases de Datos', 'valverde@uni.edu');
INSERT INTO DOCENTES VALUES (3, 'Lic. Huaman Ortega', 'Desarrollo Web', 'huaman@uni.edu');
INSERT INTO DOCENTES VALUES (4, 'Mg. Paredes Quispe', 'Redes y Seguridad', 'paredes@uni.edu');

INSERT INTO AULAS VALUES (1, 'Lab-101', 25);
INSERT INTO AULAS VALUES (2, 'Aula-202', 40);
INSERT INTO AULAS VALUES (3, 'Lab-303', 30);
INSERT INTO AULAS VALUES (4, 'Aula-404', 20);

INSERT INTO CURSOS VALUES (1, 'Programacion en Python', 60, 1, 1);
INSERT INTO CURSOS VALUES (2, 'Bases de Datos Oracle', 50, 2, 2);
INSERT INTO CURSOS VALUES (3, 'Desarrollo Web con HTML/CSS', 45, 3, 3);
INSERT INTO CURSOS VALUES (4, 'Seguridad Informatica', 40, 4, 4);
INSERT INTO CURSOS VALUES (5, 'Inteligencia Artificial', 70, 1, 1);

INSERT INTO ALUMNOS VALUES (1, 'Lester Correa', 'lester@gmail.com', TO_DATE('2002-04-12', 'YYYY-MM-DD'), 23);
INSERT INTO ALUMNOS VALUES (2, 'Abigail Torres', 'abigail@gmail.com', TO_DATE('2003-02-05', 'YYYY-MM-DD'), 22);
INSERT INTO ALUMNOS VALUES (3, 'Eloise Rivera', 'eloise@gmail.com', TO_DATE('2006-09-21', 'YYYY-MM-DD'), 19);
INSERT INTO ALUMNOS VALUES (4, 'Carlos Mendoza', 'carlosm@gmail.com', TO_DATE('2001-06-18', 'YYYY-MM-DD'), 24);
INSERT INTO ALUMNOS VALUES (5, 'Lucia Fernandez', 'luciaf@gmail.com', TO_DATE('2004-12-09', 'YYYY-MM-DD'), 21);

INSERT INTO MATRICULAS VALUES (1, 1, 1, SYSDATE, 'Activa');
INSERT INTO MATRICULAS VALUES (2, 2, 2, SYSDATE, 'Activa');
INSERT INTO MATRICULAS VALUES (3, 3, 3, SYSDATE, 'Pendiente');
INSERT INTO MATRICULAS VALUES (4, 4, 4, SYSDATE, 'Activa');
INSERT INTO MATRICULAS VALUES (5, 5, 5, SYSDATE, 'Finalizada');
INSERT INTO MATRICULAS VALUES (6, 1, 3, SYSDATE, 'Activa');
INSERT INTO MATRICULAS VALUES (7, 2, 1, SYSDATE, 'Activa');

COMMIT;