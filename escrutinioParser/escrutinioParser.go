package main

import (
	"os"
	"fmt"
	"log"
    "github.com/tealeg/xlsx"
)

func main() {

	for i := 1; i < 13; i++ {
		excelFileName := fmt.Sprintf("./actas/ActaSesion%d.xlsx",i)
		xlFile, err := xlsx.OpenFile(excelFileName)
		if err != nil {
			log.Println(err)
			os.Exit(1)
		}
		parseAct(xlFile)
	}
}

func parseAct(file *xlsx.File){
    for _, sheet := range file.Sheets {
		for i := 1; i < len(sheet.Rows[2].Cells); i++ {
			for j := 2; j < 22; j++ {
				k,_:= sheet.Rows[j].Cells[i].Int()
				if j != 21 {
					fmt.Printf("%d,",k)
				}else{
					fmt.Printf("%d",k)
				}
			}
			fmt.Printf("\n")
		}
	}
}