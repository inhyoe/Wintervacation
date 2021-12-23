public class 랩8 {
    public static void main(String[] args) {
        class MyClass{
            public int i = 3;
        }
        Object o = new Object();
        MyClass obj = new MyClass();
        System.out.println("i =" + obj.i);
    }
}
