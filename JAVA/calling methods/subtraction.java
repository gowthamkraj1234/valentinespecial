// By passing arguments to the method we can perform different operations on the same method. Here we are performing subtraction and division by passing different arguments to the same method.

class subtraction{
    public static void sub(int a,double b){
        double c=a-b;
        System.out.println("The difference of a and b is: "+c);
    }
    public static void division(double a, int b){
        double c=a/b;
        System.out.println("The division of a and b is: "+c);
    }
    public static void main(String[] args) {
        
        sub(10,21.4);
        sub(72,40.0);
        division(47.0,2);
        division(90.0,15);
    }
}