/*
Brian Prost
Oval.java
subclass of Shape.java
08 November 2020
 */

package homeworkGuerr;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Rectangle;

public class Oval extends Shape {

    // initialize the characteristics of the shape
    public Oval(Rectangle r, Color shapeColor, boolean isShapeSolid) {
        super(r, shapeColor, isShapeSolid);
    }

    // draws oval on the graphic
    @Override
    void draw(Graphics g) {
        g.fillOval(this.x, this.y, this.width, this.height);
    }
}