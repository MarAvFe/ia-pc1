# JRV.pdf --> jrv.csv

## Requisitos

- [Indicadores Cantonales de los censos del 2000 y 2011](https://www.estadonacion.or.cr/files/biblioteca_virtual/otras_publicaciones/Indicadores-cantonales_Censos-2000-y-2011.xlsx)
- [Golang](https://golang.org/doc/install) 1.10+
- [LibreOffice Calc](https://www.libreoffice.org/)

## Proceso

### Eliminar las páginas intratables

Muchos de los datos de este documento no pueden ser tratados automáticamente (de manera sencilla) ya que son imágenes. Y otra información como créditos o títulos nos agregan ruido al procesamiento. Por esto debemos crear una copia del documento y eliminar todas las páginas excepto las que tengan el nombre de cada una de las provincias de Costa Rica.

### Parsear el archivo

Verifique que el nombre del archivo y su ubicación están actualizados en el código fuente del parser. Luego ejecútelo de la siguiente manera:

```bash
$ go run indicadoresParser.go > indicadores.csv
$
```

### Profit (¿)