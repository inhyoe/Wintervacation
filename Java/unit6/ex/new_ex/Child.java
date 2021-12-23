package Java.unit6.ex.new_ex;


class Parents { 
    public void print(){
        System.out.println(" 부모클래스의 print()메소드 ");
    }
}
public class Child extends Parents{
    public void print(){
        super.print();
        System.out.println(" 오버라이딩한 자식클래스의 print()메소드");
    }
    public static void main(String[] args) {
        Child obj = new Child();
        obj.print();
    }

    
}
