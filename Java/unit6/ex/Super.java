package Java.unit6.ex;
class Parent{
    void print(){
        System.out.println("부모 클래스의 print() 메소드");
    }
}
public class Super extends Parent {
    void print(){
        super.print(); // 부모 클래스의 메소드 호출
        System.out.println("자식 클래스의 print() 메소드");
        // 오버라이딩
    }
    public static void main(String[] args) {
        Super obj = new Super();
        obj.print();
    }
}
