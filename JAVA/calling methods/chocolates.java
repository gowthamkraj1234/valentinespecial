class five_star{
    public void content(){
        System.out.println("coco");
        System.out.println("Peanuts");
        System.out.println("Sugar");
    }
}
class milkybar{
    public void content( String s){
        System.out.println(s);
    }
}
class lollipop{
    public String content(){
        System.out.println("Sugar "+"color "+"flavor");
        System.out.println("Preservatives");
        return "lollipop";   
    }
}
class chocolates{
    public static void main(String[] args) {
        new five_star().content();
        new milkybar().content("milkproducts");
        System.out.println(new lollipop().content());
    }
}