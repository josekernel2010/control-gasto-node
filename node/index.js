// llamando el modulo express para la coneccion
const express = require("express");
const colors = require("colors");
const movimientoRouter = require("./routes/movimiento");
const app = express();

//midleware funcion de express
//va a servir para recibir datos de un formulario
app.use(express.urlencoded({ extended: false }));
app.use(express.json());
app.use("/movimiento", movimientoRouter);

//que escuche en el puerto 3000
app.listen(3000, (err, res) => {
  if (err) {
    console.log("Error en el servidor => ".red + err);
  } else {
    console.log("Servidor corriendo en el puerto 3000".rainbow);
  }
});
