public class Result {
    public static double seventhsem(String USN){
        int sub1=85;
        int sub2=90;
        int sub3=88;
        int sub4=90;
        int sub5=77;
        int sub6=80;
        double result=(sub1+sub2+sub3+sub4+sub5+sub6)/6.0;
        return result;

    }
    public static void main(String[] args) {
        System.out.println(seventhsem("4MH22IS029"));
        double res=seventhsem("4MH22IS029");
        System.out.println("4MH22IS029's result is: " + res);
}
}
