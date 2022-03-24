/*
Brian Prost
Project3.java
This program draws two types of shapes based on user input.
08 November 2020
 */

package homeworkGuerr;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.Rectangle;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Project3 extends JFrame {

    // shape type
    private JLabel shapeTypeLabel = new JLabel("Shape Type");
    private String[] shapeTypeOptions = { "Oval", "Rectangle" };
    private JComboBox shapeTypeChooser = new JComboBox(shapeTypeOptions);

    // fill type
    private JLabel fillTypeLabel = new JLabel("Fill Type");
    private String[] fillTypeOptions = { "Solid", "Hollow" };
    private JComboBox fillTypeChooser = new JComboBox(fillTypeOptions);

    // color
    private JLabel colorTypeLabel = new JLabel("Color");
    private String[] colorTypeOptions = { "Black", "Red", "Orange", "Yellow", "Green", "Blue", "Magenta" };
    private JComboBox colorTypeChooser = new JComboBox(colorTypeOptions);

    // width
    private JLabel widthLabel = new JLabel("Width");
    private JTextField widthChoice = new JTextField(9);

    // height
    private JLabel heightLabel = new JLabel("Height");
    private JTextField heightChoice = new JTextField(9);

    // x coordinate
    private JLabel xLabel = new JLabel("X Coordinate");
    private JTextField xChoice = new JTextField(9);

    // y coordinate
    private JLabel yLabel = new JLabel("Y Coordinate");
    private JTextField yChoice = new JTextField(9);

    // draw button
    private JButton drawButton = new JButton("Draw");

    // drawing panels
    private static JPanel panelToBeDrawnOn = new JPanel();
    private static Drawing drawingPanel = new Drawing();

    // shape color
    private static Color shapeColor = null;

    public Project3() {

        // setup frame
        super("Geometric Drawing");
        setSize(500, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null); // centers frame
        setLayout(new FlowLayout());

        // first panel for user entry points
        JPanel userInputPanel = new JPanel();
        userInputPanel.setLayout(new GridLayout(7, 2, 0, 2));

        // add all labels and text fields to panel
        userInputPanel.add(shapeTypeLabel);
        userInputPanel.add(shapeTypeChooser);
        userInputPanel.add(fillTypeLabel);
        userInputPanel.add(fillTypeChooser);
        userInputPanel.add(colorTypeLabel);
        userInputPanel.add(colorTypeChooser);
        userInputPanel.add(widthLabel);
        userInputPanel.add(widthChoice);
        userInputPanel.add(heightLabel);
        userInputPanel.add(heightChoice);
        userInputPanel.add(xLabel);
        userInputPanel.add(xChoice);
        userInputPanel.add(yLabel);
        userInputPanel.add(yChoice);

        // add userInputPanel
        add(userInputPanel);

        // setup panelToBeDrawnOn
        panelToBeDrawnOn.setBorder(BorderFactory.createTitledBorder("Shape Drawing"));
        panelToBeDrawnOn.setLayout(new FlowLayout());
        // setup drawingPanel
        drawingPanel.setSize(getPreferredSize());
        // add drawingPanel to panelToBeDrawnOn
        panelToBeDrawnOn.add(drawingPanel);
        // add panelToBeDrawnOn to Frame
        add(panelToBeDrawnOn);

        // setup and add the button
        drawButton.addActionListener(new drawButton());
        add(drawButton);
    }

    // listener for drawButton
    private class drawButton implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {

            // assemble avengers!...i mean Rectangle object
            Rectangle r = new Rectangle();
            try {
                r.height = Integer.parseInt(heightChoice.getText());
                r.width = Integer.parseInt(widthChoice.getText());
                r.x = Integer.parseInt(xChoice.getText());
                r.y = Integer.parseInt(yChoice.getText());
            } catch (NumberFormatException nfe) {
                JOptionPane.showMessageDialog(null, "All entries must be an integer.",
                        "Alert", JOptionPane.WARNING_MESSAGE);
            }

            // grab color selection
            int shapeColorSelection = colorTypeChooser.getSelectedIndex();
            switch (shapeColorSelection) {
                case 0 -> shapeColor = Color.black;
                case 1 -> shapeColor = Color.red;
                case 2 -> shapeColor = Color.orange;
                case 3 -> shapeColor = Color.yellow;
                case 4 -> shapeColor = Color.green;
                case 5 -> shapeColor = Color.blue;
                case 6 -> shapeColor = Color.magenta;
            }

            // is the object filled or hollow?
            boolean isShapeFilled = false;
            if (fillTypeChooser.getSelectedIndex() == 0) {
                isShapeFilled = true;
            } else if (fillTypeChooser.getSelectedIndex() == 1) {
                isShapeFilled = false;
            }

            // construct shape object for rectangle or oval
            if (shapeTypeChooser.getSelectedIndex() == 0) { // oval
                Oval o = new Oval(r, shapeColor, isShapeFilled);
                try {
                    drawingPanel.drawShape(o);
                } catch (OutsideBounds outsideBounds) {
                    outsideBounds.printStackTrace();
                }
            } else if (shapeTypeChooser.getSelectedIndex() == 1) { // rectangle
                Rectangular rectangle = new Rectangular(r, shapeColor, isShapeFilled);
                try {
                    drawingPanel.drawShape(rectangle);
                } catch (OutsideBounds outsideBounds) {
                    outsideBounds.printStackTrace();
                }
            }
        }
    }

    // main method
    public static void main(String[] args) throws Exception {
        try {
            Project3 p3 = new Project3();
            p3.setVisible(true);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}