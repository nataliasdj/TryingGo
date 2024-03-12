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
    public static void pattern13(int n){
        int num = 0;
        for(int i = 0; i < n; i++){
            for(int x = 0; x < i+1; x++){ // or instead of i+1 do x <= i
                num+=1;
                System.out.print(num + " ");
            }
        System.out.println();
        }
    }
    public static void pattern14(int n){
        char start = 'A';
        for(int i = 0; i < n; i++){
            for(int x = 0; x < i+1; x++){ // or instead of i+1 do x <= i
                System.out.print(start + " ");
                start+=1;
            }
            start = 'A';
        System.out.println();
        }
    }
    public static void pattern15(int n){
        char start = 'A';
        for(int i = 0; i < n; i++){
            for(int x = n; x >i ; x--){ // or instead of i+1 do x <= i
                System.out.print(start + " ");
                start+=1;
            }
            start = 'A';
        System.out.println();
        }
    }
    public static void pattern16(int n){
        char start = 'A';
        for(int i = 0; i < n; i++){
            for(int x = 0; x <= i; x++){ // or instead of i+1 do x <= i
                System.out.print(start + " ");
            }
            start+=1;
        System.out.println();
        }
    }
    public static void pattern17(int n){
        char start = 'A';
        for(int i = 0; i < n; i++){
            for(int x = 0; x < n-i-1; x++){System.out.print(" ");}
            for(int x = 0; x < 2*i+1; x++){
                if (x < (2*i+1)/2){
                    System.out.print(start);
                    start += 1;
                }
                else{
                    System.out.print(start);
                    start -= 1;
                }
            }
            for(int x = 0; x < n-i-1; x++){System.out.print(" ");}
        start = 'A';
        System.out.println();
        }
    }
    public static void pattern18(int n){
        for (int i = 0; i < n; i++){
            char letter = 'A';
            letter += n - 1 - i;
            for (int j = 0; j <= i; j++){
                System.out.print(letter);
                letter += 1;
            }
            System.out.println();
        }
    }
    public static void pattern18_way2(int n){
        for (int i = 0; i < n; i++){
            for (char ch = (char)('E'-i); ch <= 'E'; ch++){
            // for (char ch = 'E'-i; ch < 'E'; ch++){
                System.out.print(ch);
            }
            System.out.println();
        }
    }
    public static void pattern19(int n){
        for(int i=0; i < n; i++){
            for(int j=0; j < n-i; j++){
                System.out.print("*");
            }
            for(int k=0; k < i*2; k++){
                System.out.print(" ");
            }
            for(int l=0; l < n-i; l++){
                System.out.print("*");
            }   
            System.out.println();
        }

        for(int x = 0; x < n; x++){
            for(int m=0; m <= x; m++){
                System.out.print("*");
            }
            for(int o=0; o < (n-x-1)*2; o++){
                System.out.print(" ");
            }
            for(int p=0; p <= x; p++){
                System.out.print("*");
            }
            System.out.println();
        }
        
    }
    public static void pattern20(int n){
        for(int i = 0; i < n; i++){
            for(int k = 0; k <= i; k++){
                System.out.print("*");
            }
            for(int l = 0; l < (n-i-1)*2; l++){
                System.out.print(" ");
            }
            for(int m = 0; m <= i; m++){
                System.out.print("*");
            }
            System.out.println();
        }
        for(int j=1;j<n;j++){
            for (int k = 0; k < n-j; k++){System.out.print("*");}
            for (int l = 0; l < j*2; l++){System.out.print(" ");}
            for (int m = 0; m<n-j; m++){System.out.print("*");}
            System.out.println();
        }
    }
    public static void pattern21(int n){
        for(int i = 0; i<n; i++){System.out.print("*");}
        for (int j = 0; j <n-2;j++){
            int input = n;
            System.out.println();
            System.out.print("*");
            while(input>2){
                System.out.print(" ");
                input-=1;
            }
            System.out.print("*");
        }
        System.out.println();
        for(int j = 0; j<n; j++){System.out.print("*");}
        
    }
    public static void pattern22(int n){
        
    }
    public static void main(String[] args) {
        // pattern12(5);
        // pattern13(5);
        // pattern14(5);
        // pattern15(5);
        // pattern16(5);
        // pattern17(5);
        // pattern18(5);
        // pattern18_way2(5);
        // pattern19(5);
        // pattern20(5);
        pattern21(5);
    }

}