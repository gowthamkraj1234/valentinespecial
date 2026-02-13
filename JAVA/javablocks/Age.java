package javablocks;
import java.util.Scanner;
public class Age {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the age:");
        int age = sc.nextInt();
        if (age <21){
            System.out.println("complete your studies");
        }
        else if (age >= 21 && age < 60){
            System.out.println("go for job");
        }
        else{
            System.out.println("enjoy your life");
        }
    }
}
