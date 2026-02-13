class volumereturn {

    final static double pi = 3.14;

    public int cube(int side) {
        return side * side * side;
    }

    public int cuboid(int l, int b, int h) {
        return l * b * h;
    }

    public double sphere(int r) {
        return (4.0/3) * pi * r * r * r;
    }

    public static void main(String[] args) {

        volumereturn v = new volumereturn();

        System.out.println("Volume of Cube = " + v.cube(5));
        System.out.println("Volume of Cuboid = " + v.cuboid(6,4,3));
        System.out.println("Volume of Sphere = " + v.sphere(5));
    }
}
