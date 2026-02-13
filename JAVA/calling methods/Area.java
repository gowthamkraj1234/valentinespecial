// Direct method
public class Area {
    final static double pi=3.14;
    public static void circle(){
        int r=5;
       double result=pi*r*r;
        System.out.println("The area of the circle is: "+result);
    }
    public static void ellipse(){
        int a=7;
        double b=4.2;
        double result=pi*a*b;
        System.out.println("The area of the ellipse is: "+result);

}
public static void main(String[] args) {
    circle();
    ellipse();
}
}
