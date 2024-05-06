package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {
	fmt.Println("Hello World!")
	var floatNum32 float32 = 10.1
	var intNum32 int32 = 2
	var result float32 = floatNum32 + float32(intNum32) //must cast

	fmt.Println(result)

	var myString string = "yo \n haha" + " " + "check this out"
	fmt.Println(myString)
	fmt.Println(len("testlength")) // number of bytes not length of the word if you wnat use utf8.runeCountInString
	fmt.Println(utf8.RuneCountInString("testinglengthagain"))

	var myRune rune = 'a'              //single char
	fmt.Println("myRune is =", myRune) //will give 97
	//also got the bool type, the normal

}
