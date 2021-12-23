package Java.unit6.ex.new_ex.unit6_3생성자;
class Mycounter{

    int counter;

    Mycounter(int value){ // 생성자.
        
        counter = value;
    }
}
public class CounterTest {
    public static void main(String[] args) {
        Mycounter c = new Mycounter(10); // 이때, c는 참조변수이다.
        Mycounter c2 = new Mycounter(20);
        System.out.println("c1 = "+c.counter);
        System.out.println("c2 = "+c2.counter);
        
    }
}
