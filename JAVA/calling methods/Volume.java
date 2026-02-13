class cube{
    public static void  vol(int a){
        int voc=a*a*a;
        System.out.println("Volume of cube is: " + voc);
    }
}
class cone{
    public static void vol(double r, int h){
        final double pi=3.14;
        double voc=(pi*r*r*h)/3;
        System.out.println("Volume of cone is: " + voc);
    }
}
class sphere{
    public static double vol(){
        final double pi=3.14;
        int r =10;
        double vos=(4*pi*r*r*r)/3;
        return vos;
    }
}
class cylinder{
    public static double vol(double pi,int r,int h){
        double voc=pi*r*r*h;
        return voc;
    }
}
public class Volume {
    public static void main(String[] args) {
        cube.vol(5);
        cone.vol(4.5,7);
        System.out.println("Volume of sphere is: " + sphere.vol());
        System.out.println("Volume of cylinder is: " + cylinder.vol(3.14, 6,8));
    }
}
