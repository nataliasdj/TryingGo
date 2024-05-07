package main

import (
	"errors" // for error type
	"fmt"
	"unicode/utf8"
)

func main() {
	//basics()
	//functions()
	arrays()
}
func arrays() {

}
func functions() {
	printMe("START OF FUNCTIONS FUNC")
	printMe("yay functions")
	num1, num2, num3 := 6, 2, 0
	var result int = intDivision(num1, num2)
	fmt.Println("result for dividing nums:", result)
	var result2, remainder2 int = intDivision2(num1, num2)
	fmt.Printf("(2nd intdiv func) The result of the division is %v with remainder %v\n", result2, remainder2)

	// with error handling and if statements or switch
	var result3, remainder3, err3 = intDivision3(num1, num3)
	switch {
	case err3 != nil:
		fmt.Println(err3.Error())
	case remainder3 == 0:
		fmt.Printf("The result of the division is %v", result3)
	default:
		fmt.Printf("The result of the division is %v with remainder %v", result3, remainder3)
	}
}

//if looks like this
// if err3 != nil {
// 	fmt.Println(err3.Error())
// } else if remainder3 == 0 {
// 	fmt.Printf("The result of the division is %v", result3)
// } else {
// 	fmt.Printf("The result of the division is %v with remainder %v", result3, remainder3)
// }

func intDivision(numerator int, denominator int) int { //the last int is the return type
	var result int = numerator / denominator
	return result
}

// if accidentally divid eby 0 got error later, so to combat see indiv3
func intDivision2(numerator int, denominator int) (int, int) { //the last int is the return type - multiple returns
	var result int = numerator / denominator
	var remainder int = numerator % denominator
	return result, remainder
}

// if func can have error so hv return type error and vals u returning
func intDivision3(numerator int, denominator int) (int, int, error) { //the last int is the return type - multiple returns
	var err error //type error, default value nil
	if denominator == 0 {
		err = errors.New("cannot divide by zero")
		return 0, 0, err
	}
	var result int = numerator / denominator
	var remainder int = numerator % denominator
	return result, remainder, err
}

func printMe(printValue string) {
	fmt.Println(printValue)
}

func basics() {
	fmt.Println("START OF BASICS FUNC aka vars, declaring, types etc")
	fmt.Println("First print: Hello World!")
	var floatNum32 float32 = 10.1
	var intNum32 int32 = 2
	var result float32 = floatNum32 + float32(intNum32) //must cast

	fmt.Println("Result of adding the floats:", result)

	var myString string = "yo \n haha" + " " + "check this out"
	fmt.Println(myString)
	fmt.Println("Testing length:", len("testlength")) // number of bytes not length of the word if you wnat use utf8.runeCountInString
	fmt.Println("Testing length again: ", utf8.RuneCountInString("testinglengthagain"))

	var myRune rune = 'a'             //single char
	fmt.Println("myRune is:", myRune) //will give 97
	//also got the bool type, the normal

	var intNum3 int
	fmt.Println("testing default:", intNum3) //can do this, will give default value which is 0, string and bool gives empty str and false respectively

	var myVar = "text" //type is inferred
	myVar2 := "text"   //shorthand ver
	fmt.Println("just printing:", myVar, myVar2)

	const myConst string = "const val" //const cant change, not like var, must initalize val immediately - sorta like global
	fmt.Println("testing const:", myConst)
}
