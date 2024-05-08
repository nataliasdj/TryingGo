package main

import (
	"errors" // for error type
	"fmt"
	"strings"
	"unicode/utf8"
)

func main() {
	//basics()
	//functions()
	//arrays_and_maps()
	//string_bytes_runes()
	//structs_interfaces()
	pointers()
}
func square_formula(thing2 [5]float64) [5]float64 {
	fmt.Printf("The memory location fo thing2 arr is: %p\n", &thing2)
	for i := range thing2 {
		thing2[i] = thing2[i] * thing2[i]
	}
	return thing2
}
func square_formula_with_ptr(thing2 *[5]float64) [5]float64 {
	fmt.Printf("The memory location fo thing2 arr is: %p\n", &thing2)
	for i := range thing2 {
		thing2[i] = thing2[i] * thing2[i]
	}
	return *thing2
}
func pointers() {
	/*ptr vars stores mem location*/
	var ptr *int32 //takes 32/64 bits - ptr doesnt point to anything aka no address asigned to it
	//also u may not dereference ptr if you havent asigned to anything
	var ptr2 *int32 = new(int32) //ptr stores a mem location
	var i int32
	fmt.Printf("ptr points to nothing: %v\nptr2 already have a location: %v\ni (normal var): %v\nthe value ptr2 point to(aka after dereferencing - also 0 cuz its default for int32):%v\n", ptr, ptr2, i, *ptr2)
	*ptr2 = 10 //after dereferencing then assign
	fmt.Printf("The value ptr2 point to(aka after dereferencing and assigning):%v\n", *ptr2)

	//can also do this
	ptr2 = &i //which means ptr2 points to the memory address of i, so both p and i reference the same thing in memory
	*ptr2 = 1 //will also change value of i

	var k int32 = 2
	i = k //is diff from the above cuz ke still has its own memory and its just copying i's value

	//slices is like using pointers thus
	var slice = []int32{1, 2, 3}
	var sliceCopy = slice
	sliceCopy[2] = 4
	fmt.Println("Print slice:", slice)
	fmt.Println("Print sliceCopy:", sliceCopy)
	// why are they slice also changed if we only change slicecopy, is cuz slices copy pointers

	//POINTERS AND
	//see prints stmnt, thing1 and thing2 mem location differ aka they 2 diff arrays, so u can change thing 2 without affecting thing1 - this results in extra memory aka not needed, so u can use pointers so it wont waste em
	var thing1 = [5]float64{1, 2, 3, 4, 5}
	fmt.Printf("The memory location fo thing1 arr is: %p\n", &thing1)
	var result [5]float64 = square_formula(thing1)
	fmt.Printf("The result is: %v\n", result)
	fmt.Printf("The value of thing1 is: %v\n", thing1)

	//basically just do this - which thing1 and thing2 points the same
	//look at placements of & and *, it was so hard to follow
	var result_with_ptr [5]float64 = square_formula_with_ptr(&thing1)
	fmt.Printf("The result is: %v\n", result_with_ptr)
	fmt.Printf("The value of thing1 is: %v\n", thing1)
}

// STRUCTS is like your own type--------------------------------------------------------
type gasEngine struct { //syntax = type(keyword) then your name of type then struct{} - can hold mixed types in forms of field which r defined by names, fields can also by another struct
	mpg     uint8
	gallons uint8
}
type owner struct {
	name string
}
type gasEngineOwner struct { //usually u put it above the main but purpose of this is to learn i think better put here
	mpg       uint8
	gallons   uint8
	ownerInfo owner //or just owner as below
}
type gasEngineOwner2_moreShorthand struct { //more shorthand
	mpg     uint8
	gallons uint8
	owner
	//can also just put int if you want, no name or anything
	//see anonymous struct in the struct func
}

//the diff looks like this
/*
myEngine
mpg: , gallons:, ownerInfo.name:
but if use shorthanded v, looks like this
mpg:, gallons:, name:
*/

// calc miles left in a gastank
// see type gasEngine being used? thus why the method can use the field
func (e gasEngine) milesLeft() uint8 {
	return e.gallons * e.mpg
}

type electricEngine struct {
	mpkw uint8 //miles per killowat
	kwh  uint8 //how much charge left in battery
}

func (e electricEngine) milesLeft() uint8 {
	return e.mpkw * e.kwh
}

