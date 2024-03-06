class Letsgo {
    public static void pattern12(int n){
        for(int i = 0; i < n; i++){
            int num = 0;
            for(int x = 0; x < i+1; x++){ // or instead of i+1 do x <= i
                num+=1;
                System.out.print(num);
            }
            for(int y = 0; y < ((n*2)-(2*i)-2); y++){
            // for(int y = 0; y <= 2*(n-1); y++){
                System.out.print(" ");
            }
            for(int z = 0; z < i+1; z++){
                System.out.print(num);
                num-=1;

            }
        System.out.println();
        }
    }
    
    public static void main(String[] args) {
        pattern12(5);
    }
}