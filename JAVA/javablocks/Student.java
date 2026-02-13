package javablocks;
import java.util.Scanner;
public class Student {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the obtained marks:");
        int marks = sc.nextInt();
        if (marks >= 35){
            System.out.println("Pass");
        }
        else{
            System.out.println("Fail");
        }
    
}
}
