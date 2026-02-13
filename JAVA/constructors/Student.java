package constructors;

public class Student {
    String name;
    int age;
    int marks;
    Student(String name, int age, int marks) {
        this.name = name;
        this.age = age;
        this.marks = marks;
    }
    public static void main(String[] args) {
        Student s = new Student("Gowtham", 21, 85);
        System.out.println("Student name: "+s.name);
        System.out.println("Student age: "+s.age);
        System.out.println("Student marks: "+s.marks);
}
}
