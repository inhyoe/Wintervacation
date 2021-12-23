package Java.unit6.ex;

class Employee1 {
    String name; // +는 public
    String address; // 아무것도 없을땐 그냥
    protected int salary; // # 은 protected
    private int rrn; // -는 private

    public Employee1(String name, String address, int salary, int rrn) {
        this.name = name;
        this.address = address;
        this.salary = salary;
        this.rrn = rrn;
    }

    public String toString() {
        return "Employee [ name=" + name + ", address =" + address
                + ",salary =" + salary + ", rrn= " + rrn + "]";
    }

    void test() {
        System.out.println("name =" + name);
        System.out.println("address =" + address);
        System.out.println("salary =" + salary);
        System.out.println("rrn =" + rrn);
    }
}

class Manager extends Employee1 {
    private int bonus;

    public Manager(String name, String address, int salary, int rrn, int bonus) {
        super(name, address, salary, rrn);
        this.bonus = bonus;
    }

    void test() {
        System.out.println("name =" + name);
        System.out.println("address =" + address);
        System.out.println("salary =" + salary);
        // System.out.println("rrn =" + rrn);
    }

}

public class Employee {
    public static void main(String[] args) {
        Employee1 e = new Employee1("장애", "왕지동", 500, 789012);
        Manager m = new Manager("병신", "복현동", 1000, 123456, 25);
        System.out.println(m);
        m.test();
        e.test();
    }
}
