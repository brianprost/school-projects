/*
Brian Prost
Drawing.java
08 November 2020
 */

package ubzrjbexGuerr;

import javax.swing.JPanel;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Rectangle;

import static Project3.Shape.getNoOfShapes;
import static Project3.Shape.numberOfShapesCreated;

public class Drawing extends JPanel {

    // variable to hold current shape
    public Shape currentShape = new Oval(new Rectangle(0, 0, 0, 0), Color.white, false);

    // method to draw current shape and number of shapes
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.drawString(String.valueOf(currentShape.numberOfShapesCreated), 10, 10);
        g.setColor(currentShape.shapeColor);
        if (currentShape instanceof Oval) {
            if (currentShape.isShapeSolid) {
                g.fillOval(currentShape.x, currentShape.y, currentShape.width, currentShape.height);
            } else {
                g.drawOval(currentShape.x, currentShape.y, currentShape.width, currentShape.height);
            }
        } else if (currentShape instanceof Rectangular) {
            if ((currentShape.isShapeSolid)) {
                g.fillRect(currentShape.x, currentShape.y, currentShape.width, currentShape.height);
            } else {
                g.drawRect(currentShape.x, currentShape.y, currentShape.width, currentShape.height);
            }
            g.setColor(currentShape.shapeColor);
        }
    }

    // specify dimensions
    @Override
    public Dimension getPreferredSize() {
        return new Dimension(200, 200);
    }

    // save new shape to currentShape variable
    public void drawShape(Shape s) throws OutsideBounds {
        // check to make sure that the shape is not out of bounds
        if (s.height > 200 || s.width > 200) {
            throw new OutsideBounds();
        } else {
            this.currentShape = s;
            // draw shape on graphic
            paintComponent(getGraphics());
        }
    }
}
