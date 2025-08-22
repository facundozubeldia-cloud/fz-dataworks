import os, sqlite3
import pandas as pd

BASE = r"C:\Github\fz-dataworks\data-analysis\classicmodels-proyect"
SQLITE_DB = os.path.join(BASE, "classic.db")
OUT_CSV   = os.path.join(BASE, "classicmodels_join.csv")

con = sqlite3.connect(SQLITE_DB)

sql = """
SELECT
  o.orderNumber                                    AS factura,
  o.orderDate                                      AS fecha,
  o.shippedDate                                    AS "fecha de entrega",
  od.productCode                                   AS productCode,
  p.productName                                    AS producto,
  p.productLine                                    AS categoria,
  p.buyPrice                                       AS "precio compra",
  od.priceEach                                     AS precio,
  od.quantityOrdered                               AS cantidad,
  o.status                                         AS status,
  c.customerNumber                                 AS customerNumber,
  c.customerName                                   AS cliente,
  c.city                                           AS ciudad,
  c.country                                        AS pais,
  e.employeeNumber                                 AS employeeNumber,
  (e.firstName || ' ' || e.lastName)               AS vendedor
FROM orderdetails od
JOIN orders      o  USING (orderNumber)
JOIN products    p  USING (productCode)
JOIN customers   c  ON o.customerNumber = c.customerNumber
LEFT JOIN employees e ON c.salesRepEmployeeNumber = e.employeeNumber
ORDER BY o.orderNumber, od.productCode;
"""

print("Ejecutando JOIN…")
df = pd.read_sql_query(sql, con)
con.close()

print("Filas:", len(df))
df.to_csv(OUT_CSV, index=False)
print("CSV exportado en:", OUT_CSV)