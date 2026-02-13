// Direct Method Program
public class AreaDirect {

    final static double pi = 3.14;

    static void square() {
        int side = 5;
        System.out.println("Area of Square = " + (side * side));
    }

    static void rectangle() {
        int l = 6, b = 4;
        System.out.println("Area of Rectangle = " + (l * b));
    }

    static void triangle() {
        int b = 8, h = 5;
        System.out.println("Area of Triangle = " + (0.5 * b * h));
    }

    static void parallelogram() {
        int b = 6, h = 4;
        System.out.println("Area of Parallelogram = " + (b * h));
    }

    static void circle() {
        int r = 5;
        System.out.println("Area of Circle = " + (pi * r * r));
    }

    static void ellipse() {
        int a = 7;
        double b = 4.2;
        System.out.println("Area of Ellipse = " + (pi * a * b));
    }

    static void trapezoid() {
        int a = 4, b = 6, h = 5;
        System.out.println("Area of Trapezoid = " + (0.5 * (a + b) * h));
    }

    public static void main(String[] args) {
        square();
        rectangle();
        triangle();
        parallelogram();
        circle();
        ellipse();
        trapezoid();
    }
}