func canMakeIt(e gasEngine, miles uint8) {
	if miles <= e.milesLeft() {
		fmt.Println("You can make it")
	} else {
		fmt.Println("Nope you need to refuel")
	}
}

// at first can only take gas, what if we want a more general to take in electric too - aka interface{} so make engine interface - then just change the above method as below

type the_interface_engine interface {
	milesLeft() uint8 //specify the signature from the method signature
}

// to make this method work it just needs the milesleft() as per the interface
func canMakeItAfterInterface(e the_interface_engine, miles uint8) {
	if miles <= e.milesLeft() {
		// return "You can make it"
		fmt.Println("You can make it")
	} else {
		// return "You cant make it, refuel"
		fmt.Println("Nope you need to refuel")
	}
}

func structs_interfaces() {
	var myEngineName gasEngine
	fmt.Println("Printing gasEngine1 struct, not defined yet:", myEngineName.mpg, myEngineName.gallons)

	var myEngineName2 gasEngine = gasEngine{mpg: 25, gallons: 15}
	fmt.Println("Printing gasEngine2 struct, already defined:", myEngineName2.mpg, myEngineName2.gallons)

	//if you want shorthand, all fields must be assigned cant only 1 - must be inorder
	var myEngineName3 gasEngine = gasEngine{25, 15}
	myEngineName3.gallons = 20
	fmt.Println("Printing gasEngine3 struct, already defined by omission and if you want to change in the middle:", myEngineName3.mpg, myEngineName3.gallons)

	var myEngineName4 gasEngineOwner = gasEngineOwner{25, 15, owner{"Alex"}}
	fmt.Println("Printing gasEngine4 struct, inside struct:", myEngineName4.mpg, myEngineName4.gallons, myEngineName4.ownerInfo.name)

	var myEngineName5 gasEngineOwner2_moreShorthand = gasEngineOwner2_moreShorthand{25, 15, owner{"Alex"}}
	fmt.Println("Printing gasEngine4 struct, inside struct:", myEngineName5.mpg, myEngineName5.gallons, myEngineName5.name)

	//anonymous struct, can define and initalize in same location - but not reusable
	var myEngineAnon = struct {
		mpg     uint8
		gallons uint8
	}{25, 15} // if want to create another struct must to this var = struct again
	fmt.Println("Printing anonymous struct:", myEngineAnon.mpg, myEngineAnon.gallons)

	//Structs can also have methods - func directly tied to the struct, and have access to struct instance itself
	//is like classes, u instantiate a glass with the var bla bla like so below, then calling method
	var myEngineName6 gasEngine = gasEngine{25, 15}
	fmt.Println("Printing gasEngine6 using methods miles left:", myEngineName6.milesLeft())

	var myEngineName7 electricEngine = electricEngine{25, 15}

	//learnt it the hardway but i think you cant as follows the canmakeit has a fmt.println - it has no return value and i was using it like it has a return value
	//fmt.Println("Printing myEngine7 using the interface allowing general usage no matter what struct was used:",canMakeItAfterInterface(...))
	fmt.Println("Printing myEngine7 using the interface allowing general usage no matter what struct was used:")
	canMakeItAfterInterface(myEngineName7, 50)

}
func string_bytes_runes() {
	/*string represented by binary
	strings in go is basically value reprented by bytes, if u want, better cast it to runes aka
	rune is an alias for int32
	*/
	var myString = "résumé"
	var myString2 = []rune("résumé") //rune is unicode point nums
	var indexed = myString[0]
	fmt.Printf("Index 0 (r)): %v, %T\n", indexed, indexed) //gives the ascii and type is uint
	for k, v := range myString {
		fmt.Println("Iterating résumé:", k, v) //gives index and ascii - also if u see output, it skips index 2 so why, basically the e accent takes up the 8 bits twice, bcs of utf8 encoding, r is 8 bits, e accent is 16 bits, s is 8, etc the last e accent is also 16 - is a special character
	}
	fmt.Printf("The length of 'myString' is %v\n", len(myString))  //length of bytes not chars
	fmt.Printf("Index 1 (é)): %v, %T\n", myString[1], myString[1]) //it got seperated with its other 8 bits, read long paragraph on the loop, thus why but if u cast it to rune, then it wont get seperated, 233 is the right one
	fmt.Printf("Index 1 (é) with rune): %v, %T\n", myString2[1], myString2[1])

	//String building + string is immutable, cant be modified
	var strSlice = []string{"h", "e", "l", "l", "o"}
	var catStr = ""
	for i := range strSlice {
		//we create new string right which not efficient, so import built in string
		catStr += strSlice[i] //create new string everytime
	}
	fmt.Printf("Before string builder: %v\n", catStr)
	var strBuilder strings.Builder
	for i := range strSlice {
		//array allocated internally, values then appended
		strBuilder.WriteString(strSlice[i]) //instead of +=
	}
	var catStr2 = strBuilder.String() //then string is created
	fmt.Printf("After string builder: %v\n", catStr2)

}
func arrays_and_maps() {
	//can initalize like all 4
	var arr [3]int32 //array is 3 & fixed like normal - default val of element types which is 0
	var arr2 [3]int32 = [3]int32{1, 2, 3}
	arr3 := [3]int32{4, 5, 6}
	arr4 := [...]int32{7, 8, 9} // still arr fixed size 3, is inferred

	arr[1] = 123
	fmt.Println("array 1, index 0:", arr[0])
	fmt.Println("array 1, index 1&2", arr[1:3])

	fmt.Println("array 1, mem 0 location:", &arr[0]) // memory location if & - the first 4 bytes
	fmt.Println("array 1, mem 1 location:", &arr[1])
	fmt.Println("array 2:", arr2)
	fmt.Println("array 3:", arr3)
	fmt.Println("array 4:", arr4)

	//SLICES------------
	var intSlice []int32 = []int32{10, 11, 12, 13, 14} //omitting length value becomes a slice bcs no fixed length i think, so can do like so....
	fmt.Printf("Length of slicearray is %v with capacity %v\n", len(intSlice), cap(intSlice))
	intSlice = append(intSlice, 15) // store in diff memory, like arraylist ish, copy and put the appended in diff array
	fmt.Printf("Length of slicearray after append is %v with capacity %v\n", len(intSlice), cap(intSlice))
	//Although capacity is longer than length, cannot index if longer than curr length

	var intSlice2 []int32 = []int32{16, 17}
	intSlice = append(intSlice, intSlice2...) //,must use ... (spread operator)
	fmt.Println("appending slice 1 to 2:", intSlice)

	var intSlice3 []int32 = make([]int32, 3, 8) // specify length ex. 3 and optionally the capacity ex.8 otherwise capacity is default of length if not given, best practice put capacity if u know
	fmt.Println("slice3:", intSlice3)

	//MAPS
	var myMap map[string]uint8 = make(map[string]uint8) //key string, val is unsigned int 8
	fmt.Println("myMap:", myMap)
	var myMap2 = map[string]uint8{"Jill": 23, "Claire": 45, "Ada": 35}
	fmt.Println("map2, key Jill:", myMap2["Jill"])
	fmt.Println("map2, key Wesker not in map", myMap2["Wesker"]) //key not exist aka gives default val, careful

	var age, ok = myMap2["Chris"] //can return 2 val boolean
	if ok {
		fmt.Printf("The age of who you looking for %v\n", age)
	} else {
		fmt.Println("Invalid name")
	}
	delete(myMap2, "Claire") //built in delete (map,key) - no return val cuz delete by reference

	//no order for maps when loops
	for name := range myMap2 { //for loop key and val
		fmt.Printf("Loop1: Name: %v\n", name)
	}
	for name, age := range myMap2 { //for loop key and val
		fmt.Printf("Loop2: Name: %v, Age: %v\n", name, age)
	}

	for key, val := range arr {
		fmt.Printf("Loop3: Index: %v, Value: %v\n", key, val)
	}

	var i int = 0 //closest you will get to a while loop cuz go dont have
	fmt.Println("Demonstration of for that looks like while loop")
	for i < 3 {
		fmt.Println(i)
		i = i + 1
	}
	fmt.Println("or 2nd loop syntax")
	i = 0
	for {
		if i >= 3 {
			break
		}
		fmt.Println(i)
		i = i + 1
	}
	fmt.Println("or 3rd loop syntax")
	for i := 0; i < 3; i++ {
		fmt.Println(i)
	}

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
