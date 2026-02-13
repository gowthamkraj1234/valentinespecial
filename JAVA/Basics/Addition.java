public class Addition {
    public static void Add(){
        System.out.println("Add() starts");
        int a=10;
        int b=20;
        int c=a+b;
        System.out.println("The addition of a and b is "+c);
        System.out.println("Add() ends");
    }
    public static void main(String[] args) {
        System.out.println("Main() starts");
        Add();
        System.out.println("Main() ends");
    }
}
