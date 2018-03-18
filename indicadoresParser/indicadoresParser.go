package main

import (
	"os"
	"fmt"
	"log"
    "github.com/tealeg/xlsx"
)

func main() {

	excelFileName := "./Indicadores-cantonales_Censos-2000-y-2011_resumen.xlsx"
	xlFile, err := xlsx.OpenFile(excelFileName)
	if err != nil {
		log.Println(err)
		os.Exit(1)
	}
	parseAct(xlFile)
}

func parseAct(file *xlsx.File){
    for _, sheet := range file.Sheets {
		for i := 7; i < len(sheet.Rows[3].Cells); i+=3 {
			str2000 := ""
			str2011 := ""
			for j := 4; j < 51; j++ {
				if ignoreRange(j) {
					continue
				}
				//log.Println(i, j, len(sheet.Rows), sheet.Rows[j].Cells)
				n := sheet.Rows[j].Cells[i].String()
				m := sheet.Rows[j].Cells[i+1].String()
				if j != 50 {
					str2000 += fmt.Sprintf("%s,",n)
					str2011 += fmt.Sprintf("%s,",m)
				}else{
					str2000 += fmt.Sprintf("%s",n)
					str2011 += fmt.Sprintf("%s",m)
				}
			}
			canton := sheet.Rows[1].Cells[i].String()
			fmt.Println(canton+",2000,"+str2000)
			fmt.Println(canton+",2011,"+str2011)
		}
	}
}

func ignoreRange(k int) bool {
	igRange := []int{0,2,3,10,11,12,17,18,19,20,22,26,34,35,36,39,43,44,45}
	return intInSlice(k,igRange)
}

func intInSlice(a int, list []int) bool {
    for _, b := range list {
        if b == a {
            return true
        }
    }
    return false
}

/*
Índice del resultado
<provincia>,<año>,<Población total>,<Superficie (km2)>,<"Densidad de población Personas por km2">,<"Porcentaje de población urbana Personas que viven en zona urbana por cada 100">,<"Relación hombres-mujeres Hombres por cada 100 mujeres">,<"Relación de dependencia demográfica Personas dependientes (menores de 15 años o de 65 y más) por cada 100 personas en edad productiva (15 a 64 años)">,<Viviendas individuales ocupadas>,<"Promedio de ocupantes Promedio de personas por vivienda individual ocupada">,<Porcentaje de viviendas en buen estado>,<Porcentaje de viviendas hacinadas>,<Porcentaje de alfabetismo>,<10 a 24 años>,<25 y más años>,<Escolaridad promedio>,<25 a 49 años>,<50 o más años>,<Porcentaje de asistencia a la educación regular>,<Menor de 5 años>,<5 a 17 años>,<18 a 24 años>,<25 y más años>,<Personas fuera de la fuerza de trabajo (15 años y más)>,<Tasa neta de participación>,<Hombres>,<Mujeres>,<Porcentaje de población ocupada no asegurada>,<Porcentaje de población nacida en el extranjero>,<Porcentaje de población con discapacidad>,<Porcentaje de población no asegurada>,<Porcentaje de hogares con jefatura femenina>,<Porcentaje de hogares con jefatura compartida>
*/