public class volume1 {
   public void cuboid(int h){
    int l=10;
    int b=15;
    int v=l*b*h;
    System.out.println("Volume of cuboid is "+v);

   }
   public double cone(int r,int h){
    final double pi=3.14;
    double v=(pi*r*r*h)/3;
    return v;
   } 
   String s="Hello";
   public static void main(String[] args) {
    volume1 ref=new volume1();
    ref.cuboid(10);
    System.out.println("Volume of cone is "+ref.cone(5,7));
    System.out.println(ref.s);
    System.out.println(ref);
    volume1 ref1=new volume1();
    System.out.println(ref1);
   }
}
