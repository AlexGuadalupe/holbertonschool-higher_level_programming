-- Un script que lista el número de registros con el mismo score en la tabla second_table de la base de datos hbtn_0c_0 en tu servidor MySQL.
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;