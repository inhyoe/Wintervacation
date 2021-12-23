class C{
    public int myMethod(int a, int b){
        return 0;
    }
}
class K extends C{
    public int myMethod(int a, int b) {return 1; }
   }
public class 랩3 {
    public static void main(String[] args) {
        K b = new K();
        System.out.println("x =" + b.myMethod(0, 1));
    }
}
