package constructors;

public class Employee {
    String Emp_name;
    int Emp_id;
    double Emp_salary;
    public Employee(String name, int id, double salary) {
        System.out.println("Employee name: "+name);
        System.out.println("Employee id: "+id);
        System.out.println("Employee salary: "+salary);
}
    public static void main(String[] args) {
        Employee emp1 = new Employee("Gowtham", 123, 50000);
        System.out.println("Empl_name: "+emp1.Emp_name);
        System.out.println("Empl_id: "+emp1.Emp_id);
        System.out.println("Emp_salary: "+emp1.Emp_salary);
    }
}
