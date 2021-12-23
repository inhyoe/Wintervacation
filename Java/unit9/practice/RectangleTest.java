package Java.unit9.practice;

import org.w3c.dom.css.Rect;

interface Comparable {
    int compareTo(Object other);
}

class Rectangle implements Comparable {
    public int width = 0;
    public int height = 0;

    public String toString() {
        return "Rectangle [width" + width + ", hegiht =" + height + "j";
    }

    public Rectangle(int w, int h) {
        width = w;
        height = h;
        System.out.println(this);

    }

    public int getArea() {
        return width * height;

    }

    public int compareTo(Object other) {
        Rectangle otherRect = (Rectangle) other;
        if (this.getArea() < otherRect.getArea())
            return -1;
        else if (this.getArea() > otherRect.getArea())
            return 1;
        else
            return 0;
    }
}

public class RectangleTest {

}
