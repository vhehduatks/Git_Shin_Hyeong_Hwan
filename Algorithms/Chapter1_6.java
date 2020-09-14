package Algorithms;

public class Chapter1_6 {
    Integer[] array = new Integer[] { 5, 6, 3, 2, 1 };
    int max = array[0];
    int min = array[0];

    void clac(){
        for (int i : array) {
            if (i > max) 
                max = i;
        
            if (i < min) 
                min = i;
            
        }
        System.out.println("max_val="+max);
        System.out.println("min_val="+min);
    }

    public static void main(String[] args) {
        Chapter1_6 func=new Chapter1_6();
        func.clac();
    }

}
