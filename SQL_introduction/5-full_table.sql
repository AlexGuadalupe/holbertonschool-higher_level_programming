-- Un script que imprime la descripción de la tabla first_table de la base de datos hbtn_0c_0 en tu servidor MySQL.
SELECT 
    COLUMN_NAME AS 'Column Name',
    DATA_TYPE AS 'Data Type',
    IS_NULLABLE AS 'Is Nullable',
    COLUMN_DEFAULT AS 'Default Value'
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_SCHEMA = 'hbtn_0c_0' AND
    TABLE_NAME = 'first_table';