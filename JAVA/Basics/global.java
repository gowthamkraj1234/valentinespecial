public class global {
    static int a;
    static String b;
    static boolean c;
    public static void main(String[] args){
        String s="Local variable";
        System.out.println(s);
        System.out.println("Default value of a is " + a);
        a=100;
        System.out.println("After initialization:" + a);
        System.out.println("Default value of b is " + b);
        System.out.println("Default value of c is " + c);

    }
}
