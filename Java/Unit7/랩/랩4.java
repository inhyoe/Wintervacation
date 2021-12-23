class ClassA{
    public void methodOne(int i){}
    public void methodTwo(int i){}
    public static void methodThree(int i){}
    public static void methodfour(int i){}
}


public class 랩4 extends ClassA{
    public static void methodOne(int k, int i){}
    public void methodTwo(int i){} // 재정의
    public void methodThree(int i){}
    public static void methodFour(int i){} // 가린다
    
}
