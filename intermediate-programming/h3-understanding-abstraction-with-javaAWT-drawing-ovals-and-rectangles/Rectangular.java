/*
Brian Prost
Rectangular.java
subclass of Shape.java
08 November 2020
 */

package homeworkGuerr;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Rectangle;

public class Rectangular extends Shape {

    // initialize the characteristics of the shape
    public Rectangular(Rectangle r, Color shapeColor, boolean isShapeSolid) {
        super(r, shapeColor, isShapeSolid);
    }

    // draws rectangle on the graphic
    @Override
    void draw(Graphics g) {
        g.drawRect(this.x, this.y, this.width, this.height);
    }
}
