package main

import (
	"os"
	"fmt"
	"log"
    "github.com/tealeg/xlsx"
)

func main() {
	//totalActas := 13 // 1ra ronda
	totalActas := 9 // 2da ronda
	for i := 1; i < totalActas; i++ {
		excelFileName := fmt.Sprintf("./actasRonda2/ActaSesion%d.xlsx",i)
		xlFile, err := xlsx.OpenFile(excelFileName)
		if err != nil {
			log.Println(err)
			os.Exit(1)
		}
		parseAct(xlFile)
	}
}

func parseAct(file *xlsx.File){
		//votingOptions := 22 // 1ra ronda
		votingOptions := 11 // 2da ronda
    for _, sheet := range file.Sheets {
		for i := 1; i < len(sheet.Rows[2].Cells); i++ {
			for j := 2; j < votingOptions; j++ {
				k,_:= sheet.Rows[j].Cells[i].Int()
				if j != votingOptions-1 {
					fmt.Printf("%d,",k)
				}else{
					fmt.Printf("%d",k)
				}
			}
			fmt.Printf("\n")
		}
	}
}
