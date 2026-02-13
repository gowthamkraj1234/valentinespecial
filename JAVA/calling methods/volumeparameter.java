public class volumeparameter {

    final static double pi = 3.14;

    static void cube(int side) {
        System.out.println("Volume of Cube = " + (side * side * side));
    }

    static void cuboid(int l, int b, int h) {
        System.out.println("Volume of Cuboid = " + (l * b * h));
    }

    static void sphere(int r) {
        System.out.println("Volume of Sphere = " + ((4.0/3) * pi * r * r * r));
    }

    static void cylinder(int r, int h) {
        System.out.println("Volume of Cylinder = " + (pi * r * r * h));
    }

    static void cone(int r, int h) {
        System.out.println("Volume of Cone = " + ((1.0/3) * pi * r * r * h));
    }

    public static void main(String[] args) {
        cube(5);
        cuboid(6, 4, 3);
        sphere(5);
        cylinder(4, 7);
        cone(4, 7);
    }
}
