package javablocks;
import java.util.Scanner;
public class Bank {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the credit score:");
        int creditScore = sc.nextInt();
        System.out.println("Enter the salary:");
        double salary = sc.nextDouble();
        if (creditScore >= 700){
            if (salary >= 50000){
                System.out.println("You are eligible for a loan");
            }
            else{
                System.out.println("You are not eligible for a loan:Low salary");
            }
    }
        else{
            System.out.println("You are not eligible for a loan:Low credit score");
        }
    }
}
