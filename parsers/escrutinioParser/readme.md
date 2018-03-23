# JRV.pdf --> jrv.csv

## Requisitos

- [Actas del Escrutinio - Presidenciales](http://www.tse.go.cr/elecciones2018/actas_escrutinio.htm)
- [Golang](https://golang.org/doc/install) 1.10+

## Proceso

### Parsear las actas en un solo CSV

No hay mucho que hacerle, es solo un paso. Es más complicado el setup de go y bajar los archivos y ponerlos en la carpeta correcta. Solo requiere el parser, la carpeta actas y su contenido con nombre estándar.

```bash
$ ls -lh *
-rw-rw-r-- 1 user user    612 mar 17 22:10 escrutinioParser.go
-rw-rw-r-- 1 user user   1,5K mar 17 22:19 readme.md

actas:
total 664
-rw-rw-r-- 1 user user  75K mar 17 20:57 ActaSesion10.xlsx
-rw-rw-r-- 1 user user  82K mar 17 20:57 ActaSesion11.xlsx
-rw-rw-r-- 1 user user  60K mar 17 20:57 ActaSesion12.xlsx
-rw-rw-r-- 1 user user  23K mar 17 20:57 ActaSesion1.xlsx
-rw-rw-r-- 1 user user  32K mar 17 20:57 ActaSesion2.xlsx
-rw-rw-r-- 1 user user  45K mar 17 20:57 ActaSesion3.xlsx
-rw-rw-r-- 1 user user  38K mar 17 20:57 ActaSesion4.xlsx
-rw-rw-r-- 1 user user  52K mar 17 20:57 ActaSesion5.xlsx
-rw-rw-r-- 1 user user  55K mar 17 20:57 ActaSesion6.xlsx
-rw-rw-r-- 1 user user  64K mar 17 20:57 ActaSesion7.xlsx
-rw-rw-r-- 1 user user  56K mar 17 20:57 ActaSesion8.xlsx
-rw-rw-r-- 1 user user  69K mar 17 20:57 ActaSesion9.xlsx
```

Luego simplemente corra el parser y redirija la salida al archivo csv

```bash
$ go run escrutinioParser.go > actas.csv
$ ls -l actas.csv
-rw-rw-r-- 1 user user 368K mar 17 22:12 actas.csv
```

### Profit (¿)