package main

import (
	"fmt"
	"log"
	"os"
	"strings"

	"github.com/tealeg/xlsx"
)

func main() {

	excelFileName := "./Indicadores-cantonales_Censos-2000-y-2011_graficos_crudos.xlsx"
	xlFile, err := xlsx.OpenFile(excelFileName)
	if err != nil {
		log.Println(err)
		os.Exit(1)
	}
	parsePiramide(xlFile)
	fmt.Printf("%s", "\n\n### FILE DIVISION ###\n\n")
	parseTIC(xlFile)
	fmt.Printf("%s", "\n\n### FILE DIVISION ###\n\n")
	parseEducacion(xlFile)
	fmt.Printf("%s", "\n\n### FILE DIVISION ###\n\n")
	parsePEA(xlFile)
	fmt.Printf("%s", "\n\n### FILE DIVISION ###\n\n")
	parseOcupado(xlFile)
	fmt.Printf("%s", "\n\n### FILE DIVISION ###\n\n")
	parseAseguramiento(xlFile)
	fmt.Printf("%s", "\n\n### FILE DIVISION ###\n\n")
	parseComparativo(xlFile)
}

func parsePiramide(file *xlsx.File) {
	// <canton>,<genero>,<rango1>,<rango2>,...
	//162x19: 5-167,1-19
	sheet := file.Sheets[0]
	for i := 5; i < 167; i += 2 {
		strMujeres := ","
		strHombres := ","
		for j := 1; j < 20; j++ {
			//log.Println(i, j, len(sheet.Rows), sheet.Rows[j].Cells)
			n := sheet.Rows[j].Cells[i].String()
			m := strings.Replace(sheet.Rows[j].Cells[i+1].String(), "-", "", 1)
			if j != 19 {
				strMujeres += fmt.Sprintf("%s,", n)
				strHombres += fmt.Sprintf("%s,", m)
			} else {
				strMujeres += fmt.Sprintf("%s", n)
				strHombres += fmt.Sprintf("%s", m)
			}
		}
		canton := sheet.Rows[0].Cells[i].String()
		fmt.Println(canton + strMujeres)
		fmt.Println(canton + strHombres)
	}
}

func parseTIC(file *xlsx.File) {
	// <canton>,<porcentaje|recuento>,<agua>,<sanitario>,<electricidad>,<internet>,<computadora>,<telResidencial>,<telCelular>
	//15-895,0-3
	sheet := file.Sheets[1]
	for i := 14; i < 896; i += 11 {
		strPorc := ""
		strRecu := ""
		for j := 0; j < 8; j++ {
			if j == 3 {
				continue
			}
			n := sheet.Rows[i+j].Cells[2].String()
			m := sheet.Rows[i+j].Cells[3].String()
			if j != 7 {
				strPorc += fmt.Sprintf("%s,", n)
				strRecu += fmt.Sprintf("%s,", m)
			} else {
				strPorc += fmt.Sprintf("%s", n)
				strRecu += fmt.Sprintf("%s", m)
			}

		}
		canton := sheet.Rows[i].Cells[0].String()
		fmt.Println(canton + ",porcentaje," + strPorc)
		fmt.Println(canton + ",recuento," + strRecu)
	}
}

func parseEducacion(file *xlsx.File) {
	// <canton>,<Ningún año>,<Primaria incompleta>,<Primaria completa>,<Secundaria incompleta>,<Secundaria completa>
	//81x5: 1-81,1-8
	sheet := file.Sheets[2]
	for i := 1; i < 82; i++ {
		linea := ""
		for j := 2; j < 8; j++ {
			n := sheet.Rows[j].Cells[i].String()
			if j != 7 {
				linea += fmt.Sprintf("%s,", n)
			} else {
				linea += fmt.Sprintf("%s", n)
			}
		}
		fmt.Println(linea)
	}
}

func parsePEA(file *xlsx.File) {
	//<canton>,<Pensionado>,<Rentista>,<Estudia>,<Oficios domésticos>,<Otros>
	//81x5: 1-81,1-8
	sheet := file.Sheets[3]
	for i := 1; i < 82; i++ {
		linea := ""
		for j := 2; j < 8; j++ {
			n := sheet.Rows[j].Cells[i].String()
			if j != 7 {
				linea += fmt.Sprintf("%s,", n)
			} else {
				linea += fmt.Sprintf("%s", n)
			}
		}
		fmt.Println(linea)
	}
}

func parseOcupado(file *xlsx.File) {
	//<canton>,<Sector Primario,<Sector Secundario,<Sector Terciario>
	//81x4: 1-81,1-5
	sheet := file.Sheets[4]
	for i := 1; i < 82; i++ {
		linea := ""
		for j := 2; j < 6; j++ {
			n := sheet.Rows[j].Cells[i].String()
			if j != 5 {
				linea += fmt.Sprintf("%s,", n)
			} else {
				linea += fmt.Sprintf("%s", n)
			}
		}
		fmt.Println(linea)
	}
}

func parseAseguramiento(file *xlsx.File) {
	// <canton>,<porcentaje|recuento>,<agua>,<sanitario>,<electricidad>,<internet>,<computadora>,<telResidencial>,<telCelular>
	//16-656,0-3
	sheet := file.Sheets[5]
	for i := 16; i < 657; i += 8 {
		linea := ""
		for j := 0; j < 4; j++ {
			n := sheet.Rows[i+j].Cells[2].String()
			if j != 3 {
				linea += fmt.Sprintf("%s,", n)
			} else {
				linea += fmt.Sprintf("%s", n)
			}
		}
		canton := sheet.Rows[i].Cells[0].String()
		fmt.Println(canton + "," + linea)
	}
}

func parseComparativo(file *xlsx.File) {
	//<canton>,<secundariaCompleta|viviendasConInternet|insuficienciaDeRecursos>,<valorCanton>,<valorVecinos>
	sheet := file.Sheets[6]
	for i := 4; i < 85; i++ {
		strSecund := ""
		strIntern := ""
		strRecurs := ""
		n1 := sheet.Rows[i].Cells[1].String()
		n2 := sheet.Rows[i].Cells[2].String()
		m1 := sheet.Rows[i].Cells[4].String()
		m2 := sheet.Rows[i].Cells[5].String()
		o1 := sheet.Rows[i].Cells[7].String()
		o2 := sheet.Rows[i].Cells[8].String()

		strSecund += fmt.Sprintf("%s,%s", n1, n2)
		strIntern += fmt.Sprintf("%s,%s", m1, m2)
		strRecurs += fmt.Sprintf("%s,%s", o1, o2)

		canton := sheet.Rows[i].Cells[0].String()
		fmt.Println(canton + "," + strSecund)
		fmt.Println(canton + "," + strIntern)
		fmt.Println(canton + "," + strRecurs)
	}
}

func ignoreRange(k int) bool {
	igRange := []int{0, 2, 3, 10, 11, 12, 17, 18, 19, 20, 22, 26, 34, 35, 36, 39, 43, 44, 45}
	return intInSlice(k, igRange)
}

func intInSlice(a int, list []int) bool {
	for _, b := range list {
		if b == a {
			return true
		}
	}
	return false
}
