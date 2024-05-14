package main

import (
	"fmt"
	"sync" //for concurrency
	"time"
)

func main() {
	//goroutines()
	//channels() //way to enable goroutinges to pass around info, main feature hold data, thread safe - avoid data erasing, listen for data, also we can block code till one of them is met
	generic() // allows say u want a function that can hv similar functions for say int and float etc
}
func generic() {
	var intSlice = []int{1, 2, 3}
	fmt.Println("sumslice int using generic:", sumSlice[int](intSlice))
	fmt.Println("sumslice empty int using any:", isEmpty[int](intSlice))

	var float32Slice = []float32{1, 2, 3}
	fmt.Println("float32slice float using generic:", sumSlice[float32](float32Slice))
	fmt.Println("float32slice empty float using any:", isEmpty[float32](float32Slice))
	fmt.Println("float32slice empty float using any shorthand v:", isEmpty(float32Slice))
}
func sumSlice[T int | float32 | float64](slice []T) T { //bad example for any bcs not all types are compatible with the += so try isempty say
	var sum T
	for _, v := range slice {
		sum += v
	}
	return sum
}
func isEmpty[T any](slice []T) bool {
	return len(slice) == 0
}

// THIS IS DEADLOCK
//
//	func channels() {
//		var c = make(chan int) //to make a channel syntax make chan int- this channel can only hold 1 int val
//		c <- 1                 //this add value 1, channel is like an array c:[1] and only has 1 size//this code blocks until sth reads from it
//		var i = <-c //now it looks like this c: [] and i =1//its like 1 is popped from the channel and put into i so channel is empty now
//		fmt.Println("This is i:", i) //its a deadlock
//	}
func channels() {
	var c = make(chan int)
	var bc = make(chan int, 5) //buffer channel can store 5 ints
	go process(c)
	fmt.Println("This is c:", <-c) //directily printing the popped out thing, we wait here to set value in channel, and goroutinges set the val and exit func and main function knows its already set so then they print
	go process2(c)
	for i := range c { //i is val of channel, iterate over the channel
		fmt.Println("This is i process channel:", i) //so we created the channel and start goroutine, in main function we wait at top of for loop for sth to be added to the channel,
	}
	go process2(bc)
	for j := range bc {
		fmt.Println("This is i process buffer:", j)
		time.Sleep(time.Second * 1) //1s, process func stays active until main is done, but process doesnt really have to wait, it can just exit -putting this makes it so main can just go ahead and keep reading while process is done
	}
}

func process(c chan int) {
	c <- 123
}
func process2(c chan int) {
	defer close(c) // to this close right b4 func exits
	for i := 0; i < 5; i++ {
		c <- i //we have to read from channel multiple times in the main right
		//here we add 0 to channel, main func read from channel, and cont to i=5
	}
	fmt.Println("Exiting process")
}

var dbData = []string{"id1", "id2", "id3", "id4", "id5"}
var wg = sync.WaitGroup{} //for concurrency - kinda like counters,
var m = sync.Mutex{}      // when 2 multiple threads modify the same data aka results memory location in the same time, is not good
// a normal mutex drawback is completely locking other goroutines to not touch what is inside, in this case result, u can use sync rwmutex which is read write
var mrw = sync.RWMutex{}
var results = []string{}

func goroutines() {
	/*
		1 cpu core way to launch mult func executing concurrencly, before we do task1 then task2 and say dbcall() func takes 3 seconds in task1, while waiting for dbcall we can switch to task 2, after getting respond back from dbcall then we go back to task1

		basic def = (aka mult tasks in progress at the same time)

		or thru parralel execution where ex there are 2 cpu cores and so task1 is on cpu core 1 and ask2 on cpu core2, this is also part of concurrency but using parralel execution
	*/
	// t0 := time.Now() //if uncomment it will call dbcall always which always has a wg.done so it will crash
	// for i := 0; i < len(dbData); i++ {
	// 	dbCall(i) //call 3 times  2s, which currently is being called one by one, to do it concurrently u put go in the front
	// }
	// fmt.Printf("Total execution time not concurrently: %v\n", time.Since(t0)) // takes a while right

	t1 := time.Now()
	for i := 0; i < len(dbData); i++ {
		wg.Add(1)    //when we spawn a new go routine, add 1 and call done which decrements the counter, done in the dbCall()
		go dbCall(i) //immediately exit b4 printing bcs is not waiting, for it to wait then continue, use synch package in import
	}
	wg.Wait()                                                             // wait for counter to come back to 0 meaning all task are completed and rest of code executes
	fmt.Printf("Total execution time concurrently: %v\n", time.Since(t1)) // takes a while right
	fmt.Printf("The results are %v\n", results)

}
func dbCall(i int) { //simulate db call delay
	var delay float32 = 2000
	time.Sleep(time.Duration(delay) * time.Millisecond)
	//before using the rwlock
	// fmt.Println("The result from the database is: ", dbData[i])
	// m.Lock() //check if lock already set by another go routine? if yes, wait here until lock is released and set lock itself
	// results = append(results, dbData[i]) //without mutex there might be faulty data - aka we tinker this then unlcok
	// m.Unlock()
	save(dbData[i])
	log()
	wg.Done() //to decrement
}

/*in summary, this pattern alows miltiple goroutinges to read from our slice at the same time but only blocking when writes are happening in contrast if we dont have rlock, even reads can happen only one at a time
 */
func save(result string) {
	m.Lock() //in order to proceed all locks full and read must be released - this prevents us accessing the slice while other goroutines are writeing or reading the results
	results = append(results, result)
	m.Unlock()
}
func log() {
	mrw.RLock() //when we reach here, they check if there is a full lock (lock type just Lock) if lock method exists then it will wait b4 its released before continuing so we not reading while results is being written to,
	//if no full lock then goroutine acquire a readlock and then proceed with rest of code, u can have rlock at same time - also, these readlock, blocks code execution at m.lock, when go routines hits the m.lock,
	fmt.Println("The current result from the database is: ", results)
	mrw.RUnlock()

}
