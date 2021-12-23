package Java.unit6.ex.new_ex;

class Employee{
    String name;
    String address;
    protected int salaray;
    private int rrn;
    /* public int setname(){
        return name;
    } */ // int형이 아닌 String 형.
    public String setname(){ return name; }
    public void getname(String name){ this.name = name; }
    public String setaddress(){ return address; }
    public void getaddress(String address){ this.address = address; }
    public int setsalary(){ return salaray; }
    public void getsalary(int salaray){ this.salaray = salaray; }
    public int setrrn(){ return rrn; }
    public void getrrn(int rrn){ this.rrn = rrn; }

  /*   public Employee(String name, String address, int salary, int rrn){
        this.name = name;
        this.address = address;
        this.salaray = salary;
        this.rrn = rrn;
    }

    public String toString(){
        return "Employee [name = "+ name + ", address=" + address + ", salary =" + salaray + ",rrn= " + rrn +"]";
    } */ // 위의 코드를 이렇게 함축할 수도 있다.
}


public class mployee extends Employee{
    public static void main(String[] args) {
        Employee just = new Employee();
        Employee manager = new Employee();
        just.getname("최주형");
        just.setname();
        just.getaddress("서울시");
        just.setaddress();
        just.getsalary(2500000);
        just.setsalary();
/*         just.setrrn(990203);
        just.getrrn();
 */    // 접근 한정자이기때문에 안된다.

        System.out.println("이름: " + just.setname() + "\n주소 : "+ just.setaddress()+ "\n연봉 : " + just.setsalary() );

}
    
}
