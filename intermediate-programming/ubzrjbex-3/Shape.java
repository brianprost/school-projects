/*
Brian Prost
Shape.java
08 November 2020
 */

package ubzrjbexGuerr;

import java.awt.*;
import java.awt.Rectangle;

public abstract class Shape extends Rectangle {

    // instance variables
    Color shapeColor;
    boolean isShapeSolid;

    // class variable to hold number of shapes
    public static int numberOfShapesCreated = -1;

    // constructor to....wait for it....construct the shape
    public Shape(Rectangle r, Color shapeColor, boolean isShapeSolid) {
        super(r);
        this.shapeColor = shapeColor;
        this.isShapeSolid = isShapeSolid;
        numberOfShapesCreated++; // iterate number of shapes
    }

    // sets the color
    void setColor(Graphics g) {
        this.shapeColor = g.getColor();
    }

    // is shape solid or hollow? this method will tell you just that
    boolean getSolid(Graphics g) {
        return this.isShapeSolid;
    }

    // grabs the number of shapes created so far
    public static int getNoOfShapes() {
        return numberOfShapesCreated;
    }

    // abstract method that accepts a Graphics object as a parameter
    abstract void draw(Graphics g);

}