//creando constante para la coneccion con require
const mysql = require("mysql2");
const colors = require("colors");
require("dotenv").config();
//creando la configuracion de la coneccion
const conexion = mysql.createConnection({
  host: process.env.HOST,
  user: process.env.USER,
  password: process.env.PASSWORD,
  database: process.env.DATABASE,
});

// función con condiciones para la coneccion
conexion.connect((err, connect) => {
  if (err) {
    console.log("Ha ocurrido un error en la base de datos => ".red + err);
  } else {
    console.log("Conexion correcta a la base de datos".yellow);
    return connect;
  }
});

//exportando la coneccion
module.exports = conexion;
