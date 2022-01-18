//importamos la conexion
const conexion = require("../conexion");

/* -----------------------------------
::: exportamos todas las funciones :::
--------------------------------------*/

// consula todos los movimientos de la base de datos
const todos = (req, res) => {
  const sql = `SELECT * FROM movimiento`;
  conexion.query(sql, (err, result) => {
    if (err) {
      res.send("Error en la consulta " + err);
    } else {
      res.send(result);
    }
  });
};

//buscamos un movimiento por id
const buscar = (req, res) => {
  // con esto accedemos hacia un parametro
  const id = req.params.id;
  /*con el signo '?'en la consulta se sustituye por el valor de la
    variable y en coneccion.query agregamos [id] para que se ejecute
    y así evitar errores o inyecciones sql */
  const sql = `SELECT * FROM movimiento WHERE id = ?`;
  conexion.query(sql, [id], (err, result) => {
    if (err) {
      res.send("Error en la consulta " + err);
    } else {
      res.send(result);
    }
  });
};

// registro de movimientos
// ::: problem con la palabra coneccion cuando era conexion :v :::
const registro = (req, res) => {
  const sql = `INSERT INTO movimiento SET ?`;
  conexion.query(sql, req.body, (err) => {
    if (err) {
      res.send("Error en el registro " + err);
    } else {
      res.send(":: Registro exitoso ::".green);
    }
  });
};

// modificamos por id un movimiento
const modificar = (req, res) => {
  const id = req.params.id;
  // para elegir que campos se van a modificar
  const campo = req.body.campo;
  const nuevo_valor = req.body.nuevo_valor;
  const sql = `UPDATE movimiento SET ${campo}='${nuevo_valor}' WHERE id = ${id} `;
  conexion.query(sql, (err) => {
    if (err) {
      res.send("Error en la modificacion " + err);
    } else {
      res.send(":: Modificacion exitosa ::".green);
    }
  });
};

// eliminamos un movimiento por id
const eliminar = (req, res) => {
  const id = req.params.id;
  /*
   :: Importante: que en la sentencia se utilice el signo '?' y no ${id} ::
   :: por las inyecciones sql :::::::::::::::::::::::::::::::::::::::::::::
  */
  const sql = `DELETE FROM movimiento WHERE id = ?`;
  conexion.query(sql, [id], (err) => {
    if (err) {
      res.send("Error en la eliminacion " + err);
    } else {
      res.send(":: Se ha eliminado correctamente ::".green);
    }
  });
};

// exportamos los metodos
module.exports = { todos, registro, modificar, buscar, eliminar };
