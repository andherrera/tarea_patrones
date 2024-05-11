[TOCM]

[TOC]

# Tarea N1 - Problemas de patrones
Arquitectura de Software Grupo 3 (Python)

## 1. Sistema de gestión de tareas
**Contexto:**
Imagina un sistema de gestión de tareas en el que los usuarios pueden crear, editar, eliminar y completar tareas. Cada acción realizada por el usuario corresponde a una acción que debe ser ejecutado. Además, es importante mantener un registro de todas las acciones realizadas para permitir la reversión de las mismas si es necesario.

**Aplicación del Patrón: **
En este escenario, el patrón será aplicado para encapsular cada una de las acciones que el usuario puede realizar sobre una tarea.

El patrón que seleccione debe tener los siguientes beneficios:
- Desacopla el invocador de los objetos que realizan las acciones.
- Permite la extensión de nuevas operaciones sin modificar el código existente.
- Facilita el registro de acciones para realizar operaciones de reversión.

## 2. Construcción de una orden personalizada de pizza
Imagina que estás trabajando en una aplicación de pedidos de pizza en línea y necesitas implementar un sistema de construcción de órdenes personalizadas. Los clientes deben poder crear pizzas personalizadas con ingredientes específicos, tamaños de porción y opciones de cobertura.

Requerimientos del sistema:
1. Los clientes deben poder crear una pizza personalizada eligiendo entre diferentes tamaños de porción (pequeño, mediano, grande) y opciones de masa (delgada, gruesa, integral).
2. Los ingredientes disponibles para la pizza incluyen queso, pepperoni, jamón, champiñones, pimientos, cebolla, aceitunas y piña.
3. Los clientes pueden seleccionar múltiples ingredientes para agregar a su pizza. Pueden elegir la cantidad de cada ingrediente.
4. Las pizzas pueden tener una cobertura adicional en forma de queso extra en el borde de la masa.
5. Los clientes deben poder calcular el costo total de su pizza en función de las selecciones realizadas, incluyendo el tamaño de la porción, los ingredientes y la cobertura adicional.
6. Una vez que los clientes hayan construido su pizza personalizada, deben poder revisarla y realizar el pedido.

## 3. La creación de un sistema de generación de informes personalizados con diferentes formatos de salida
**Problema:** Sistema de Generación de Informes Personalizados

L@ llamaron para desarrollar un software empresarial que necesita generar informes a partir de una base de datos. Los informes pueden tener diferentes formatos de salida, como PDF, Excel y HTML. Además, cada tipo de informe puede requerir pasos específicos de generación, como consultar la base de datos, aplicar cálculos y formatear el resultado final. Dado que los informes y los formatos de salida pueden ser diversos, es importante tener una solución que maneje esta complejidad y permita la generación de informes de manera flexible y extensible.

El patrón de diseño que escoja debe permitir manejar la variación en la generación de informes y formatos de salida, al tiempo que garantiza que los pasos generales sean consistentes para todos los tipos de informes. Esto facilita la extensión del sistema a medida que se agregan nuevos tipos de informes o formatos de salida en el futuro.

## 4. Problema: Integración de biblioteca incompatible
La integración de una biblioteca de terceros con una interfaz incompatible en tu sistema existente.

L@ llamaron para desarrollar una aplicación que procesa datos geográficos y utiliza una biblioteca de terceros para mostrar mapas en formato KML (Keyhole Markup Language). Sin embargo, tu sistema ya está diseñado para trabajar con datos en formato GeoJSON. La biblioteca de terceros solo admite KML, pero necesitas que tu aplicación funcione con datos GeoJSON sin modificar toda la lógica existente.

Tu solución debe permitir integrar componentes incompatibles al proporcionar una interfaz uniforme y una capa de adaptación entre ellos.