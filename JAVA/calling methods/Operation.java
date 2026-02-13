class Addition{
    public static void Add(){
        System.out.println("Addition of two numbers is: " +(70+42));

    }
}
class Subtraction{
    public static void Sub(){
        System.out.println("Subtraction of two numbers is: " + (172-30));
    }
}
class Multiplication{
    public static void mul(){
        System.out.println("Multiplication of two numbers is: " + (4*2));
    }
}

public class Operation {
    public static void main(String[] args) {
        Addition.Add();
        Subtraction.Sub();
        Multiplication.mul();
    }
}
