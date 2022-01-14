// creando con express una ruta para el controlador movimiento
const express = require("express");
const router = express.Router();
const movimientoController = require("../controllers/movimiento");

// para mostrar
router.get("/todos", movimientoController.todos);
router.get("/buscar:id", movimientoController.buscar);
// para ingresar
router.post("/registro", movimientoController.registro);
router.post("/modificar:id", movimientoController.modificar);
router.post("/eliminar:id", movimientoController.eliminar);

// exportamos el router
module.exports = router;
