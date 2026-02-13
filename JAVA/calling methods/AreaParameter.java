// Parameter Type Method Program
public class AreaParameter {

    final static double pi = 3.14;

    static void square(int side) {
        System.out.println("Area of Square = " + (side * side));
    }

    static void rectangle(int l, int b) {
        System.out.println("Area of Rectangle = " + (l * b));
    }

    static void triangle(int b, int h) {
        System.out.println("Area of Triangle = " + (0.5 * b * h));
    }

    static void parallelogram(int b, int h) {
        System.out.println("Area of Parallelogram = " + (b * h));
    }

    static void circle(int r) {
        System.out.println("Area of Circle = " + (pi * r * r));
    }

    static void ellipse(int a, double b) {
        System.out.println("Area of Ellipse = " + (pi * a * b));
    }

    static void trapezoid(int a, int b, int h) {
        System.out.println("Area of Trapezoid = " + (0.5 * (a + b) * h));
    }

    public static void main(String[] args) {
        square(5);
        rectangle(6, 4);
        triangle(8, 5);
        parallelogram(6, 4);
        circle(5);
        ellipse(7, 4.2);
        trapezoid(4, 6, 5);
    }
}
