

class Date {
    private int year;
    private int month;
    private int date;

    Date(int year, int month, int date) {
        this.year = year;
        this.month = month;
        this.date = date;
    }

    public String toString() {
        return "Date [year = " + year + ",month= " + month + ",date = " + date + "]";
    }
}

class Employee {
    private String name;
    private Date birthdDate; // birthDate = 변수 Date = 자료형은 아

    public Employee(String name, Date birthDate) {
        this.name = name;
        this.birthdDate = birthDate;
    }

    @Override
    public String toString() {
        return "Employye [ name =" + name + ",birthDate = " + birthdDate + "]";
    }
}

public class Has_A관계 {
    public static void main(String[] args) {
        Date birth = new Date(1990, 8, 17);
        Employee em = new Employee("유창훈", birth);
        System.out.println(birth);
        System.out.println(em);
    }
}
