package main

import (
	"strings"
	"os"
	"fmt"
	"log"
    "github.com/tealeg/xlsx"
)

func main() {
    excelFileName := "./jrv.xlsx"
    xlFile, err := xlsx.OpenFile(excelFileName)
    if err != nil {
		log.Println(err)
		os.Exit(1)
	}
	
	province := ""
	canton := ""
	district := ""
	town := ""
	junta := 0
	electors := 0

	cnt := 0
	national := true

    for _, sheet := range xlFile.Sheets {
        for i, row := range sheet.Rows {
			if len(sheet.Rows) == i { // Fin de la página
				break
			}
			if len(row.Cells) == 0{ // Fila vacía
				continue
			}
			if strings.Contains(row.Cells[0].String(), "TOTAL") { // Fila irrelevante
				if strings.Contains(row.Cells[0].String(), "TOTAL DE LA REP") { // Fin de las juntas nacionales
					national = false
				}
				continue
			}
			if (len(row.Cells) == 2) || (len(row.Cells) == 3) { // Fila con un distrito o cantón
				if row.Cells[0].String() == "" {
					if row.Cells[1].String() != "" {
						district = row.Cells[1].String()
					}else{
						district = row.Cells[2].String()
					}
				}else{
					if row.Cells[1].String() != "" {
						province  = row.Cells[0].String()
						canton  = row.Cells[1].String() 
					}else{
						province  = row.Cells[0].String()
						canton  = row.Cells[2].String() 
					}
				}
				continue
			}
			if len(row.Cells) == 1 { // Fila con un barrio
				town = row.Cells[0].String()
				continue
			}


			f, s := getPositions(row)

			// Lee el número de junta
			junta, err = row.Cells[f].Int()
			if err != nil {
				log.Println("junt:",err)
			}
			// Lee el número de electores
			electors, err = row.Cells[s].Int()
			if err != nil {
				log.Println("vots:",err)
			}
			
			// DEBUG: Imprime los valores para detectar errores
			if (province == "") ||
				(canton == "") ||
				(district == "") ||
				(town == "") ||
				(junta == -1) ||
				(electors == -1) {
				log.Println("Junta",cnt,"atención:",row)
			}

			// Las juntas internacionales no tienen distrito
			if national {
				fmt.Printf("%s,%s,%s,%s,%d,%d\n",province,canton,district,town,junta,electors)
			}else{
				fmt.Printf("%s,%s,%s,%s,%d,%d\n",province,canton,"",town,junta,electors)
			}
			cnt++
        }
	}
}

// Las filas con números de junta y votantes, tienen sus valores 
// en columnas variables. La 2da o 3ra o 1ra o 4ta. Esta función
// determina estos índices.
func getPositions(row *xlsx.Row) (int,int) {
	f := -1
	s := -1
	for i, cell := range row.Cells {
		text := cell.String()
		if text == ""{
			continue
		}else{
			if f == -1{
				f = i
				continue
			}else{
				s = i
				continue
			}
		}		
	}
	return f, s
}