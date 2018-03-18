# JRV.pdf --> jrv.csv

## Requisitos

- Conexión a internet 
- [LibreOffice Calc](https://www.libreoffice.org/)
- [pdftk](https://packages.ubuntu.com/xenial/pdftk)
- [Golang](https://golang.org/doc/install) 1.10+
- [JRV.pdf](http://www.tse.go.cr/pdf/nacional2018/JRV.pdf)

## Proceso

### Reducir el tamaño del pdf

Con la ayuda de `pdftk` simplemente se regenera el pdf, que reduce su espacio reduciendo su calidad a un estándar. Note cómo el archivo pasa de 12Mb a 3.8Mb

```bash
$ pdftk JRV.pdf cat 1-end output jrvSmall.pdf
$ ls -l
drwxr-x--- 2 user user 4,0K mar 17 19:45 ./
drwxr-x--- 4 user user 4,0K mar 13 14:22 ../
-rw-rw-r-- 1 user user  12M mar 17 13:17 JRV.pdf
-rw-rw-r-- 1 user user 3,8M mar 17 15:06 jrvSmall.pdf
```

### Convertir el pdf a xlsx

Ingrese a `http://pdftoxls.com/` y suba `jrvSmall.pdf`. Al tener un tamaño reducido, es más sencillo de transmitir. Luego descargue el archivo y sálvelo como jrvWeb.xlsx

### Normalizar el xlsx

Abra el archivo `jrvWeb.xlsx` con LibreOffice. Aparentemente el sitio web deja información vacía en algunas celdas. Esto se puede solucionar editando cualquier celda y salvando el archivo nuevamente. LibreOffice se encarga de eliminar estas celdas basura. Esto ayuda a las reglas de para procesar el archivo más adelante. Salve el archivo como `jrv.xlsx`.

### Convertir el xlsx a csv

Descargue el parser del xlsx y córralo de la siguiente manera:

```bash
$ go run xlsxParser.go > jrv.csv
$
```

Este parser imprime a la salida estándar el archivo, la cuál se redirige a un archivo CSV.
En caso de haber algún error, esta si será impresa en la salida de la consola.

### Profit (¿)